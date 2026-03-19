# Power Apps Code Apps Docs Map

Snapshot date: 2026-03-19

Use Microsoft Learn as the primary source of truth for platform behavior. Start from the docs index, then open the smallest page that answers the task.

## Core entry points

- Docs index: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/>
- Overview: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview>
- Quickstart: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/quickstart>
- Architecture: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/architecture>

## Important current guidance

- The docs index groups content into `Get started`, `Build`, `Deploy`, `Monitor`, `Manage`, and `Troubleshoot`.
- The architecture page says the main moving parts are:
  - the Power Apps client library for code apps
  - generated models and services for connectors
  - `power.config.json`
  - the Power Apps host
- The architecture page says `pac code push` packages the built app for publishing to a Power Platform environment.

## Setup and CLI guidance

- New npm CLI quickstart: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/npm-quickstart>
- As of the 2026-03-05 Learn page snapshot, the new npm CLI is preview and is included starting with the Power Apps client library for code apps version `1.0.4`.
- That page says the npm CLI exposes `init`, `run`, and `push`.
- That page says the older Power Platform CLI `pac code` commands are deprecated in a future release.
- Local dev note from the same page: Chrome and Edge changed local network access behavior in December 2025, which can affect localhost development and iframe embedding.

## Build and data docs

Use these when the user asks how to connect or structure app behavior:

- Connect to data: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-data>
- Connect to Copilot Studio: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-copilot-studio>
- Connect to Dataverse: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-dataverse>
- Get Dataverse tables metadata: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/get-dataverse-tables-metadata>
- Connect to Azure SQL: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-azure-sql>
- SharePoint operations: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/sharepoint-operations>
- Analyze data requests and responses: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/analyze-data-requests-responses>
- Get context data: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/get-context-data>
- Embed in an iframe: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/embed-iframe>

## Deploy, monitor, and admin docs

- Application lifecycle management (ALM): browse from the docs index if the direct page path changes.
- Manage PAC CLI code telemetry: browse from the docs index.
- Set up Azure App Insights: browse from the docs index.
- Configure Content Security Policy (CSP): <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/content-security-policy>
- Migrate your code to v1.0: browse from the docs index.

## High-signal troubleshooting docs

- Troubleshoot adding a data source: <https://learn.microsoft.com/en-us/power-apps/developer/code-apps/troubleshoot-add-datasource>
- Zscaler issues: browse from the docs index if needed.

The data-source troubleshooting page is especially useful when `pac code add-data-source` fails. The 2026-03-19 snapshot says to:

- verify the latest Power Platform CLI
- verify auth and environment context with `pac auth create` and `pac auth list`
- compare `Environment ID` from `pac env who` against `power.config.json`
- ensure `region` is `prod` unless intentionally targeting a different region

## CSP notes

The CSP page says:

- CSP is configured at the environment level for code apps.
- Default `connect-src` is `'none'`.
- Custom directive values are appended to defaults unless the default is `'none'`.
- CSP can be configured in the Power Platform admin center or through the Environment Management Settings API.

## Practical research order

1. Open the docs index to orient yourself.
2. Open the architecture page if you need to explain how the platform fits together.
3. Open the npm quickstart when setup or publishing commands matter.
4. Open targeted how-to or troubleshoot pages for the exact connector, admin feature, or failure mode.
5. Only after that, use repo samples and GitHub discussions to fill in gaps or current friction.
