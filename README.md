# PowerApps Code Apps Explorer

Reusable Codex sub-agent skill for researching and troubleshooting Microsoft Power Apps code apps.

## Install In Codex

Codex loads local skills from your Codex home skills directory.

On Windows, the usual target is:

```powershell
$CODEX_HOME\skills\powerapps-codeapps-explorer
```

### Option 1: Clone, then copy the skill folder

```powershell
git clone https://github.com/ranjith7022/powerapps-codeapps-explorer-agent.git
Copy-Item -Recurse -Force .\powerapps-codeapps-explorer-agent\powerapps-codeapps-explorer "$env:CODEX_HOME\skills\powerapps-codeapps-explorer"
```

### Option 2: Copy from this local workspace

```powershell
Copy-Item -Recurse -Force .\powerapps-codeapps-explorer "$env:CODEX_HOME\skills\powerapps-codeapps-explorer"
```

### Verify

Confirm this file exists after copying:

```powershell
Get-Item "$env:CODEX_HOME\skills\powerapps-codeapps-explorer\SKILL.md"
```

### Use

Invoke it by name in Codex:

```text
Use $powerapps-codeapps-explorer to research a Power Apps code apps deployment issue.
```

## Use From VS Code

Open this repo in VS Code and run the bundled tasks from `Terminal` -> `Run Task`.

Available tasks:

- `Codex: Install PowerApps Skill`
- `Codex: Verify PowerApps Skill`
- `Codex: Refresh GitHub Signals`
- `Codex: Refresh GitHub Signals (JSON)`

These tasks live in `.vscode/tasks.json`.

## What is included

- `powerapps-codeapps-explorer/SKILL.md`
  - trigger description and workflow for the sub-agent
- `powerapps-codeapps-explorer/references/`
  - official docs map
  - upstream repo map
  - GitHub issue and discussion snapshot
- `powerapps-codeapps-explorer/scripts/fetch_repo_signals.py`
  - live GitHub signal refresh script for current open issues and discussions

## Focus areas

- Microsoft Learn docs for code apps
- `microsoft/PowerAppsCodeApps` templates and samples
- current GitHub issues and discussions
- npm CLI and `pac code` transition guidance
- Dataverse, SharePoint, ALM, CSP, and troubleshooting context
