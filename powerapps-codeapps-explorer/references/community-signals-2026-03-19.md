# PowerAppsCodeApps Community Signals

Snapshot date: 2026-03-19

Primary sources:

- Issues: <https://github.com/microsoft/PowerAppsCodeApps/issues>
- Discussions: <https://github.com/microsoft/PowerAppsCodeApps/discussions>

Use this file as a starting snapshot only. Refresh live data with `python scripts/fetch_repo_signals.py --format markdown` whenever the task depends on current bugs or newly answered discussions.

## Current issue hotspots

### Connection references and data-source generation

These are some of the highest-signal open issues in the current snapshot:

- `#267` `pac code list-connection-reference command not working`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/267>
- `#266` `pac code add-data-source fails with Connection Reference`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/266>
- `#214` `pac code add-data-source -cr fails with "Failed to resolve connection ID"`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/214>
- `#241` `pac code list-connection-references returns null for logical name`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/241>
- `#242` `pac code add-data-source does not populate tableId and version in dataSourcesInfo.ts`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/242>
- `#212` `Connection References issue`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/212>

If the user mentions connection references, `-cr`, `list-connection-reference`, or local data connectivity failures, inspect these before assuming user error.

### Deployment, pipeline, and service principal failures

- `#244` `Service principal auth fails on Code App update`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/244>
- `#231` `Code Apps not deployed using Deployment Pipeline`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/231>
- `#217` `DevOps Pipeline using Power Platform Build Tools fails on unpack`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/217>
- `#200` `Anomalies when building Power Platform Code Apps with Azure DevOps ALM`
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/200>

If the failure appears only in CI or deployment automation, start with these issues and then open the ALM docs.

### Connector-specific and generated-code bugs

- `#245` SQL stored procedure execution issue
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/245>
- `#243` Oracle tabular data source issue
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/243>
- `#230` binary body parameters upload corrupted files
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/230>
- `#206` SharePoint connector 404 because `{dataset}` path parameter is not populated
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/206>
- `#209` Blob storage and Business Central connections not working
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/209>
- `#213` unable to connect to Fabric SQL Database
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/213>
- `#166` SharePoint table with whitespace and underscores fails to connect
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/166>
- `#171` Azure Databricks data source naming mismatch
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/171>

### Type generation and runtime behavior

- `#210` decimal fields generated as string
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/210>
- `#205` yes/no fields generated incorrectly
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/205>
- `#197` multiselect picklist generated as single value
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/197>
- `#216` unable to retrieve full-size Dataverse images
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/216>
- `#199` display issue when embedded in an iframe within a model-driven app
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/199>
- `#272` MSAL browser auth and Graph API redirect URI problem due to dynamic iframe URL
  - <https://github.com/microsoft/PowerAppsCodeApps/issues/272>

## Current discussion hotspots

Recent open discussions on 2026-03-19 include:

- `#271` Best approach for handling SharePoint document uploads and environment switching
  - <https://github.com/microsoft/PowerAppsCodeApps/discussions/271>
- `#270` Unable to view data when running in dev
  - <https://github.com/microsoft/PowerAppsCodeApps/discussions/270>
- `#268` CORS issue for SharePoint images
  - <https://github.com/microsoft/PowerAppsCodeApps/discussions/268>
- `#269` Support triggering Power Automate flows from Code Apps
  - <https://github.com/microsoft/PowerAppsCodeApps/discussions/269>
- `#222` PAYG licensing
  - <https://github.com/microsoft/PowerAppsCodeApps/discussions/222>
- `#264` SharePoint connector missing support for list attachments
  - <https://github.com/microsoft/PowerAppsCodeApps/discussions/264>
- `#225` `pac code push` returns 500 with service principal auth
  - <https://github.com/microsoft/PowerAppsCodeApps/discussions/225>
- `#220` Known issue: `pac code push` fails with `httpClient` error in PAC CLI `v2.3.2`
  - <https://github.com/microsoft/PowerAppsCodeApps/discussions/220>

Other recurring discussion themes in the snapshot:

- permissions and environment variables
- SharePoint document library support
- display-name ergonomics in `pac code init`
- PWA support
- lookup implementation proposals

## Practical heuristics from the community snapshot

- If `pac code push` fails, check CLI version immediately and inspect both issue `#244` and discussion `#220`.
- If `add-data-source` fails, especially with connection references, inspect the connection-reference cluster before assuming auth or syntax mistakes.
- If SharePoint file, image, or document-library behavior is involved, inspect both issues and discussions because the pain spans bugs and missing features.
- If the question is about licensing, permissions, or environment variables, discussions currently carry more signal than issues.
- If the task involves browser auth inside the code app runtime, flag the iframe-hosting model as a likely constraint and treat direct browser auth patterns skeptically.
