#!/usr/bin/env python3
"""Fetch current GitHub issues and discussions for a repo."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


THEMES = [
    ("connection-reference", ("connection reference", "list-connection-reference", "list-connection-references", "add-data-source -cr")),
    ("deployment", ("deployment pipeline", "devops", "alm", "service principal", "push", "unpack", "pipeline")),
    ("sharepoint", ("sharepoint", "document", "attachment", "cors")),
    ("dataverse", ("dataverse", "picklist", "lookup", "tableid", "odata", "image")),
    ("connector", ("connector", "sql", "oracle", "blob", "business central", "fabric", "databricks")),
    ("auth", ("auth", "msal", "graph api", "login", "redirect uri")),
    ("runtime", ("iframe", "cache", "dev", "localhost", "csp")),
]


def fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": "Codex"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_json(url: str):
    return json.loads(fetch_text(url))


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    return " ".join(html.unescape(value).split())


def classify(title: str) -> list[str]:
    lowered = title.lower()
    matches = [name for name, keywords in THEMES if any(keyword in lowered for keyword in keywords)]
    return matches or ["other"]


def fetch_issues(repo: str, limit: int) -> list[dict]:
    url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100"
    payload = fetch_json(url)
    issues = []
    for item in payload:
        if "pull_request" in item:
            continue
        issues.append(
            {
                "number": item["number"],
                "title": item["title"],
                "created_at": item["created_at"],
                "updated_at": item["updated_at"],
                "url": item["html_url"],
                "themes": classify(item["title"]),
            }
        )
        if len(issues) >= limit:
            break
    return issues


def parse_discussion_entries(repo: str, html_text: str) -> list[dict]:
    repo_pattern = re.escape(repo)
    title_pattern = re.compile(
        rf'href="/{repo_pattern}/discussions/(?P<number>\d+)"[^>]*class="[^"]*discussion-Link--secondary[^"]*"[^>]*>(?P<title>.*?)</a>',
        re.S,
    )
    author_pattern = re.compile(r'href="/(?P<author>[^"/]+)">')
    time_pattern = re.compile(r'<relative-time datetime="(?P<dt>[^"]+)"')
    category_pattern = re.compile(rf'href="/{repo_pattern}/discussions/categories/[^"]+">(?P<category>[^<]+)</a>')

    results = []
    seen = set()
    matches = list(title_pattern.finditer(html_text))
    for index, match in enumerate(matches):
        number = int(match.group("number"))
        if number in seen:
            continue
        seen.add(number)

        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(html_text)
        window = html_text[start:end]

        author_match = author_pattern.search(window)
        time_match = time_pattern.search(window)
        category_match = category_pattern.search(window)

        results.append(
            {
                "number": number,
                "title": strip_tags(match.group("title")),
                "created_at": time_match.group("dt") if time_match else "",
                "author": author_match.group("author") if author_match else "",
                "category": strip_tags(category_match.group("category")) if category_match else "",
                "url": f"https://github.com/{repo}/discussions/{number}",
                "themes": classify(strip_tags(match.group("title"))),
            }
        )
    return results


def fetch_discussions(repo: str, limit: int) -> list[dict]:
    entries = []
    page = 1
    while len(entries) < limit and page <= 3:
        url = f"https://github.com/{repo}/discussions?discussions_q={quote('is:open')}&page={page}"
        html_text = fetch_text(url)
        parsed = parse_discussion_entries(repo, html_text)
        if not parsed:
            break
        entries.extend(parsed)
        page += 1
    return entries[:limit]


def summarize(items: Iterable[dict]) -> list[tuple[str, int]]:
    counter = Counter()
    for item in items:
        counter.update(item["themes"])
    return sorted(counter.items(), key=lambda pair: (-pair[1], pair[0]))


def format_markdown(repo: str, issues: list[dict], discussions: list[dict]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# GitHub Signals for {repo}",
        "",
        f"Generated: {now}",
        "",
        "## Open issue themes",
    ]
    for theme, count in summarize(issues):
        lines.append(f"- {theme}: {count}")
    lines.extend(["", "## Latest open issues"])
    for issue in issues:
        created = issue["created_at"][:10]
        themes = ", ".join(issue["themes"])
        lines.append(f"- #{issue['number']} ({created}) {issue['title']} [{themes}]")
        lines.append(f"  {issue['url']}")

    lines.extend(["", "## Latest open discussions"])
    for discussion in discussions:
        created = discussion["created_at"][:10]
        category = discussion["category"] or "Unknown"
        themes = ", ".join(discussion["themes"])
        lines.append(f"- #{discussion['number']} ({created}) {discussion['title']} [{category}; {themes}]")
        lines.append(f"  {discussion['url']}")
    return "\n".join(lines) + "\n"


def format_json(repo: str, issues: list[dict], discussions: list[dict]) -> str:
    payload = {
        "repo": repo,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "issues": issues,
        "discussions": discussions,
    }
    return json.dumps(payload, indent=2) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch open GitHub issues and discussions for a repo.")
    parser.add_argument("--repo", default="microsoft/PowerAppsCodeApps", help="owner/name")
    parser.add_argument("--issues-limit", type=int, default=12, help="number of open issues to include")
    parser.add_argument("--discussions-limit", type=int, default=12, help="number of open discussions to include")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        issues = fetch_issues(args.repo, args.issues_limit)
        discussions = fetch_discussions(args.repo, args.discussions_limit)
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"Failed to fetch repo signals: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        sys.stdout.write(format_json(args.repo, issues, discussions))
    else:
        sys.stdout.write(format_markdown(args.repo, issues, discussions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
