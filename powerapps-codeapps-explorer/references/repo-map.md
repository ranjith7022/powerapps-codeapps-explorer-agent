# PowerAppsCodeApps Repo Map

Snapshot date: 2026-03-19

Primary repo: <https://github.com/microsoft/PowerAppsCodeApps>

Local clone in this workspace:

- `C:\Users\mailr\Desktop\now\codeapps-sub-agent\powerapps-codeapps-upstream`

## What the repo is for

The repo README describes Power Apps code apps as custom web apps that run natively within Power Apps by using standard web technologies such as React, TypeScript, and Vite alongside Power Platform connectors and data sources.

Use the repo for implementation patterns, templates, samples, tests, and current product-adjacent guidance. Do not use it as a substitute for official Learn docs when the question is about platform truth.

## Top-level areas

- `templates/`
  - `starter`: recommended template with React, Vite, Tailwind CSS, TanStack Query, and React Router
  - `vite`: minimal Vite + React template preconfigured for code apps
- `samples/`
  - `HelloWorld`
  - `FluentSample`
  - `StaticAssetTracker`
  - `Dataverse`
  - `tanstack-app`
- `plugin/`
  - plugin marketplace assets and built-in Power Apps plugin guidance
- `tests/`
  - Playwright end-to-end tests for templates
- `sessions/ppcc2025/`
  - conference and workshop material
- `docs/assets/`
  - documentation images and static assets

## Template usage patterns

`templates/README.md` currently shows this flow for both templates:

1. scaffold from `microsoft/PowerAppsCodeApps/templates/<template>#main`
2. `npm install`
3. `pac code init --environment [environmentId] --displayName [appDisplayName]`
4. `npm run dev`

The docs now also describe the newer npm CLI path, so check which flow the user is actually following before giving setup commands.

## Sample value by scenario

- `samples/HelloWorld`
  - simplest starting point for seeing the SDK integrated into a TypeScript app
- `samples/Dataverse`
  - strong reference for CRUD, lookup resolution, and generated services
- `samples/FluentSample`
  - larger learning sample with Fluent UI, Office 365, SQL, custom APIs, and routing
- `samples/StaticAssetTracker`
  - asset-management style workflow sample
- `samples/tanstack-app`
  - lightweight React and Vite baseline

## Plugin area

The repo includes a `plugin/` folder that matters if the user wants a sub-agent, Copilot workflow, or skill-oriented experience.

Important files discovered in the snapshot:

- `plugin/README.md`
- `plugin/power-apps-plugin/agents/code-app-architect.md`
- `plugin/power-apps-plugin/shared/version-check.md`
- multiple skills such as `create-power-app`, `add-dataverse`, `add-sharepoint`, `add-office365`, `deploy`, and `list-connections`

## High-signal guidance from the plugin

The plugin README says:

- it is a Copilot plugin for building Power Apps code apps with React and Vite
- it is preview
- it exposes skill-like commands for create, deploy, and connector-specific add flows

The `code-app-architect` agent file is especially useful as a distilled expert checklist. It emphasizes:

- skill-first workflows instead of ad-hoc scaffolding
- connector-first design instead of raw `fetch` or `axios`
- generated models and services in `src/generated/`
- `power.config.json` as the environment anchor
- Node.js `v22+`
- PowerShell invocation for `pac` on Windows
- a known `pac` CLI `2.3.2` push bug

## Local project inspection checklist

When a user shares a project, inspect these first:

- `power.config.json`
  - `environmentId`
  - `region`
- `package.json`
  - scripts
  - Power Apps package version
  - React, Vite, and toolchain versions
- `src/generated/`
  - services and models created by connector or Dataverse generation
- `src/`
  - whether the app actually uses generated services
  - whether raw network calls are being attempted
- pipeline files
  - whether build, pack, or deployment steps match the current code-app flow

## Common repo-backed heuristics

- Start from `templates/starter` unless the user explicitly wants a minimal base.
- Borrow patterns from `samples/Dataverse` before inventing custom data-service code.
- Check `plugin/` when designing an agent or skill for code apps work.
- Treat `.github/workflows/` and `tests/` as examples of how Microsoft is validating templates.
