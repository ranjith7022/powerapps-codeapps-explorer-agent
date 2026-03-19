---
name: powerapps-codeapps-explorer
description: Research, summarize, and troubleshoot Microsoft Power Apps code apps by using the official Microsoft Learn docs, the microsoft/PowerAppsCodeApps repository, and current GitHub issues/discussions. Use when Codex needs expert guidance on code apps architecture, templates, npm CLI or pac CLI workflows, generated connector services, Dataverse or SharePoint patterns, deployment or ALM behavior, CSP or App Insights setup, or recent platform bugs and community workarounds.
---

# PowerApps Code Apps Explorer

## Overview

Use this skill to explore the Power Apps code apps ecosystem before making recommendations, writing implementation plans, or debugging user projects. Ground answers in Microsoft Learn first, then use the upstream repo and current GitHub signals to explain what is documented, what is merely practiced in samples, and what is currently failing in the field.

## Workflow

### 1. Start with official docs

Open [references/docs-map.md](references/docs-map.md) first.

- Treat Microsoft Learn as the source of truth for platform capabilities, lifecycle, and admin settings.
- Prefer the docs index when orienting yourself, then jump to the smallest page that answers the task.
- For current setup guidance, explicitly check whether the task should use the new npm CLI flow or the older `pac code` flow.
- If the user asks for "latest", "current", or "recent", browse again instead of relying only on bundled notes.

### 2. Map the request to the upstream repo

Open [references/repo-map.md](references/repo-map.md) when the task touches templates, samples, generated code layout, plugin guidance, or repo conventions.

- Use the upstream repo to understand how Microsoft is scaffolding and demonstrating code apps in practice.
- Prefer `templates/starter` for opinionated React apps and `templates/vite` for minimal setups.
- Check `samples/` for real patterns before inventing an architecture from scratch.
- Check `plugin/` when the user wants agentic workflows, connector skills, or Codex/Copilot-oriented guidance.

### 3. Refresh GitHub signals for time-sensitive troubleshooting

Open [references/community-signals-2026-03-19.md](references/community-signals-2026-03-19.md) for the bundled snapshot, then refresh it for live troubleshooting with:

```bash
python scripts/fetch_repo_signals.py --repo microsoft/PowerAppsCodeApps --format markdown
```

- Use the live refresh whenever the task mentions open bugs, regressions, known issues, workarounds, discussions, announcements, or release friction.
- Treat the bundled community snapshot as a starting point, not a permanent truth.
- Call out exact issue or discussion numbers when they materially affect your recommendation.

### 4. Inspect the local app before prescribing fixes

For a user project, inspect these files first if they exist:

- `power.config.json`
- `package.json`
- `src/generated/`
- `src/`
- CI or pipeline files

Focus on:

- which initialization flow was used
- environment and region settings
- whether generated models/services exist and look current
- whether the app is trying to bypass connectors with raw HTTP
- whether the failure is local dev, publish, runtime, ALM, or admin-policy related

### 5. Troubleshoot by failure class

Use this decision order:

1. Version and toolchain mismatch
2. Environment mismatch or auth context mismatch
3. Data source generation problems
4. Connector-specific bugs or unsupported patterns
5. Deployment or pipeline behavior
6. Runtime sandbox, CSP, iframe, or browser restrictions

### 6. State certainty clearly

- Distinguish documented behavior from repo convention and from community workaround.
- Cite docs URLs and GitHub URLs when giving precise recommendations.
- If you infer a likely cause from issue patterns, label it as an inference.
- If multiple known bugs fit, present the shortest validation path instead of guessing.

## Reference Selection

- Open [references/docs-map.md](references/docs-map.md) for official Learn entry points and platform facts.
- Open [references/repo-map.md](references/repo-map.md) for templates, samples, plugin structure, and practical repo conventions.
- Open [references/community-signals-2026-03-19.md](references/community-signals-2026-03-19.md) for the 2026-03-19 GitHub snapshot.
- Run [scripts/fetch_repo_signals.py](scripts/fetch_repo_signals.py) when the task needs current issues or discussion activity.

## Guardrails

- Prefer official docs over assumptions.
- Prefer connector-backed patterns over raw external HTTP calls inside code apps.
- Treat GitHub issues and discussions as evidence of current friction, not as normative documentation.
- Prefer exact commands, file paths, and issue numbers over vague advice.
- Do not freeze time-sensitive recommendations; refresh current GitHub signals when needed.

## Output Expectations

When answering, usually provide:

- the most relevant docs page or pages
- the matching repo example or template
- any open issues or discussions that materially change the recommendation
- a concise next action list for the user
