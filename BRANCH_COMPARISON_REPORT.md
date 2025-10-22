# Branch Comparison Report

**Generated on:** 2025-10-22 16:41:45 UTC
**Total branches analyzed:** 192
**Comparison base:** main branch

---

## Table of Contents

- [Summary Statistics](#summary-statistics)
- [Branch Details](#branch-details)

---

## Summary Statistics

- **Branches ahead of main:** 191
- **Branches behind main:** 190
- **Branches in sync with main:** 1
- **Branches with file changes:** 190

### Top 10 Branches Most Ahead of Main

| Branch | Commits Ahead | Last Commit |
|--------|---------------|-------------|
| copilot/fix-6542 | 3655 | 2025-05-21 |
| copilot/fix-6210 | 3633 | 2025-05-19 |
| ekzhu-optional-thought-as-content | 3621 | 2025-05-12 |
| ekzhu-otel | 3609 | 2025-05-06 |
| mem | 3586 | 2025-05-21 |
| ekzhu-stream-group-message | 3551 | 2025-04-16 |
| gagb/qualcoder | 3501 | 2025-03-26 |
| rysweet-typescript | 3434 | 2025-03-06 |
| python-v0.4.9.3 | 3426 | 2025-03-28 |
| python-v0.4.9.2 | 3423 | 2025-03-14 |

### Top 10 Branches with Most File Changes

| Branch | Files Changed | Insertions | Deletions |
|--------|---------------|------------|-----------|
| metaagent | 2629 | +171843 | -221995 |
| gagb-mednav | 2626 | +165789 | -225714 |
| five-trace | 2624 | +165739 | -225714 |
| fix_fs | 2622 | +165404 | -225731 |
| fs-fix | 2622 | +165531 | -226086 |
| 0.2 | 2606 | +189281 | -211064 |
| o1-example | 2605 | +189158 | -211064 |
| update_old_site_for_04 | 2604 | +189234 | -211064 |
| wael/add-azure-dalle | 2603 | +188970 | -211064 |
| autogenstudio_agenteval | 2581 | +173335 | -219086 |

---

## Branch Details

Detailed information for each branch, sorted alphabetically.

### 0.2

**Last Commit:**
- Hash: `c631b34e`
- Author: Yogesh Chauhan
- Date: 2025-05-29 04:31:48 +0530
- Message: Fix Typo - Update JSON_mode_example.ipynb (#6457)

**Comparison with main:**
- Commits ahead: 1984
- Commits behind: 1

**Changes:**
- 2606 files changed, 189281 insertions(+), 211064 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2556 more files

---

### 1205-bug-tool-callings-fails-for-two-calls-in-the-same-message

**Last Commit:**
- Hash: `fba7caee`
- Author: Brian Finney
- Date: 2024-01-10 23:29:46 -0800
- Message: More async tool fixes (#1204)

**Comparison with main:**
- Commits ahead: 1138
- Commits behind: 1

**Changes:**
- 2171 files changed, 73665 insertions(+), 241161 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- ... and 2121 more files

---

### 1214-feature-request-unify-function-decorators-for-function-calling-reply-termination-and-hook-functions

**Last Commit:**
- Hash: `20ba7404`
- Author: Davor Runje
- Date: 2024-01-12 20:15:53 +0000
- Message: renaming

**Comparison with main:**
- Commits ahead: 1148
- Commits behind: 1

**Changes:**
- 2171 files changed, 74157 insertions(+), 241158 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- ... and 2121 more files

---

### 4367-fix-code-scanning-alert---websites-must-specify-the-httponly-attribute-on-sensitive-cookies

**Last Commit:**
- Hash: `bcd6e71e`
- Author: Eric Zhu
- Date: 2024-11-25 18:18:13 -0800
- Message: Fix assistant agent doc (#4365)

**Comparison with main:**
- Commits ahead: 2779
- Commits behind: 1

**Changes:**
- 1694 files changed, 41287 insertions(+), 168314 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/design/04 - Agent and Topic ID Specs.md`
- `docs/design/readme.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- ... and 1644 more files

---

### add-ruff-sort-rule

**Last Commit:**
- Hash: `87a0f6f1`
- Author: Davor Runje
- Date: 2024-03-28 13:09:28 +0000
- Message: run pre-commit on all files

**Comparison with main:**
- Commits ahead: 1459
- Commits behind: 1

**Changes:**
- 2434 files changed, 126195 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2384 more files

---

### add-ruff-sort-rule-incrementally

**Last Commit:**
- Hash: `e9258832`
- Author: Davor Runje
- Date: 2024-03-28 13:25:45 +0000
- Message: CI test

**Comparison with main:**
- Commits ahead: 1458
- Commits behind: 1

**Changes:**
- 2433 files changed, 125964 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2383 more files

---

### add-sort-imports-to-precommit

**Last Commit:**
- Hash: `8f4e2fc5`
- Author: Davor Runje
- Date: 2024-03-31 20:51:01 +0000
- Message: add ruff rule for sorting imports in pre-commit hook, but disable it in CI

**Comparison with main:**
- Commits ahead: 1474
- Commits behind: 1

**Changes:**
- 2443 files changed, 127445 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2393 more files

---

### add_stable

**Last Commit:**
- Hash: `44c33881`
- Author: Jack Gerrits
- Date: 2025-01-08 14:38:39 -0500
- Message: stable redirect

**Comparison with main:**
- Commits ahead: 2997
- Commits behind: 1

**Changes:**
- 1546 files changed, 35598 insertions(+), 144883 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1496 more files

---

### add_to_display

**Last Commit:**
- Hash: `0ed31f52`
- Author: Ryan Sweet
- Date: 2025-02-17 08:05:43 -0800
- Message: Merge branch 'main' into add_to_display

**Comparison with main:**
- Commits ahead: 3310
- Commits behind: 1

**Changes:**
- 898 files changed, 15131 insertions(+), 107743 deletions(-)

**Modified files:**

- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/README.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/samples/AgentChat/AutoGen.Basic.Sample/Example10_SemanticKernel.cs`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/Extension/KernelExtension.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelAgent.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- ... and 848 more files

---

### agenteval

**Last Commit:**
- Hash: `d8c837d1`
- Author: Beibin Li
- Date: 2024-02-22 09:22:13 -0800
- Message: Merge pull request #1755 from SeunRomiluyi/agenteval

**Comparison with main:**
- Commits ahead: 1297
- Commits behind: 1

**Changes:**
- 2265 files changed, 97520 insertions(+), 240408 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2215 more files

---

### agenteval_experiments

**Last Commit:**
- Hash: `1582927c`
- Author: Yiran Wu
- Date: 2024-06-23 16:19:37 -0700
- Message: Improve doc in tutorial/conversation-patterns and customized_speaker_selection (#3006)

**Comparison with main:**
- Commits ahead: 1730
- Commits behind: 1

**Changes:**
- 2567 files changed, 163798 insertions(+), 222921 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2517 more files

---

### agentprofiler

**Last Commit:**
- Hash: `8ee02f8e`
- Author: gagb
- Date: 2024-01-10 15:56:58 -0800
- Message: Merge branch 'main' into agentprofiler

**Comparison with main:**
- Commits ahead: 1163
- Commits behind: 1

**Changes:**
- 2178 files changed, 74499 insertions(+), 241161 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- ... and 2128 more files

---

### ags-readme

**Last Commit:**
- Hash: `47e3edc2`
- Author: Victor Dibia
- Date: 2025-01-13 06:47:46 -0800
- Message: Merge branch 'main' into ags-readme

**Comparison with main:**
- Commits ahead: 3032
- Commits behind: 1

**Changes:**
- 1531 files changed, 35253 insertions(+), 144248 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1481 more files

---

### ags_docs_update

**Last Commit:**
- Hash: `cb271977`
- Author: Victor Dibia
- Date: 2025-01-15 12:26:22 -0800
- Message: Merge branch 'main' into ags_docs_update

**Comparison with main:**
- Commits ahead: 3052
- Commits behind: 1

**Changes:**
- 1522 files changed, 35599 insertions(+), 141618 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1472 more files

---

### ags_minor_fixes

**Last Commit:**
- Hash: `f85ba02b`
- Author: Victor Dibia
- Date: 2025-01-17 11:07:29 -0800
- Message: remove uneeded logging info messages, add log level

**Comparison with main:**
- Commits ahead: 3062
- Commits behind: 1

**Changes:**
- 1526 files changed, 36063 insertions(+), 140710 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1476 more files

---

### ame

**Last Commit:**
- Hash: `10f22ee9`
- Author: Ricky Loynd
- Date: 2025-03-03 10:23:33 -0800
- Message: module path changes

**Comparison with main:**
- Commits ahead: 3182
- Commits behind: 1

**Changes:**
- 1330 files changed, 35459 insertions(+), 130288 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1280 more files

---

### anny-production

**Last Commit:**
- Hash: `05c441c6`
- Author: gagb
- Date: 2024-02-26 03:34:11 +0000
- Message: Improve command

**Comparison with main:**
- Commits ahead: 1299
- Commits behind: 1

**Changes:**
- 2260 files changed, 93545 insertions(+), 240411 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2210 more files

---

### anthropic-bedrock

**Last Commit:**
- Hash: `a6aa61c4`
- Author: HRUSHIKESH DOKALA
- Date: 2024-07-24 11:33:12 +0000
- Message: fix: deprecate the check for aws session token

**Comparison with main:**
- Commits ahead: 1787
- Commits behind: 1

**Changes:**
- 2574 files changed, 169267 insertions(+), 219649 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2524 more files

---

### anthropic-client

**Last Commit:**
- Hash: `b7c41bda`
- Author: Hk669
- Date: 2024-06-13 01:17:02 +0530
- Message: intial setup for anthropic client with pricing config

**Comparison with main:**
- Commits ahead: 1694
- Commits behind: 1

**Changes:**
- 2556 files changed, 156973 insertions(+), 223480 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2506 more files

---

### anthropic-fix

**Last Commit:**
- Hash: `361703d2`
- Author: Qingyun Wu
- Date: 2024-06-20 23:29:21 -0400
- Message: notebook

**Comparison with main:**
- Commits ahead: 1719
- Commits behind: 1

**Changes:**
- 2562 files changed, 160549 insertions(+), 222921 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2512 more files

---

### aprofile

**Last Commit:**
- Hash: `c955e858`
- Author: gagb
- Date: 2024-06-06 15:21:42 -0700
- Message: change default model

**Comparison with main:**
- Commits ahead: 1734
- Commits behind: 1

**Changes:**
- 2523 files changed, 139753 insertions(+), 241401 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2473 more files

---

### audio-capability

**Last Commit:**
- Hash: `74222366`
- Author: Wael Karkoub
- Date: 2024-04-04 03:25:49 +0100
- Message: Merge branch 'main' into audio-capability

**Comparison with main:**
- Commits ahead: 1512
- Commits behind: 1

**Changes:**
- 2463 files changed, 130584 insertions(+), 241399 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2413 more files

---

### autogenstudio

**Last Commit:**
- Hash: `5871bb59`
- Author: Victor Dibia
- Date: 2024-10-10 14:50:53 -0700
- Message: add support for video type

**Comparison with main:**
- Commits ahead: 1899
- Commits behind: 1

**Changes:**
- 2557 files changed, 174176 insertions(+), 211117 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2507 more files

---

### autogenstudio_agenteval

**Last Commit:**
- Hash: `0ab10dc1`
- Author: James Woffinden-Luey
- Date: 2024-07-31 08:25:01 -0700
- Message: fixing formatting buld break

**Comparison with main:**
- Commits ahead: 1847
- Commits behind: 1

**Changes:**
- 2581 files changed, 173335 insertions(+), 219086 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2531 more files

---

### autogenstudio_agents

**Last Commit:**
- Hash: `0291f24c`
- Author: KnucklesSG1
- Date: 2024-06-06 22:42:27 -0500
- Message: Fixed formatting.

**Comparison with main:**
- Commits ahead: 1631
- Commits behind: 1

**Changes:**
- 2525 files changed, 152576 insertions(+), 230464 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2475 more files

---

### BeibinLi-patch-1

**Last Commit:**
- Hash: `72e6e426`
- Author: Beibin Li
- Date: 2024-04-19 10:43:18 -0700
- Message: Merge branch 'main' into BeibinLi-patch-1

**Comparison with main:**
- Commits ahead: 1563
- Commits behind: 1

**Changes:**
- 2493 files changed, 140325 insertions(+), 241370 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2443 more files

---

### chat

**Last Commit:**
- Hash: `07520aa3`
- Author: Linxin Song
- Date: 2024-02-22 07:01:30 +0900
- Message: [AutoBuild] fix test error (#1750)

**Comparison with main:**
- Commits ahead: 1294
- Commits behind: 1

**Changes:**
- 2264 files changed, 97288 insertions(+), 240408 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2214 more files

---

### cleanup

**Last Commit:**
- Hash: `a3efd9ce`
- Author: Chi Wang
- Date: 2023-09-19 18:14:54 +0000
- Message: cleanup

**Comparison with main:**
- Commits ahead: 777
- Commits behind: 1

**Changes:**
- 1945 files changed, 27903 insertions(+), 242684 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- `autogen/agentchat/contrib/math_user_proxy_agent.py`
- `autogen/agentchat/contrib/retrieve_assistant_agent.py`
- `autogen/agentchat/contrib/retrieve_user_proxy_agent.py`
- ... and 1895 more files

---

### client_docs

**Last Commit:**
- Hash: `66b859b1`
- Author: Jack Gerrits
- Date: 2025-01-08 09:08:20 -0500
- Message: Merge branch 'main' into client_docs

**Comparison with main:**
- Commits ahead: 2989
- Commits behind: 1

**Changes:**
- 1547 files changed, 35442 insertions(+), 144670 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1497 more files

---

### coding-ekzhu

**Last Commit:**
- Hash: `5b8965e8`
- Author: Davor Runje
- Date: 2024-01-31 06:41:44 +0100
- Message: Merge remote-tracking branch 'origin/main' into coding-ekzhu

**Comparison with main:**
- Commits ahead: 1224
- Commits behind: 1

**Changes:**
- 2225 files changed, 83269 insertions(+), 240564 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2175 more files

---

### coding-review

**Last Commit:**
- Hash: `702bdd39`
- Author: Davor Runje
- Date: 2024-02-01 10:00:04 +0000
- Message: fixed failing tests

**Comparison with main:**
- Commits ahead: 1229
- Commits behind: 1

**Changes:**
- 2226 files changed, 83339 insertions(+), 240562 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2176 more files

---

### complex-chat

**Last Commit:**
- Hash: `2f8b06a9`
- Author: Qingyun Wu
- Date: 2024-02-13 22:24:17 -0500
- Message: chess

**Comparison with main:**
- Commits ahead: 1264
- Commits behind: 1

**Changes:**
- 2252 files changed, 92314 insertions(+), 240505 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2202 more files

---

### compression

**Last Commit:**
- Hash: `f64a0742`
- Author: Yiran Wu
- Date: 2023-10-21 17:20:34 -0400
- Message: Merge branch 'main' into compression

**Comparison with main:**
- Commits ahead: 918
- Commits behind: 1

**Changes:**
- 1966 files changed, 34372 insertions(+), 242612 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- `autogen/agentchat/contrib/__init__.py`
- `autogen/agentchat/contrib/compression_agent.py`
- ... and 1916 more files

---

### console_async_printing_and_optional_stats

**Last Commit:**
- Hash: `3b44d612`
- Author: Jack Gerrits
- Date: 2025-01-09 10:58:29 -0500
- Message: Make stats output option

**Comparison with main:**
- Commits ahead: 3001
- Commits behind: 1

**Changes:**
- 1539 files changed, 35600 insertions(+), 144600 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1489 more files

---

### control_stream

**Last Commit:**
- Hash: `4c8d1149`
- Author: Jack Gerrits
- Date: 2025-02-07 15:46:11 -0500
- Message: Abstract channel, add control channel

**Comparison with main:**
- Commits ahead: 3240
- Commits behind: 1

**Changes:**
- 1061 files changed, 16690 insertions(+), 120795 deletions(-)

**Modified files:**

- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/README.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/global.json`
- `dotnet/samples/AgentChat/AutoGen.Basic.Sample/Example10_SemanticKernel.cs`
- `dotnet/samples/AgentChat/AutoGen.OpenAI.Sample/Tool_Call_With_Ollama_And_LiteLLM.cs`
- `dotnet/samples/AgentChat/AutoGen.WebAPI.Sample/Program.cs`
- `dotnet/samples/Hello/HelloAgent/HelloAgent.cs`
- `dotnet/samples/Hello/HelloAgent/HelloAgent.csproj`
- `dotnet/samples/Hello/HelloAgent/Program.cs`
- `dotnet/src/AutoGen.Core/Extension/AgentExtension.cs`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- ... and 1011 more files

---

### copilot/fix-6210

**Last Commit:**
- Hash: `f3c714d3`
- Author: Jack Gerrits
- Date: 2025-05-19 17:03:19 -0400
- Message: Merge branch 'main' into copilot/fix-6210

**Comparison with main:**
- Commits ahead: 3633
- Commits behind: 1

**Changes:**
- 512 files changed, 7071 insertions(+), 45467 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `README.md`
- `docs/dotnet/core/index.md`
- `docs/switcher.json`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- `dotnet/test/AutoGen.Tests/Orchestrator/RolePlayOrchestratorTests.cs`
- `python/.gitignore`
- `python/README.md`
- `python/docs/README.md`
- `python/docs/src/generate_api_reference.py`
- `python/docs/src/images/assistant-agent.svg`
- `python/docs/src/user-guide/agentchat-user-guide/jaeger.png`
- `python/docs/src/user-guide/agentchat-user-guide/memory.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tracing.ipynb`
- `python/docs/src/user-guide/extensions-user-guide/azure-foundry-agent.ipynb`
- `python/packages/autogen-agentchat/pyproject.toml`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/__init__.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_assistant_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_base_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_code_executor_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_society_of_mind_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_task.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_team.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/messages.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat_manager.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_chat_agent_container.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_events.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_graph/_digraph_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_graph/_graph_builder.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_orchestrator.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_prompts.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_round_robin_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_selector_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_swarm_group_chat.py`
- ... and 462 more files

---

### copilot/fix-6542

**Last Commit:**
- Hash: `b3e4b44a`
- Author: Eric Zhu
- Date: 2025-05-21 20:30:48 -0700
- Message: Merge branch 'main' into copilot/fix-6542

**Comparison with main:**
- Commits ahead: 3655
- Commits behind: 1

**Changes:**
- 509 files changed, 6643 insertions(+), 45019 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `README.md`
- `docs/dotnet/core/index.md`
- `docs/switcher.json`
- `dotnet/dotnet-install.sh`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- `dotnet/test/AutoGen.Tests/Orchestrator/RolePlayOrchestratorTests.cs`
- `python/.gitignore`
- `python/README.md`
- `python/docs/README.md`
- `python/docs/src/generate_api_reference.py`
- `python/docs/src/images/assistant-agent.svg`
- `python/docs/src/user-guide/agentchat-user-guide/jaeger.png`
- `python/docs/src/user-guide/agentchat-user-guide/memory.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tracing.ipynb`
- `python/docs/src/user-guide/extensions-user-guide/azure-foundry-agent.ipynb`
- `python/packages/autogen-agentchat/pyproject.toml`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/__init__.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_assistant_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_base_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_code_executor_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_society_of_mind_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_task.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_team.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/messages.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat_manager.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_chat_agent_container.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_events.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_graph/_digraph_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_graph/_graph_builder.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_orchestrator.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_prompts.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_round_robin_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_selector_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_swarm_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/tools/_agent.py`
- ... and 459 more files

---

### copilot/generate-branch-modification-report

**Last Commit:**
- Hash: `11b801b9`
- Author: copilot-swe-agent[bot]
- Date: 2025-10-22 16:34:21 +0000
- Message: Initial plan

**Comparison with main:**
- Commits ahead: 1
- Commits behind: 0

**Changes:**
- No changes

---

### cost

**Last Commit:**
- Hash: `d71d04cc`
- Author: AutoGen-Hub
- Date: 2024-06-13 04:19:34 -0400
- Message: config list

**Comparison with main:**
- Commits ahead: 1698
- Commits behind: 1

**Changes:**
- 2556 files changed, 154393 insertions(+), 223481 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2506 more files

---

### costfix

**Last Commit:**
- Hash: `46c34bd2`
- Author: kevin666aa
- Date: 2024-07-19 12:21:48 -0400
- Message: update

**Comparison with main:**
- Commits ahead: 1758
- Commits behind: 1

**Changes:**
- 2580 files changed, 168305 insertions(+), 221994 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2530 more files

---

### ct_webarena-profiler

**Last Commit:**
- Hash: `19f5cc21`
- Author: Gagan Bansal
- Date: 2024-05-07 15:15:46 -0700
- Message: Improve layout

**Comparison with main:**
- Commits ahead: 1693
- Commits behind: 1

**Changes:**
- 2524 files changed, 139608 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2474 more files

---

### ct_webarena_learning

**Last Commit:**
- Hash: `e7f82e8e`
- Author: rickyloynd-microsoft
- Date: 2024-05-09 18:32:36 -0700
- Message: Function stubs

**Comparison with main:**
- Commits ahead: 1704
- Commits behind: 1

**Changes:**
- 2517 files changed, 138761 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2467 more files

---

### ct_webarena_may22

**Last Commit:**
- Hash: `2247ebbc`
- Author: Adam Fourney
- Date: 2024-05-29 13:51:57 -0700
- Message: Move the temperature adjustment to right before updaitng the ledger/plan.

**Comparison with main:**
- Commits ahead: 1711
- Commits behind: 1

**Changes:**
- 2516 files changed, 138817 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2466 more files

---

### custom_img

**Last Commit:**
- Hash: `53f07b8e`
- Author: gagb
- Date: 2024-03-14 07:10:19 +0000
- Message: Add a new devcontainer config

**Comparison with main:**
- Commits ahead: 1396
- Commits behind: 1

**Changes:**
- 2369 files changed, 113105 insertions(+), 239748 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/default-hosted/devcontainer.json`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- ... and 2319 more files

---

### declarative_agentchat_team_vd

**Last Commit:**
- Hash: `b598377d`
- Author: Victor Dibia
- Date: 2025-01-23 20:03:38 -0800
- Message: Merge remote-tracking branch 'origin/main' into declarative_agentchat_team_vd

**Comparison with main:**
- Commits ahead: 3095
- Commits behind: 1

**Changes:**
- 1524 files changed, 36810 insertions(+), 138012 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1474 more files

---

### dev/AGCore.Grpc

**Last Commit:**
- Hash: `ff2b4232`
- Author: Jacob Alber
- Date: 2025-01-30 02:02:32 -0500
- Message: wip: Implementing GrpcGateway

**Comparison with main:**
- Commits ahead: 3181
- Commits behind: 1

**Changes:**
- 1323 files changed, 35369 insertions(+), 129666 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1273 more files

---

### dev/agentchat_dotnet

**Last Commit:**
- Hash: `e1f7fe03`
- Author: Jacob Alber
- Date: 2025-02-13 12:16:10 -0500
- Message: WIP: Factor out RunManager to manage GroupChat lifecycle

**Comparison with main:**
- Commits ahead: 3287
- Commits behind: 1

**Changes:**
- 951 files changed, 15177 insertions(+), 109698 deletions(-)

**Modified files:**

- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/README.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/samples/AgentChat/AutoGen.Basic.Sample/Example10_SemanticKernel.cs`
- `dotnet/samples/Hello/HelloAgent/HelloAgent.csproj`
- `dotnet/samples/Hello/HelloAgent/Program.cs`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/Extension/KernelExtension.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelAgent.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- ... and 901 more files

---

### dev/agentchat_dotnet_agents

**Last Commit:**
- Hash: `5181f28c`
- Author: Ryan Sweet
- Date: 2025-03-06 16:33:51 -0800
- Message: Merge branch 'main' into dev/agentchat_dotnet_agents

**Comparison with main:**
- Commits ahead: 3397
- Commits behind: 1

**Changes:**
- 809 files changed, 15015 insertions(+), 87677 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/PromptTemplate.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Agents/AssistantAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Agents/CodeExecutorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Agents/CodingAssistantAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Agents/SocietyOfMindAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Agents/ToolManager.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Agents/UserProxyAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- ... and 759 more files

---

### dev/agentchat_dotnet_groupchat

**Last Commit:**
- Hash: `3b07b5a1`
- Author: Ryan Sweet
- Date: 2025-03-10 11:27:59 -0800
- Message: Merge branch 'main' into dev/agentchat_dotnet_groupchat

**Comparison with main:**
- Commits ahead: 3412
- Commits behind: 1

**Changes:**
- 789 files changed, 14029 insertions(+), 86601 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/PromptTemplate.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/SelectorGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/SwarmGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/TeamState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- ... and 739 more files

---

### dev/async_input

**Last Commit:**
- Hash: `7f0de678`
- Author: Jacob Alber
- Date: 2025-01-15 09:23:26 -0500
- Message: feat: Change async input strategy

**Comparison with main:**
- Commits ahead: 3045
- Commits behind: 1

**Changes:**
- 1523 files changed, 35636 insertions(+), 141686 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1473 more files

---

### dev/ESRPCodesign

**Last Commit:**
- Hash: `bcf0ccb6`
- Author: Jacob Alber
- Date: 2025-01-10 13:38:20 -0500
- Message: Merge branch 'main' into dev/ESRPCodesign

**Comparison with main:**
- Commits ahead: 3027
- Commits behind: 1

**Changes:**
- 1533 files changed, 35262 insertions(+), 144368 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1483 more files

---

### dev/fix_agent_registration_consistency

**Last Commit:**
- Hash: `c3547317`
- Author: Ryan Sweet
- Date: 2025-03-06 16:34:04 -0800
- Message: Merge branch 'main' into dev/fix_agent_registration_consistency

**Comparison with main:**
- Commits ahead: 3399
- Commits behind: 1

**Changes:**
- 803 files changed, 13826 insertions(+), 87707 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/TeamState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMentionTermination.cs`
- ... and 753 more files

---

### dev/grpc_dotnet_allup

**Last Commit:**
- Hash: `100e9e02`
- Author: Jacob Alber
- Date: 2025-01-31 09:45:34 -0500
- Message: feat: Enable Wildcard Subscriptions

**Comparison with main:**
- Commits ahead: 3185
- Commits behind: 1

**Changes:**
- 1322 files changed, 35276 insertions(+), 129605 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1272 more files

---

### disable_m1_stats

**Last Commit:**
- Hash: `fdf71855`
- Author: Eric Zhu
- Date: 2025-01-09 10:10:25 -0800
- Message: Merge branch 'main' into disable_m1_stats

**Comparison with main:**
- Commits ahead: 3003
- Commits behind: 1

**Changes:**
- 1537 files changed, 35344 insertions(+), 144495 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1487 more files

---

### disable_project_check

**Last Commit:**
- Hash: `46f2c5fc`
- Author: Jack Gerrits
- Date: 2025-01-08 09:34:30 -0500
- Message: Merge branch 'main' into disable_project_check

**Comparison with main:**
- Commits ahead: 2995
- Commits behind: 1

**Changes:**
- 1547 files changed, 35639 insertions(+), 144888 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1497 more files

---

### doc-polishing

**Last Commit:**
- Hash: `ced89ac0`
- Author: Jack Gerrits
- Date: 2025-01-08 09:25:06 -0500
- Message: Merge branch 'main' into doc-polishing

**Comparison with main:**
- Commits ahead: 2991
- Commits behind: 1

**Changes:**
- 1548 files changed, 35667 insertions(+), 144891 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1498 more files

---

### doc-update

**Last Commit:**
- Hash: `a084ca24`
- Author: Qingyun Wu
- Date: 2024-06-30 17:55:35 -0400
- Message: Update website/docusaurus.config.js

**Comparison with main:**
- Commits ahead: 1338
- Commits behind: 1

**Changes:**
- 2291 files changed, 102212 insertions(+), 239806 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2241 more files

---

### docs-fixes

**Last Commit:**
- Hash: `334cd4c0`
- Author: Eric Zhu
- Date: 2025-01-08 09:32:36 -0800
- Message: Fix agent and agent runtime in Core doc

**Comparison with main:**
- Commits ahead: 2991
- Commits behind: 1

**Changes:**
- 1547 files changed, 35640 insertions(+), 144888 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1497 more files

---

### docs-update-for-parallel-tool-calls

**Last Commit:**
- Hash: `da5b6635`
- Author: Eric Zhu
- Date: 2025-01-17 01:09:41 -0800
- Message: Merge branch 'main' into docs-update-for-parallel-tool-calls

**Comparison with main:**
- Commits ahead: 3060
- Commits behind: 1

**Changes:**
- 1526 files changed, 36112 insertions(+), 140741 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1476 more files

---

### dotnet

**Last Commit:**
- Hash: `e43c156c`
- Author: Bill Wilder
- Date: 2024-10-06 01:14:21 -0400
- Message: Fix spelling of "dotnet" (#3669)

**Comparison with main:**
- Commits ahead: 1825
- Commits behind: 1

**Changes:**
- 2505 files changed, 147075 insertions(+), 231616 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2455 more files

---

### dotnet-pre-python-alignment

**Last Commit:**
- Hash: `8687eec5`
- Author: Ryan Sweet
- Date: 2025-01-31 07:50:27 -0800
- Message: interim

**Comparison with main:**
- Commits ahead: 3164
- Commits behind: 1

**Changes:**
- 1439 files changed, 35975 insertions(+), 131423 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1389 more files

---

### ekzhu-fix-website

**Last Commit:**
- Hash: `72833f09`
- Author: Eric Zhu
- Date: 2025-03-12 01:07:27 -0700
- Message: Fix website cards

**Comparison with main:**
- Commits ahead: 3416
- Commits behind: 1

**Changes:**
- 763 files changed, 13514 insertions(+), 84522 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMentionTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TimeoutTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TokenUsageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/Agents/AIAgent/InferenceAgent.cs`
- `dotnet/src/Microsoft.AutoGen/Core/InProcessRuntime.cs`
- `dotnet/src/Microsoft.AutoGen/Core/MessageDelivery.cs`
- `dotnet/src/Microsoft.AutoGen/Core/ResultSink.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcGateway.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcGatewayService.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcWorkerConnection.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- ... and 713 more files

---

### ekzhu-log-tools

**Last Commit:**
- Hash: `c9a89ae4`
- Author: Eric Zhu
- Date: 2025-03-06 15:25:06 -0800
- Message: fix

**Comparison with main:**
- Commits ahead: 3394
- Commits behind: 1

**Changes:**
- 801 files changed, 13753 insertions(+), 88098 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RunContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/TeamState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- ... and 751 more files

---

### ekzhu-nested-team

**Last Commit:**
- Hash: `a5bb0526`
- Author: Eric Zhu
- Date: 2025-03-06 19:09:05 -0800
- Message: Nested teams in group chats

**Comparison with main:**
- Commits ahead: 3394
- Commits behind: 1

**Changes:**
- 801 files changed, 13689 insertions(+), 87597 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/TeamState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMentionTermination.cs`
- ... and 751 more files

---

### ekzhu-optional-thought-as-content

**Last Commit:**
- Hash: `7c4f8d11`
- Author: Eric Zhu
- Date: 2025-05-12 21:51:53 -0700
- Message: Add option for openai client to avoid setting reasoning tokens as assistant message content when sending to the model api.

**Comparison with main:**
- Commits ahead: 3621
- Commits behind: 1

**Changes:**
- 518 files changed, 9251 insertions(+), 47621 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `README.md`
- `docs/dotnet/core/index.md`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- `dotnet/test/AutoGen.Tests/Orchestrator/RolePlayOrchestratorTests.cs`
- `python/.gitignore`
- `python/README.md`
- `python/docs/README.md`
- `python/docs/src/generate_api_reference.py`
- `python/docs/src/images/assistant-agent.svg`
- `python/docs/src/user-guide/agentchat-user-guide/jaeger.png`
- `python/docs/src/user-guide/agentchat-user-guide/memory.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tracing.ipynb`
- `python/docs/src/user-guide/extensions-user-guide/azure-foundry-agent.ipynb`
- `python/packages/autogen-agentchat/pyproject.toml`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/__init__.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_assistant_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_base_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_code_executor_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_society_of_mind_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_task.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_team.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/messages.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat_manager.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_chat_agent_container.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_events.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_graph/_digraph_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_graph/_graph_builder.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_orchestrator.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_prompts.py`
- ... and 468 more files

---

### ekzhu-otel

**Last Commit:**
- Hash: `5b63e649`
- Author: Eric Zhu
- Date: 2025-05-06 16:23:45 -0700
- Message: Add message attributes to otel traces

**Comparison with main:**
- Commits ahead: 3609
- Commits behind: 1

**Changes:**
- 531 files changed, 9380 insertions(+), 48564 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `README.md`
- `docs/dotnet/core/index.md`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- `dotnet/test/AutoGen.Tests/Orchestrator/RolePlayOrchestratorTests.cs`
- `python/.gitignore`
- `python/README.md`
- `python/docs/README.md`
- `python/docs/src/generate_api_reference.py`
- `python/docs/src/images/assistant-agent.svg`
- `python/docs/src/user-guide/agentchat-user-guide/jaeger.png`
- `python/docs/src/user-guide/agentchat-user-guide/memory.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tracing.ipynb`
- `python/docs/src/user-guide/extensions-user-guide/azure-foundry-agent.ipynb`
- `python/packages/autogen-agentchat/pyproject.toml`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/__init__.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_assistant_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_base_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_code_executor_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_society_of_mind_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_task.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_team.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/messages.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat_manager.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_chat_agent_container.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_events.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_graph/_digraph_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_graph/_graph_builder.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_group_chat.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_orchestrator.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_prompts.py`
- ... and 481 more files

---

### ekzhu-otel-span-wip

**Last Commit:**
- Hash: `8897bf3b`
- Author: Eric Zhu
- Date: 2025-03-07 19:03:59 -0800
- Message: wip

**Comparison with main:**
- Commits ahead: 3407
- Commits behind: 1

**Changes:**
- 787 files changed, 13539 insertions(+), 86696 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/TeamState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMentionTermination.cs`
- ... and 737 more files

---

### ekzhu-stream-group-message

**Last Commit:**
- Hash: `b9d70127`
- Author: Eric Zhu
- Date: 2025-04-16 14:27:57 -0700
- Message: Merge branch 'main' into ekzhu-stream-group-message

**Comparison with main:**
- Commits ahead: 3551
- Commits behind: 1

**Changes:**
- 583 files changed, 9140 insertions(+), 61433 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `README.md`
- `docs/dotnet/core/index.md`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- `dotnet/test/AutoGen.Tests/Orchestrator/RolePlayOrchestratorTests.cs`
- `python/.gitignore`
- `python/README.md`
- `python/docs/README.md`
- `python/docs/src/generate_api_reference.py`
- `python/docs/src/images/assistant-agent.svg`
- `python/docs/src/user-guide/agentchat-user-guide/graph-flow.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/jaeger.png`
- `python/docs/src/user-guide/agentchat-user-guide/memory.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tracing.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tutorial/agents.ipynb`
- `python/docs/src/user-guide/core-user-guide/components/workbench.ipynb`
- `python/docs/src/user-guide/core-user-guide/cookbook/data/nifty_500_quarterly_results.csv`
- `python/docs/src/user-guide/extensions-user-guide/azure-foundry-agent.ipynb`
- `python/packages/agbench/benchmarks/GAIA/Templates/ParallelAgents/expected_answer.txt`
- `python/packages/agbench/benchmarks/GAIA/Templates/ParallelAgents/prompt.txt`
- `python/packages/agbench/benchmarks/GAIA/Templates/ParallelAgents/requirements.txt`
- `python/packages/agbench/benchmarks/GAIA/Templates/ParallelAgents/scenario.py`
- `python/packages/autogen-agentchat/pyproject.toml`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/__init__.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_assistant_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_base_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_code_executor_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_message_filter_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_society_of_mind_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_task.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_team.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/conditions/__init__.py`
- ... and 533 more files

---

### enrich_ecosystem_style

**Last Commit:**
- Hash: `ba5a07a9`
- Author: Shaokun Zhang
- Date: 2023-11-30 13:31:08 -0500
- Message: Add ecosystem page for website (#803)

**Comparison with main:**
- Commits ahead: 1016
- Commits behind: 1

**Changes:**
- 2087 files changed, 51578 insertions(+), 241792 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-lmm.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- ... and 2037 more files

---

### examples

**Last Commit:**
- Hash: `871a34ec`
- Author: Qingyun Wu
- Date: 2024-03-12 11:02:51 -0400
- Message: add notebook to topics

**Comparison with main:**
- Commits ahead: 1382
- Commits behind: 1

**Changes:**
- 2322 files changed, 114093 insertions(+), 239806 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2272 more files

---

### ext-refactor

**Last Commit:**
- Hash: `b0f0bdce`
- Author: Leonardo Pinheiro
- Date: 2024-12-04 09:09:31 +1000
- Message: Merge branch 'main' into ext-refactor

**Comparison with main:**
- Commits ahead: 2825
- Commits behind: 1

**Changes:**
- 1675 files changed, 40102 insertions(+), 164787 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1625 more files

---

### ext_link

**Last Commit:**
- Hash: `84007e3f`
- Author: Jack Gerrits
- Date: 2025-01-07 13:31:30 -0500
- Message: Merge branch 'main' into ext_link

**Comparison with main:**
- Commits ahead: 2980
- Commits behind: 1

**Changes:**
- 1580 files changed, 36361 insertions(+), 144939 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1530 more files

---

### feature/autogenstudio-ui-extra-headers

**Last Commit:**
- Hash: `399ca090`
- Author: Ronald Pereira
- Date: 2024-07-01 12:22:29 -0300
- Message: Merge branch 'main' into feature/autogenstudio-ui-extra-headers

**Comparison with main:**
- Commits ahead: 1763
- Commits behind: 1

**Changes:**
- 2571 files changed, 164717 insertions(+), 221783 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2521 more files

---

### feature/azure-ai-inference-client

**Last Commit:**
- Hash: `9d33c7cf`
- Author: Leonardo Pinheiro
- Date: 2025-01-20 14:28:56 +1000
- Message: lint

**Comparison with main:**
- Commits ahead: 3078
- Commits behind: 1

**Changes:**
- 1528 files changed, 36829 insertions(+), 138703 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1478 more files

---

### five-trace

**Last Commit:**
- Hash: `d00c96ac`
- Author: Eduardo Salinas
- Date: 2024-06-24 14:57:20 -0400
- Message: add tracing to five-agents scenario.py

**Comparison with main:**
- Commits ahead: 1981
- Commits behind: 1

**Changes:**
- 2624 files changed, 165739 insertions(+), 225714 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2574 more files

---

### fix-async-reply

**Last Commit:**
- Hash: `98bef250`
- Author: Davor Runje
- Date: 2024-01-10 10:05:57 +0000
- Message: documentation update and added tests for register_reply function

**Comparison with main:**
- Commits ahead: 1131
- Commits behind: 1

**Changes:**
- 2171 files changed, 73358 insertions(+), 241161 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- ... and 2121 more files

---

### fix-check_can_use_docker_or_throw

**Last Commit:**
- Hash: `536a28ab`
- Author: Davor Runje
- Date: 2024-01-25 06:37:59 +0000
- Message: fix check_can_use_docker_or_throw

**Comparison with main:**
- Commits ahead: 1186
- Commits behind: 1

**Changes:**
- 2201 files changed, 80659 insertions(+), 241121 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2151 more files

---

### fix-contribtest

**Last Commit:**
- Hash: `4be8fe3a`
- Author: Hk669
- Date: 2024-04-19 23:48:45 +0530
- Message: bump: contrib-tests

**Comparison with main:**
- Commits ahead: 1565
- Commits behind: 1

**Changes:**
- 2493 files changed, 140338 insertions(+), 241370 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2443 more files

---

### fix-lfs-file

**Last Commit:**
- Hash: `3e4a7ea7`
- Author: Davor Runje
- Date: 2024-03-12 14:43:07 +0000
- Message: add file with LFS installed

**Comparison with main:**
- Commits ahead: 1375
- Commits behind: 1

**Changes:**
- 2317 files changed, 108397 insertions(+), 239806 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2267 more files

---

### fix-tests-custom-client

**Last Commit:**
- Hash: `7c68924e`
- Author: Davor Runje
- Date: 2024-02-01 09:27:13 +0000
- Message: added new protocol for gpt assistants support in custom client and fixed failing tests

**Comparison with main:**
- Commits ahead: 1253
- Commits behind: 1

**Changes:**
- 2220 files changed, 84328 insertions(+), 240561 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2170 more files

---

### fix669

**Last Commit:**
- Hash: `ba4c37f8`
- Author: Li Jiang
- Date: 2024-04-27 22:19:55 +0800
- Message: Merge branch 'main' into fix669

**Comparison with main:**
- Commits ahead: 1576
- Commits behind: 1

**Changes:**
- 2507 files changed, 147414 insertions(+), 231615 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2457 more files

---

### fix_ci

**Last Commit:**
- Hash: `337bbb63`
- Author: afourney
- Date: 2025-01-09 10:48:53 -0800
- Message: Merge branch 'main' into fix_ci

**Comparison with main:**
- Commits ahead: 3006
- Commits behind: 1

**Changes:**
- 1534 files changed, 35318 insertions(+), 144480 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1484 more files

---

### fix_fs

**Last Commit:**
- Hash: `e782ccfb`
- Author: gagb
- Date: 2024-06-13 13:16:07 -0700
- Message: Fix argument parsing and validation

**Comparison with main:**
- Commits ahead: 1969
- Commits behind: 1

**Changes:**
- 2622 files changed, 165404 insertions(+), 225731 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2572 more files

---

### fixcompress

**Last Commit:**
- Hash: `93b2ead8`
- Author: kevin666aa
- Date: 2023-12-28 13:16:21 -0500
- Message: Merge remote-tracking branch 'origin/main' into fixcompress

**Comparison with main:**
- Commits ahead: 1094
- Commits behind: 1

**Changes:**
- 2158 files changed, 65282 insertions(+), 241268 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- ... and 2108 more files

---

### fixcreate

**Last Commit:**
- Hash: `ca02914f`
- Author: kevin666aa
- Date: 2023-12-04 00:35:15 -0500
- Message: update

**Comparison with main:**
- Commits ahead: 1040
- Commits behind: 1

**Changes:**
- 2105 files changed, 56458 insertions(+), 241536 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- ... and 2055 more files

---

### flatten_core_base

**Last Commit:**
- Hash: `94c5c9b3`
- Author: Jack Gerrits
- Date: 2024-12-03 16:55:13 -0800
- Message: fmt

**Comparison with main:**
- Commits ahead: 2828
- Commits behind: 1

**Changes:**
- 1668 files changed, 39404 insertions(+), 163726 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1618 more files

---

### flip_hil

**Last Commit:**
- Hash: `bd937ae4`
- Author: Adam Fourney
- Date: 2025-01-09 16:39:30 -0800
- Message: Added uv.lock

**Comparison with main:**
- Commits ahead: 3022
- Commits behind: 1

**Changes:**
- 1534 files changed, 35267 insertions(+), 144397 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1484 more files

---

### fs-fix

**Last Commit:**
- Hash: `0f4b9364`
- Author: Gagan Bansal
- Date: 2024-06-11 00:47:22 -0700
- Message: Add temp fix

**Comparison with main:**
- Commits ahead: 1957
- Commits behind: 1

**Changes:**
- 2622 files changed, 165531 insertions(+), 226086 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2572 more files

---

### gagb-experimental-async

**Last Commit:**
- Hash: `b39b13d4`
- Author: Gagan Bansal
- Date: 2024-04-22 21:42:32 -0700
- Message: Update readme

**Comparison with main:**
- Commits ahead: 1578
- Commits behind: 1

**Changes:**
- 2520 files changed, 135171 insertions(+), 241391 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2470 more files

---

### gagb-fix-5212

**Last Commit:**
- Hash: `a7ee98b9`
- Author: gagb
- Date: 2025-01-26 22:26:52 -0800
- Message: Run poe check

**Comparison with main:**
- Commits ahead: 3100
- Commits behind: 1

**Changes:**
- 1472 files changed, 37688 insertions(+), 133650 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1422 more files

---

### gagb-m1

**Last Commit:**
- Hash: `43a38083`
- Author: gagb
- Date: 2024-12-25 17:51:11 -0800
- Message: Refactor RichConsole to streamline image handling and remove redundant output logic

**Comparison with main:**
- Commits ahead: 2930
- Commits behind: 1

**Changes:**
- 1624 files changed, 39025 insertions(+), 149257 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1574 more files

---

### gagb-mednav

**Last Commit:**
- Hash: `e8e1a114`
- Author: Gagan Bansal
- Date: 2024-07-15 13:23:29 -0700
- Message: Add code

**Comparison with main:**
- Commits ahead: 1984
- Commits behind: 1

**Changes:**
- 2626 files changed, 165789 insertions(+), 225714 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2576 more files

---

### gagb-readme

**Last Commit:**
- Hash: `dcfc3c64`
- Author: Jack Gerrits
- Date: 2025-01-09 12:56:00 -0500
- Message: Merge branch 'main' into gagb-readme

**Comparison with main:**
- Commits ahead: 3043
- Commits behind: 1

**Changes:**
- 1537 files changed, 35344 insertions(+), 144495 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1487 more files

---

### gagb-whisper

**Last Commit:**
- Hash: `8f8357ea`
- Author: gagb
- Date: 2024-03-21 19:08:48 -0700
- Message: Update

**Comparison with main:**
- Commits ahead: 1442
- Commits behind: 1

**Changes:**
- 2411 files changed, 121224 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2361 more files

---

### gagb/qualcoder

**Last Commit:**
- Hash: `d563ba0a`
- Author: gagb
- Date: 2025-03-26 11:45:18 -0700
- Message: Run poe fmt

**Comparison with main:**
- Commits ahead: 3501
- Commits behind: 1

**Changes:**
- 669 files changed, 11266 insertions(+), 75412 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/Agents/AIAgent/InferenceAgent.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- `dotnet/test/AutoGen.OpenAI.Tests/ApprovalTests/OpenAIMessageTests.BasicMessageTest.approved.txt`
- `dotnet/test/AutoGen.OpenAI.Tests/ApprovalTests/OpenAIMessageTests.BasicMessageTest.received.txt`
- `dotnet/test/AutoGen.Tests/Function/FunctionTests.cs`
- `dotnet/test/AutoGen.Tests/Orchestrator/RolePlayOrchestratorTests.cs`
- `dotnet/test/AutoGen.Tests/SingleAgentTest.cs`
- `dotnet/test/AutoGen.Tests/TwoAgentTest.cs`
- `python/.gitignore`
- `python/README.md`
- `python/docs/README.md`
- `python/docs/src/generate_api_reference.py`
- `python/docs/src/images/assistant-agent.svg`
- `python/docs/src/user-guide/agentchat-user-guide/custom-agents.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/graph-flow.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/jaeger.png`
- `python/docs/src/user-guide/agentchat-user-guide/memory.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/selector-group-chat.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tracing.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tutorial/agents.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tutorial/messages.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tutorial/state.ipynb`
- ... and 619 more files

---

### gaia_multiagent_v01_march_1st

**Last Commit:**
- Hash: `63a01753`
- Author: Adam Fourney
- Date: 2024-03-01 13:53:48 -0800
- Message: Added a link to AutoGenBench

**Comparison with main:**
- Commits ahead: 1393
- Commits behind: 1

**Changes:**
- 2294 files changed, 97683 insertions(+), 239810 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2244 more files

---

### garnermccloud

**Last Commit:**
- Hash: `a93cfff6`
- Author: Hk669
- Date: 2024-06-21 10:40:21 +0530
- Message: fix naming convention

**Comparison with main:**
- Commits ahead: 1726
- Commits behind: 1

**Changes:**
- 2562 files changed, 160442 insertions(+), 222921 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2512 more files

---

### gh-readonly-queue/main/pr-4958-8c4c9f0776700a55cb9218fa1412bd7563d22f91

**Last Commit:**
- Hash: `cc5f9690`
- Author: SeryioGonzalez
- Date: 2025-01-09 21:17:47 +0100
- Message: Update swarm.ipynb (#4958)

**Comparison with main:**
- Commits ahead: 3011
- Commits behind: 1

**Changes:**
- 1534 files changed, 35283 insertions(+), 144437 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1484 more files

---

### gh-readonly-queue/main/pr-4959-7ed1d92a501463fb79b711554cd32aaeb801e40b

**Last Commit:**
- Hash: `8c4c9f07`
- Author: SeryioGonzalez
- Date: 2025-01-09 21:16:50 +0100
- Message: Update swarm.ipynb (#4959)

**Comparison with main:**
- Commits ahead: 3010
- Commits behind: 1

**Changes:**
- 1534 files changed, 35284 insertions(+), 144438 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1484 more files

---

### gh-readonly-queue/main/pr-4970-0122d44aa33977b2c9c1d47e5de9fc23fe41395a

**Last Commit:**
- Hash: `7ed1d92a`
- Author: Jack Gerrits
- Date: 2025-01-09 15:16:10 -0500
- Message: Fixes for azure-container-code-executor.ipynb (#4970)

**Comparison with main:**
- Commits ahead: 3009
- Commits behind: 1

**Changes:**
- 1534 files changed, 35285 insertions(+), 144439 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1484 more files

---

### gpt-assistant-improving

**Last Commit:**
- Hash: `f84ec741`
- Author: IANTHEREAL
- Date: 2023-12-13 16:08:03 +0800
- Message: improving log

**Comparison with main:**
- Commits ahead: 1065
- Commits behind: 1

**Changes:**
- 2120 files changed, 58439 insertions(+), 241535 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- ... and 2070 more files

---

### groupcompress

**Last Commit:**
- Hash: `b472c322`
- Author: kevin666aa
- Date: 2023-12-27 18:27:32 -0500
- Message: Merge remote-tracking branch 'origin/main' into groupcompress

**Comparison with main:**
- Commits ahead: 1195
- Commits behind: 1

**Changes:**
- 2161 files changed, 65824 insertions(+), 241268 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- ... and 2111 more files

---

### homepage-fix

**Last Commit:**
- Hash: `854153d0`
- Author: Eric Zhu
- Date: 2025-01-08 10:43:17 -0800
- Message: Update links

**Comparison with main:**
- Commits ahead: 2997
- Commits behind: 1

**Changes:**
- 1546 files changed, 35598 insertions(+), 144884 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1496 more files

---

### husseinmozannar-patch-1

**Last Commit:**
- Hash: `ae10a5a1`
- Author: Hussein Mozannar
- Date: 2024-11-14 21:33:01 -0800
- Message: Update README.md

**Comparison with main:**
- Commits ahead: 2710
- Commits behind: 1

**Changes:**
- 1716 files changed, 40940 insertions(+), 172514 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/design/03 - Agent Worker Protocol.md`
- `docs/design/04 - Agent and Topic ID Specs.md`
- `docs/design/readme.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- ... and 1666 more files

---

### i1960

**Last Commit:**
- Hash: `90fb2c87`
- Author: Davor Runje
- Date: 2024-03-12 14:49:14 +0000
- Message: limit version of numpy and fix LFS file

**Comparison with main:**
- Commits ahead: 1375
- Commits behind: 1

**Changes:**
- 2317 files changed, 108399 insertions(+), 239806 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2267 more files

---

### improv-lang

**Last Commit:**
- Hash: `6d66fe69`
- Author: Eric Zhu
- Date: 2025-01-07 10:50:52 -0800
- Message: Improve language for teams note

**Comparison with main:**
- Commits ahead: 2979
- Commits behind: 1

**Changes:**
- 1580 files changed, 36361 insertions(+), 144939 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1530 more files

---

### initiate_chat_updates

**Last Commit:**
- Hash: `0c5aed04`
- Author: Shaokun Zhang
- Date: 2024-04-16 01:07:58 -0400
- Message: add AgentOptimizer test in CI (#2380)

**Comparison with main:**
- Commits ahead: 1541
- Commits behind: 1

**Changes:**
- 2470 files changed, 132351 insertions(+), 241391 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2420 more files

---

### initiate_chats_update

**Last Commit:**
- Hash: `88f1a588`
- Author: ShobhitVishnoi30
- Date: 2024-06-18 11:38:30 +0530
- Message: added finished_chat_indexes_to_exclude_from_carryover in a_initiate_chats

**Comparison with main:**
- Commits ahead: 1549
- Commits behind: 1

**Changes:**
- 2475 files changed, 135466 insertions(+), 241387 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2425 more files

---

### integ-test

**Last Commit:**
- Hash: `f8630c43`
- Author: Ryan Sweet
- Date: 2024-12-10 09:32:16 -0800
- Message: Merge branch 'main' into integ-test

**Comparison with main:**
- Commits ahead: 2867
- Commits behind: 1

**Changes:**
- 1645 files changed, 37032 insertions(+), 156770 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1595 more files

---

### isort-imports

**Last Commit:**
- Hash: `13ce8bc9`
- Author: Davor Runje
- Date: 2024-03-26 08:02:00 +0000
- Message: add isort to pre-commit

**Comparison with main:**
- Commits ahead: 1448
- Commits behind: 1

**Changes:**
- 2417 files changed, 123496 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2367 more files

---

### jluey/agenteval_onstudio

**Last Commit:**
- Hash: `ca66289a`
- Author: James Woffinden-Luey
- Date: 2024-09-26 11:52:59 -0700
- Message: fixing precommit issues

**Comparison with main:**
- Commits ahead: 1898
- Commits behind: 1

**Changes:**
- 2560 files changed, 175546 insertions(+), 211117 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2510 more files

---

### kostapetan/fix-runtime-broadcast

**Last Commit:**
- Hash: `1cbe9e4c`
- Author: Ryan Sweet
- Date: 2024-12-02 18:35:00 -0800
- Message: Merge branch 'main' into kostapetan/fix-runtime-broadcast

**Comparison with main:**
- Commits ahead: 2812
- Commits behind: 1

**Changes:**
- 1680 files changed, 39874 insertions(+), 165564 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- ... and 1630 more files

---

### kostapetan/hello-distributed

**Last Commit:**
- Hash: `d2497d14`
- Author: Kosta Petan
- Date: 2024-11-28 15:36:00 +0100
- Message: fix runtime broadcasting

**Comparison with main:**
- Commits ahead: 2808
- Commits behind: 1

**Changes:**
- 1698 files changed, 40046 insertions(+), 166088 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- ... and 1648 more files

---

### kostapetan/marketing-sample

**Last Commit:**
- Hash: `df0ab60d`
- Author: Jennifer Marsman
- Date: 2024-12-04 11:23:36 -0500
- Message: Prompt tweaks to fix some spelling and grammar errors (#4542)

**Comparison with main:**
- Commits ahead: 2671
- Commits behind: 1

**Changes:**
- 1831 files changed, 49064 insertions(+), 177692 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/design/03 - worker-protocol.md`
- `docs/design/04 - Agent and Topic ID Specs.md`
- `docs/design/05 - Services.md`
- `docs/design/readme.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- ... and 1781 more files

---

### kostapetan/refactor-dotnet

**Last Commit:**
- Hash: `4084193b`
- Author: Kosta Petan
- Date: 2024-12-19 15:42:09 +0100
- Message: samples work

**Comparison with main:**
- Commits ahead: 2904
- Commits behind: 1

**Changes:**
- 1642 files changed, 36931 insertions(+), 156193 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1592 more files

---

### landing-page

**Last Commit:**
- Hash: `22012fea`
- Author: Eric Zhu
- Date: 2025-01-09 11:11:12 -0800
- Message: update landing page example

**Comparison with main:**
- Commits ahead: 3007
- Commits behind: 1

**Changes:**
- 1534 files changed, 35313 insertions(+), 144470 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1484 more files

---

### li/rag_temp

**Last Commit:**
- Hash: `d21aaf46`
- Author: Li Jiang
- Date: 2024-03-02 07:58:05 +0800
- Message: Merge branch 'main' into new_rag

**Comparison with main:**
- Commits ahead: 1385
- Commits behind: 1

**Changes:**
- 2311 files changed, 106871 insertions(+), 239805 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2261 more files

---

### linguist_overrides

**Last Commit:**
- Hash: `f6c1e763`
- Author: Jack Gerrits
- Date: 2025-01-08 18:27:52 -0500
- Message: Merge branch 'main' into linguist_overrides

**Comparison with main:**
- Commits ahead: 3001
- Commits behind: 1

**Changes:**
- 1539 files changed, 35620 insertions(+), 144623 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1489 more files

---

### litellmclient

**Last Commit:**
- Hash: `07f2cda7`
- Author: Mark Sze
- Date: 2024-07-01 04:12:58 +0000
- Message: Streaming and manual tool calling refinements, tidy up.

**Comparison with main:**
- Commits ahead: 1744
- Commits behind: 1

**Changes:**
- 2574 files changed, 165361 insertions(+), 222586 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2524 more files

---

### llm_config_enhancements

**Last Commit:**
- Hash: `ae3370db`
- Author: Umer Mansoor
- Date: 2024-08-12 12:49:42 -0700
- Message: Merge branch 'main' into llm_config_enhancements

**Comparison with main:**
- Commits ahead: 1830
- Commits behind: 1

**Changes:**
- 2562 files changed, 170597 insertions(+), 216012 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2512 more files

---

### m1_debug_vd

**Last Commit:**
- Hash: `dcf57f56`
- Author: Victor Dibia
- Date: 2025-01-09 14:55:13 -0800
- Message: format fixes

**Comparison with main:**
- Commits ahead: 3019
- Commits behind: 1

**Changes:**
- 1534 files changed, 35265 insertions(+), 144410 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1484 more files

---

### m1_package

**Last Commit:**
- Hash: `48e0a2ed`
- Author: Adam Fourney
- Date: 2025-01-08 13:52:04 -0800
- Message: Suppress 'ResourceWarning: unclosed socket'

**Comparison with main:**
- Commits ahead: 3002
- Commits behind: 1

**Changes:**
- 1540 files changed, 35583 insertions(+), 144792 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1490 more files

---

### m1_singleton_team

**Last Commit:**
- Hash: `2eb5a317`
- Author: afourney
- Date: 2025-01-16 12:26:36 -0800
- Message: Merge branch 'main' into m1_singleton_team

**Comparison with main:**
- Commits ahead: 3056
- Commits behind: 1

**Changes:**
- 1526 files changed, 35813 insertions(+), 141594 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1476 more files

---

### magentic-one-viz

**Last Commit:**
- Hash: `4023454c`
- Author: Mohammad Mazraeh
- Date: 2024-10-31 11:54:24 +0000
- Message: add simple chainlit integration (#3999)

**Comparison with main:**
- Commits ahead: 2650
- Commits behind: 1

**Changes:**
- 1757 files changed, 45547 insertions(+), 178648 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/design/03 - worker-protocol.md`
- `docs/design/04 - Agent and Topic ID Specs.md`
- `docs/design/05 - Services.md`
- `docs/design/readme.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- ... and 1707 more files

---

### main

**Last Commit:**
- Hash: `13e144e5`
- Author: 4shen0ne
- Date: 2025-10-04 09:06:04 +0800
- Message: fix: order by clause (#7051)

**Comparison with main:**
- Commits ahead: 0
- Commits behind: 0

**Changes:**
- No changes

---

### mathtest

**Last Commit:**
- Hash: `97355371`
- Author: kevin666aa
- Date: 2023-11-11 13:23:11 -0500
- Message: Merge remote-tracking branch 'origin/main' into mathtest

**Comparison with main:**
- Commits ahead: 971
- Commits behind: 1

**Changes:**
- 2004 files changed, 42622 insertions(+), 242611 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-lmm.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- ... and 1954 more files

---

### mem

**Last Commit:**
- Hash: `9ba21ec7`
- Author: Ricky Loynd
- Date: 2025-05-21 14:19:14 -0700
- Message: AIME 2025 tasks

**Comparison with main:**
- Commits ahead: 3586
- Commits behind: 1

**Changes:**
- 705 files changed, 17865 insertions(+), 58838 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `README.md`
- `docs/dotnet/core/index.md`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- `dotnet/test/AutoGen.Tests/Orchestrator/RolePlayOrchestratorTests.cs`
- `python/.gitignore`
- `python/README.md`
- `python/docs/README.md`
- `python/docs/src/generate_api_reference.py`
- `python/docs/src/images/assistant-agent.svg`
- `python/docs/src/user-guide/agentchat-user-guide/graph-flow.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/jaeger.png`
- `python/docs/src/user-guide/agentchat-user-guide/memory.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tracing.ipynb`
- `python/docs/src/user-guide/agentchat-user-guide/tutorial/agents.ipynb`
- `python/docs/src/user-guide/core-user-guide/components/workbench.ipynb`
- `python/docs/src/user-guide/core-user-guide/cookbook/data/nifty_500_quarterly_results.csv`
- `python/docs/src/user-guide/extensions-user-guide/azure-foundry-agent.ipynb`
- `python/packages/autogen-agentchat/pyproject.toml`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/__init__.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_assistant_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_base_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_code_executor_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_message_filter_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/agents/_society_of_mind_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_chat_agent.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_task.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/base/_team.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/conditions/__init__.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/conditions/_terminations.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/messages.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/__init__.py`
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat.py`
- ... and 655 more files

---

### metaagent

**Last Commit:**
- Hash: `194f8d49`
- Author: LeoLjl
- Date: 2024-07-13 16:52:16 +0000
- Message: Update notebook

**Comparison with main:**
- Commits ahead: 1779
- Commits behind: 1

**Changes:**
- 2629 files changed, 171843 insertions(+), 221995 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2579 more files

---

### migrate_to_event_rpc

**Last Commit:**
- Hash: `28828c5a`
- Author: Jack Gerrits
- Date: 2024-12-30 16:50:13 -0500
- Message: Merge branch 'main' into migrate_to_event_rpc

**Comparison with main:**
- Commits ahead: 2955
- Commits behind: 1

**Changes:**
- 1588 files changed, 36254 insertions(+), 145624 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1538 more files

---

### minior-assistant-fix

**Last Commit:**
- Hash: `cfee01fc`
- Author: Eric Zhu
- Date: 2025-01-09 23:01:51 -0800
- Message: Minor API doc update for openai assistant agent

**Comparison with main:**
- Commits ahead: 3022
- Commits behind: 1

**Changes:**
- 1534 files changed, 35263 insertions(+), 144390 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1484 more files

---

### mm_client

**Last Commit:**
- Hash: `e5205a9d`
- Author: Beibin Li
- Date: 2024-03-31 12:16:14 -0700
- Message: Merge branch 'main' into mm_client

**Comparison with main:**
- Commits ahead: 1501
- Commits behind: 1

**Changes:**
- 2444 files changed, 127752 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2394 more files

---

### move-samples

**Last Commit:**
- Hash: `3ba01130`
- Author: Eric Zhu
- Date: 2025-01-07 16:00:52 -0800
- Message: Remove utils

**Comparison with main:**
- Commits ahead: 2998
- Commits behind: 1

**Changes:**
- 1552 files changed, 35670 insertions(+), 144730 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1502 more files

---

### multi-task-chat-TOP

**Last Commit:**
- Hash: `c2ae0c78`
- Author: Qingyun Wu
- Date: 2024-01-25 13:55:17 -0500
- Message: Merge remote-tracking branch 'origin/multi-task-chat' into multi-task-chat-TOP

**Comparison with main:**
- Commits ahead: 1195
- Commits behind: 1

**Changes:**
- 2202 files changed, 83949 insertions(+), 241121 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2152 more files

---

### neurips

**Last Commit:**
- Hash: `224165d9`
- Author: afourney
- Date: 2024-12-10 10:07:16 -0800
- Message: Simplify video_surfer demo. (#4643)

**Comparison with main:**
- Commits ahead: 2877
- Commits behind: 1

**Changes:**
- 1651 files changed, 39573 insertions(+), 156668 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1601 more files

---

### o1-example

**Last Commit:**
- Hash: `e7544784`
- Author: Mohammad Mazraeh
- Date: 2024-11-26 02:46:27 +0000
- Message: Merge branch '0.2' into o1-example

**Comparison with main:**
- Commits ahead: 1972
- Commits behind: 1

**Changes:**
- 2605 files changed, 189158 insertions(+), 211064 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2555 more files

---

### osllm

**Last Commit:**
- Hash: `7dad875f`
- Author: Yogesh Haribhau Kulkarni
- Date: 2023-10-25 23:00:05 +0530
- Message: Added LM Studio way of serving open-source models (#377)

**Comparison with main:**
- Commits ahead: 785
- Commits behind: 1

**Changes:**
- 1946 files changed, 28258 insertions(+), 242684 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- `autogen/agentchat/contrib/math_user_proxy_agent.py`
- `autogen/agentchat/contrib/retrieve_assistant_agent.py`
- `autogen/agentchat/contrib/retrieve_user_proxy_agent.py`
- ... and 1896 more files

---

### Oslo

**Last Commit:**
- Hash: `50ac5476`
- Author: Anush
- Date: 2023-10-25 10:38:43 +0530
- Message: feat: Qdrant vector store support (#303)

**Comparison with main:**
- Commits ahead: 915
- Commits behind: 1

**Changes:**
- 1966 files changed, 36202 insertions(+), 242612 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- `autogen/agentchat/contrib/__init__.py`
- `autogen/agentchat/contrib/math_user_proxy_agent.py`
- ... and 1916 more files

---

### patch/v0.4.2

**Last Commit:**
- Hash: `c23b108e`
- Author: Jack Gerrits
- Date: 2025-01-15 10:39:51 -0500
- Message: Update to 0.4.2

**Comparison with main:**
- Commits ahead: 3039
- Commits behind: 1

**Changes:**
- 1528 files changed, 35127 insertions(+), 143912 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1478 more files

---

### profiler

**Last Commit:**
- Hash: `8f82c115`
- Author: gagb
- Date: 2023-11-04 02:15:22 +0000
- Message: Add code for profiling a testbed conversation

**Comparison with main:**
- Commits ahead: 945
- Commits behind: 1

**Changes:**
- 1983 files changed, 38112 insertions(+), 242612 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- `autogen/agentchat/contrib/__init__.py`
- `autogen/agentchat/contrib/math_user_proxy_agent.py`
- ... and 1933 more files

---

### profiler-0.1.0

**Last Commit:**
- Hash: `2bc48803`
- Author: gagb
- Date: 2023-12-05 01:53:41 +0000
- Message: Change to use openaiwrapper

**Comparison with main:**
- Commits ahead: 1034
- Commits behind: 1

**Changes:**
- 2110 files changed, 56690 insertions(+), 241536 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- ... and 2060 more files

---

### python-v0.4.8.1

**Last Commit:**
- Hash: `3b9aa013`
- Author: Eric Zhu
- Date: 2025-03-05 09:07:59 -0800
- Message: update version number

**Comparison with main:**
- Commits ahead: 3379
- Commits behind: 1

**Changes:**
- 843 files changed, 14792 insertions(+), 95760 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RunContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/TeamState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- ... and 793 more files

---

### python-v0.4.8.2

**Last Commit:**
- Hash: `c6c2c8e8`
- Author: Eric Zhu
- Date: 2025-03-07 15:41:04 -0800
- Message: update version

**Comparison with main:**
- Commits ahead: 3382
- Commits behind: 1

**Changes:**
- 842 files changed, 14785 insertions(+), 95728 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RunContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/TeamState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- ... and 792 more files

---

### python-v0.4.9.1

**Last Commit:**
- Hash: `27fd76dc`
- Author: Eric Zhu
- Date: 2025-03-13 21:49:14 -0700
- Message: update version to v0.4.9.1

**Comparison with main:**
- Commits ahead: 3420
- Commits behind: 1

**Changes:**
- 763 files changed, 13517 insertions(+), 84450 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMentionTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TimeoutTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TokenUsageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/Agents/AIAgent/InferenceAgent.cs`
- `dotnet/src/Microsoft.AutoGen/Core/InProcessRuntime.cs`
- `dotnet/src/Microsoft.AutoGen/Core/MessageDelivery.cs`
- `dotnet/src/Microsoft.AutoGen/Core/ResultSink.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcGateway.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcGatewayService.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcWorkerConnection.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- ... and 713 more files

---

### python-v0.4.9.2

**Last Commit:**
- Hash: `4a1660fe`
- Author: Eric Zhu
- Date: 2025-03-14 12:20:42 -0700
- Message: Upgrade llama cpp to 0.3.8 to fix windows related error (#5948)

**Comparison with main:**
- Commits ahead: 3423
- Commits behind: 1

**Changes:**
- 763 files changed, 13515 insertions(+), 84432 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMentionTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TimeoutTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TokenUsageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/Agents/AIAgent/InferenceAgent.cs`
- `dotnet/src/Microsoft.AutoGen/Core/InProcessRuntime.cs`
- `dotnet/src/Microsoft.AutoGen/Core/MessageDelivery.cs`
- `dotnet/src/Microsoft.AutoGen/Core/ResultSink.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcGateway.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcGatewayService.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcWorkerConnection.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- ... and 713 more files

---

### python-v0.4.9.3

**Last Commit:**
- Hash: `e45a1576`
- Author: Eric Zhu
- Date: 2025-03-28 21:35:01 -0700
- Message: update version v0.4.9.3

**Comparison with main:**
- Commits ahead: 3426
- Commits behind: 1

**Changes:**
- 763 files changed, 13526 insertions(+), 84341 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMentionTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TextMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TimeoutTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/TokenUsageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/Agents/AIAgent/InferenceAgent.cs`
- `dotnet/src/Microsoft.AutoGen/Core/InProcessRuntime.cs`
- `dotnet/src/Microsoft.AutoGen/Core/MessageDelivery.cs`
- `dotnet/src/Microsoft.AutoGen/Core/ResultSink.cs`
- `dotnet/src/Microsoft.AutoGen/Extensions/MEAI/ServiceCollectionChatCompletionExtensions.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcGateway.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcGatewayService.cs`
- `dotnet/src/Microsoft.AutoGen/RuntimeGateway.Grpc/Services/Grpc/GrpcWorkerConnection.cs`
- `dotnet/test/AutoGen.AzureAIInference.Tests/ChatCompletionClientAgentTests.cs`
- ... and 713 more files

---

### qw-dev

**Last Commit:**
- Hash: `77558b73`
- Author: Qingyun Wu
- Date: 2024-02-01 18:13:55 -0500
- Message: add states

**Comparison with main:**
- Commits ahead: 1209
- Commits behind: 1

**Changes:**
- 2217 files changed, 83016 insertions(+), 240561 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2167 more files

---

### raimondasl/issue-5186

**Last Commit:**
- Hash: `6bd8b1bb`
- Author: Eric Zhu
- Date: 2025-01-24 11:18:49 -0800
- Message: Merge branch 'main' into raimondasl/issue-5186

**Comparison with main:**
- Commits ahead: 3089
- Commits behind: 1

**Changes:**
- 1522 files changed, 37141 insertions(+), 136825 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1472 more files

---

### readme-icon

**Last Commit:**
- Hash: `24e3dd3e`
- Author: Jieyu Zhang
- Date: 2023-12-02 10:29:40 -0800
- Message: Update README.md

**Comparison with main:**
- Commits ahead: 1022
- Commits behind: 1

**Changes:**
- 2098 files changed, 53483 insertions(+), 241537 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-lmm.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- ... and 2048 more files

---

### refactorization-middleware

**Last Commit:**
- Hash: `400c4144`
- Author: Davor Runje
- Date: 2024-01-26 15:22:16 +0000
- Message: polishing

**Comparison with main:**
- Commits ahead: 1283
- Commits behind: 1

**Changes:**
- 2223 files changed, 83403 insertions(+), 240562 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2173 more files

---

### release/dotnet/0.0.14

**Last Commit:**
- Hash: `7f635b43`
- Author: Xiaoyun Zhang
- Date: 2024-05-28 14:55:40 -0700
- Message: [.Net] Update website for AutoGen.SemanticKernel and AutoGen.Ollama (#2814)

**Comparison with main:**
- Commits ahead: 1667
- Commits behind: 1

**Changes:**
- 2531 files changed, 152153 insertions(+), 226198 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2481 more files

---

### release/dotnet/0.0.15

**Last Commit:**
- Hash: `9d1b5386`
- Author: LittleLittleCloud
- Date: 2024-06-14 09:09:16 -0700
- Message: Merge branch 'main' into release/dotnet/0.0.15

**Comparison with main:**
- Commits ahead: 1706
- Commits behind: 1

**Changes:**
- 2556 files changed, 159234 insertions(+), 223272 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2506 more files

---

### release/dotnet/0.0.17

**Last Commit:**
- Hash: `04be2ee9`
- Author: Xiaoyun Zhang
- Date: 2024-07-29 11:32:26 -0700
- Message: bump version and add release note (#3246)

**Comparison with main:**
- Commits ahead: 1807
- Commits behind: 1

**Changes:**
- 2571 files changed, 170672 insertions(+), 219139 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2521 more files

---

### release/dotnet/0.1.0

**Last Commit:**
- Hash: `7b5c5eee`
- Author: Xiaoyun Zhang
- Date: 2024-08-21 13:20:13 -0700
- Message: [.Net] Release 0.1.0 (#3398)

**Comparison with main:**
- Commits ahead: 1848
- Commits behind: 1

**Changes:**
- 2553 files changed, 168789 insertions(+), 215122 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2503 more files

---

### release/dotnet/0.2.0

**Last Commit:**
- Hash: `b97bca55`
- Author: Xiaoyun Zhang
- Date: 2024-09-05 14:23:52 -0700
- Message: [.Net] release v0.2.0 (#3483)

**Comparison with main:**
- Commits ahead: 1882
- Commits behind: 1

**Changes:**
- 2554 files changed, 173011 insertions(+), 211117 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2504 more files

---

### release/dotnet/0.2.1

**Last Commit:**
- Hash: `6c9d9d8c`
- Author: David Luong
- Date: 2024-09-13 17:21:19 -0400
- Message: [.NET] Release v0.2.1 (#3529)

**Comparison with main:**
- Commits ahead: 1892
- Commits behind: 1

**Changes:**
- 2558 files changed, 174374 insertions(+), 211064 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2508 more files

---

### release/dotnet/0.2.2

**Last Commit:**
- Hash: `3bd87b9d`
- Author: Ryan Sweet
- Date: 2024-11-16 09:03:12 -0800
- Message: Merge branch 'main' into release/dotnet/0.2.2

**Comparison with main:**
- Commits ahead: 2727
- Commits behind: 1

**Changes:**
- 1716 files changed, 41257 insertions(+), 171106 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/design/03 - Agent Worker Protocol.md`
- `docs/design/04 - Agent and Topic ID Specs.md`
- `docs/design/readme.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- ... and 1666 more files

---

### remove-contrib-openaitest

**Last Commit:**
- Hash: `9a216b1d`
- Author: Ian
- Date: 2023-11-13 01:59:46 +0800
- Message: Openai assistant function usage notebook (#639)

**Comparison with main:**
- Commits ahead: 960
- Commits behind: 1

**Changes:**
- 2006 files changed, 43277 insertions(+), 242611 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-lmm.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- ... and 1956 more files

---

### remove_deprecations

**Last Commit:**
- Hash: `2c40e2d1`
- Author: Jack Gerrits
- Date: 2025-01-08 08:51:42 -0500
- Message: Merge branch 'main' into remove_deprecations

**Comparison with main:**
- Commits ahead: 2985
- Commits behind: 1

**Changes:**
- 1548 files changed, 35430 insertions(+), 144737 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1498 more files

---

### remove_switcher_content_override

**Last Commit:**
- Hash: `2a7cf0a0`
- Author: Jack Gerrits
- Date: 2025-01-08 13:07:47 -0500
- Message: Merge branch 'main' into remove_switcher_content_override

**Comparison with main:**
- Commits ahead: 2994
- Commits behind: 1

**Changes:**
- 1546 files changed, 35596 insertions(+), 144887 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1496 more files

---

### replacecreate_completion_client_from_env

**Last Commit:**
- Hash: `39632e95`
- Author: Jack Gerrits
- Date: 2025-01-08 09:30:04 -0500
- Message: Merge branch 'main' into replacecreate_completion_client_from_env

**Comparison with main:**
- Commits ahead: 2992
- Commits behind: 1

**Changes:**
- 1548 files changed, 35639 insertions(+), 144891 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1498 more files

---

### revert-3470-patch-1

**Last Commit:**
- Hash: `2c225e7a`
- Author: Xiaoyun Zhang
- Date: 2024-09-05 14:32:53 -0700
- Message: Revert "Update Installation.md (#3470)"

**Comparison with main:**
- Commits ahead: 1825
- Commits behind: 1

**Changes:**
- 2505 files changed, 147069 insertions(+), 231615 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2455 more files

---

### rpc_over_events

**Last Commit:**
- Hash: `39a7a804`
- Author: Jack Gerrits
- Date: 2024-12-20 16:16:26 -0500
- Message: WIP checkpoint

**Comparison with main:**
- Commits ahead: 2917
- Commits behind: 1

**Changes:**
- 1632 files changed, 38938 insertions(+), 151099 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1582 more files

---

### rysweet-3920-net-example-that-shows-x-lang-composition

**Last Commit:**
- Hash: `48892399`
- Author: Xiaoyun Zhang
- Date: 2024-12-03 10:24:05 -0800
- Message: .NET Add protos to paths-filter (#4493)

**Comparison with main:**
- Commits ahead: 2815
- Commits behind: 1

**Changes:**
- 1682 files changed, 39998 insertions(+), 165139 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- ... and 1632 more files

---

### rysweet-add-azd-container-apps-support

**Last Commit:**
- Hash: `acd7e864`
- Author: Ryan Sweet
- Date: 2025-02-14 07:42:18 -0800
- Message: add a buffer to message delivery so that clients wh subscribe within a window can receive (#5543)

**Comparison with main:**
- Commits ahead: 3295
- Commits behind: 1

**Changes:**
- 911 files changed, 15493 insertions(+), 108544 deletions(-)

**Modified files:**

- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/README.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/samples/AgentChat/AutoGen.Basic.Sample/Example10_SemanticKernel.cs`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/Extension/KernelExtension.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelAgent.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- ... and 861 more files

---

### rysweet-add-message-buffer-to-registry

**Last Commit:**
- Hash: `15cace04`
- Author: Ryan Sweet
- Date: 2025-02-13 17:51:23 -0800
- Message: adds a buffer to message delivery so that clients who subscribe within a five second window of a message will receive it.

**Comparison with main:**
- Commits ahead: 3329
- Commits behind: 1

**Changes:**
- 916 files changed, 15378 insertions(+), 108654 deletions(-)

**Modified files:**

- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/README.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/samples/AgentChat/AutoGen.Basic.Sample/Example10_SemanticKernel.cs`
- `dotnet/samples/Hello/HelloAgent/Program.cs`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/Extension/KernelExtension.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelAgent.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- ... and 866 more files

---

### rysweet-agent-inspector-scratch

**Last Commit:**
- Hash: `72552a7b`
- Author: Ryan Sweet
- Date: 2024-11-22 13:34:24 -0800
- Message: messing around

**Comparison with main:**
- Commits ahead: 2751
- Commits behind: 1

**Changes:**
- 1707 files changed, 42392 insertions(+), 169600 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/design/03 - Agent Worker Protocol.md`
- `docs/design/04 - Agent and Topic ID Specs.md`
- `docs/design/readme.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- ... and 1657 more files

---

### rysweet-HelloAppHost-python-check

**Last Commit:**
- Hash: `5c7f4b0f`
- Author: Ryan Sweet
- Date: 2025-01-26 16:58:47 -0800
- Message: interim

**Comparison with main:**
- Commits ahead: 3073
- Commits behind: 1

**Changes:**
- 1527 files changed, 36860 insertions(+), 139236 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1477 more files

---

### rysweet-ohdear-i-lost-something

**Last Commit:**
- Hash: `93a2a3d0`
- Author: Ryan Sweet
- Date: 2025-01-28 10:16:31 -0800
- Message: stash

**Comparison with main:**
- Commits ahead: 3076
- Commits behind: 1

**Changes:**
- 1527 files changed, 36939 insertions(+), 138956 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/dotnet/user-guide/core-user-guide/defining-message-types.md`
- `docs/dotnet/user-guide/core-user-guide/differences-python.md`
- `docs/dotnet/user-guide/core-user-guide/getting-started.md`
- `docs/dotnet/user-guide/core-user-guide/installation.md`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- ... and 1477 more files

---

### rysweet-typescript

**Last Commit:**
- Hash: `a1c0cdf9`
- Author: Ryan Sweet
- Date: 2025-03-06 16:34:06 -0800
- Message: Merge branch 'main' into rysweet-typescript

**Comparison with main:**
- Commits ahead: 3434
- Commits behind: 1

**Changes:**
- 884 files changed, 18221 insertions(+), 87677 deletions(-)

**Modified files:**

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/typescript-build-test.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/OutputCollectorAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/RoundRobinGroupChat.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/BaseState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/ChatAgentContainerState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/SerializedState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/State/TeamState.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/ExternalTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/FunctionCallTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/HandoffTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/MaxMessageTermination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Terminations/SourceMatchTermination.cs`
- ... and 834 more files

---

### rysweet-typescript-grpc

**Last Commit:**
- Hash: `4c96064f`
- Author: Ryan Sweet
- Date: 2025-02-26 09:11:17 -0800
- Message: iteration on the tests

**Comparison with main:**
- Commits ahead: 3369
- Commits behind: 1

**Changes:**
- 1007 files changed, 25521 insertions(+), 103677 deletions(-)

**Modified files:**

- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/typescript-build-test.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/samples/AgentChat/AutoGen.Basic.Sample/Example10_SemanticKernel.cs`
- `dotnet/src/AutoGen.Core/Function/FunctionAttribute.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/Extension/KernelExtension.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelAgent.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelChatCompletionAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ModelContext.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Termination.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Tools.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Usage.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/ChatAgentRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatBase.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatHandlerRouter.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/GroupChat/GroupChatManagerBase.cs`
- ... and 957 more files

---

### single

**Last Commit:**
- Hash: `8844f865`
- Author: Qingyun Wu
- Date: 2024-03-15 18:26:45 -0400
- Message: Allow different senders in nested chat (#2028)

**Comparison with main:**
- Commits ahead: 1404
- Commits behind: 1

**Changes:**
- 2398 files changed, 117363 insertions(+), 241421 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2348 more files

---

### slm

**Last Commit:**
- Hash: `370ebf5e`
- Author: Li Jiang
- Date: 2023-11-17 21:56:11 +0800
- Message: Update speaker selector in GroupChat and update some notebooks (#688)

**Comparison with main:**
- Commits ahead: 982
- Commits behind: 1

**Changes:**
- 2018 files changed, 43064 insertions(+), 242611 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-lmm.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- ... and 1968 more files

---

### sort-import-ruff

**Last Commit:**
- Hash: `120d4f57`
- Author: Davor Runje
- Date: 2024-03-28 12:28:29 +0000
- Message: resolve merge conflicts

**Comparison with main:**
- Commits ahead: 1461
- Commits behind: 1

**Changes:**
- 2433 files changed, 126170 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2383 more files

---

### SQL

**Last Commit:**
- Hash: `a911d1c2`
- Author: olgavrou
- Date: 2024-01-18 19:03:49 +0200
- Message: set use_docker to default to True (#1147)

**Comparison with main:**
- Commits ahead: 1168
- Commits behind: 1

**Changes:**
- 2178 files changed, 75596 insertions(+), 241158 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/dotnet-run-openai-test-and-notebooks.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- ... and 2128 more files

---

### staging

**Last Commit:**
- Hash: `4084a9f3`
- Author: Jack Gerrits
- Date: 2024-10-09 15:17:59 -0400
- Message: Merge branch 'main' into staging

**Comparison with main:**
- Commits ahead: 2546
- Commits behind: 1

**Changes:**
- 1764 files changed, 41421 insertions(+), 186947 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build-test-packages.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-publish-nuget.yml`
- `.github/workflows/dotnet-publish-packages.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `CONTRIBUTORS.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/design/03 - worker-protocol.md`
- `docs/design/04 - Agent and Topic ID Specs.md`
- `docs/design/05 - Services.md`
- `docs/design/readme.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- ... and 1714 more files

---

### stateflow

**Last Commit:**
- Hash: `289cb60d`
- Author: kevin666aa
- Date: 2024-02-28 19:49:08 -0500
- Message: Merge remote-tracking branch 'origin/main' into stateflow

**Comparison with main:**
- Commits ahead: 1310
- Commits behind: 1

**Changes:**
- 2281 files changed, 101677 insertions(+), 239808 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2231 more files

---

### support_no_chromadb

**Last Commit:**
- Hash: `3f044de4`
- Author: Li Jiang
- Date: 2023-11-05 18:19:25 +0800
- Message: Remove temp file

**Comparison with main:**
- Commits ahead: 936
- Commits behind: 1

**Changes:**
- 1986 files changed, 38481 insertions(+), 242612 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- ... and 1936 more files

---

### sweben-agent

**Last Commit:**
- Hash: `03d1afa6`
- Author: Hk669
- Date: 2024-08-18 16:19:22 +0530
- Message: merge branch

**Comparison with main:**
- Commits ahead: 1846
- Commits behind: 1

**Changes:**
- 2557 files changed, 169255 insertions(+), 215971 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2507 more files

---

### task

**Last Commit:**
- Hash: `e0e0680c`
- Author: Qingyun Wu
- Date: 2024-02-29 22:29:32 -0500
- Message: add task

**Comparison with main:**
- Commits ahead: 1315
- Commits behind: 1

**Changes:**
- 2281 files changed, 101550 insertions(+), 239806 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2231 more files

---

### teachability

**Last Commit:**
- Hash: `f7950178`
- Author: gagb
- Date: 2023-10-27 12:05:25 -0700
- Message: Sanitize further

**Comparison with main:**
- Commits ahead: 912
- Commits behind: 1

**Changes:**
- 1964 files changed, 34554 insertions(+), 242612 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- `autogen/agentchat/contrib/__init__.py`
- `autogen/agentchat/contrib/math_user_proxy_agent.py`
- ... and 1914 more files

---

### tool_support

**Last Commit:**
- Hash: `76f5f5a6`
- Author: LeoLjl
- Date: 2024-04-25 01:08:30 +0800
- Message: Merge branch 'main' into tool_support

**Comparison with main:**
- Commits ahead: 1575
- Commits behind: 1

**Changes:**
- 2535 files changed, 142432 insertions(+), 241364 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2485 more files

---

### tutorial-index

**Last Commit:**
- Hash: `2220117d`
- Author: Eric Zhu
- Date: 2025-01-08 15:20:30 -0800
- Message: Merge branch 'main' into tutorial-index

**Comparison with main:**
- Commits ahead: 2999
- Commits behind: 1

**Changes:**
- 1539 files changed, 35618 insertions(+), 144630 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- ... and 1489 more files

---

### u/#4354

**Last Commit:**
- Hash: `6d223b57`
- Author: XiaoYun Zhang
- Date: 2024-12-13 13:29:24 -0800
- Message: Merge branch 'u/#4354' of https://github.com/microsoft/autogen into u/#4354

**Comparison with main:**
- Commits ahead: 2901
- Commits behind: 1

**Changes:**
- 1643 files changed, 39519 insertions(+), 154983 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1593 more files

---

### u/fix#4618

**Last Commit:**
- Hash: `dfb76020`
- Author: Xiaoyun Zhang
- Date: 2024-12-12 12:35:29 -0800
- Message: Update dotnet-build.yml

**Comparison with main:**
- Commits ahead: 2884
- Commits behind: 1

**Changes:**
- 1643 files changed, 37067 insertions(+), 156758 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1593 more files

---

### u/xiaoyun/updateAOAI

**Last Commit:**
- Hash: `3148bceb`
- Author: XiaoYun Zhang
- Date: 2025-04-07 13:54:09 -0700
- Message: update oai and aoai package version

**Comparison with main:**
- Commits ahead: 3287
- Commits behind: 1

**Changes:**
- 952 files changed, 15330 insertions(+), 110482 deletions(-)

**Modified files:**

- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/README.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- `dotnet/dotnet-install.sh`
- `dotnet/eng/MetaInfo.props`
- `dotnet/samples/AgentChat/AutoGen.Basic.Sample/Example10_SemanticKernel.cs`
- `dotnet/samples/Hello/HelloAgent/HelloAgent.cs`
- `dotnet/samples/Hello/HelloAgent/HelloAgent.csproj`
- `dotnet/samples/Hello/HelloAgent/Program.cs`
- `dotnet/src/AutoGen.Core/Middleware/FunctionCallMiddleware.cs`
- `dotnet/src/AutoGen.SemanticKernel/Extension/KernelExtension.cs`
- `dotnet/src/AutoGen.SemanticKernel/SemanticKernelAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ChatAgent.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/ITeam.cs`
- `dotnet/src/Microsoft.AutoGen/AgentChat/Abstractions/Messages.cs`
- ... and 902 more files

---

### update_old_site_for_04

**Last Commit:**
- Hash: `4b786f42`
- Author: Jack Gerrits
- Date: 2025-01-08 14:35:42 -0500
- Message: Update

**Comparison with main:**
- Commits ahead: 1977
- Commits behind: 1

**Changes:**
- 2604 files changed, 189234 insertions(+), 211064 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2554 more files

---

### useazureai

**Last Commit:**
- Hash: `965586d5`
- Author: Yiran Wu
- Date: 2023-12-04 18:34:27 -0500
- Message: Merge branch 'main' into useazureai

**Comparison with main:**
- Commits ahead: 1036
- Commits behind: 1

**Changes:**
- 2105 files changed, 56443 insertions(+), 241536 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/startup.sh`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `Dockerfile`
- `FAQ.md`
- `OAI_CONFIG_LIST_sample`
- `README.md`
- `SECURITY.md`
- `SUPPORT.md`
- `TRANSPARENCY_FAQS.md`
- `autogen-landing.jpg`
- `autogen/__init__.py`
- `autogen/agentchat/__init__.py`
- `autogen/agentchat/agent.py`
- `autogen/agentchat/assistant_agent.py`
- ... and 2055 more files

---

### version-requirement

**Last Commit:**
- Hash: `b6180ed2`
- Author: Eric Zhu
- Date: 2025-01-12 01:11:21 -0800
- Message: Add python version requirement to frontpage and readme

**Comparison with main:**
- Commits ahead: 3028
- Commits behind: 1

**Changes:**
- 1531 files changed, 35256 insertions(+), 144272 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- `dotnet/Directory.Build.props`
- `dotnet/Directory.Packages.props`
- `dotnet/README.md`
- ... and 1481 more files

---

### wael/add-azure-dalle

**Last Commit:**
- Hash: `db379009`
- Author: Ryan Sweet
- Date: 2024-10-18 11:28:47 -0700
- Message: Merge branch '0.2' into wael/add-azure-dalle

**Comparison with main:**
- Commits ahead: 1961
- Commits behind: 1

**Changes:**
- 2603 files changed, 188970 insertions(+), 211064 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- ... and 2553 more files

---

### wael/headless_web_surfer_audio

**Last Commit:**
- Hash: `6d4c143b`
- Author: Wael Karkoub
- Date: 2024-03-31 01:07:33 +0100
- Message: added files

**Comparison with main:**
- Commits ahead: 1495
- Commits behind: 1

**Changes:**
- 2446 files changed, 129904 insertions(+), 241402 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/samples-tools-tests.yml`
- `.github/workflows/single-python-package.yml`
- `.github/workflows/type-check.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- ... and 2396 more files

---

### web_surfer_fixes

**Last Commit:**
- Hash: `ee151d1f`
- Author: Hussein Mozannar
- Date: 2024-12-08 23:50:11 -0800
- Message: Merge branch 'web_surfer_fixes' of https://github.com/microsoft/autogen into web_surfer_fixes

**Comparison with main:**
- Commits ahead: 2881
- Commits behind: 1

**Changes:**
- 1662 files changed, 39709 insertions(+), 160082 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-needs-triage.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `FAQ.md`
- `README.md`
- `autogen-landing.jpg`
- `codecov.yml`
- `docs/design/01 - Programming Model.md`
- `docs/design/02 - Topics.md`
- `docs/dotnet/.gitignore`
- `docs/dotnet/README.md`
- `docs/dotnet/core/differences-from-python.md`
- `docs/dotnet/core/index.md`
- `docs/dotnet/core/installation.md`
- `docs/dotnet/core/protobuf-message-types.md`
- `docs/dotnet/core/toc.yml`
- `docs/dotnet/core/tutorial.md`
- `docs/dotnet/docfx.json`
- `docs/dotnet/index.md`
- `docs/dotnet/template/public/main.css`
- `docs/dotnet/template/public/main.js`
- `docs/dotnet/toc.yml`
- `docs/switcher.json`
- `dotnet/.config/dotnet-tools.json`
- `dotnet/.editorconfig`
- `dotnet/.tools/test-aot-compatibility.ps1`
- `dotnet/AutoGen.sln`
- ... and 1612 more files

---

### workflow

**Last Commit:**
- Hash: `d35754dd`
- Author: Rohit Singh Rathaur
- Date: 2024-02-28 12:54:05 +0530
- Message: make default model of  a constant class variable (#1780)

**Comparison with main:**
- Commits ahead: 1308
- Commits behind: 1

**Changes:**
- 2278 files changed, 100859 insertions(+), 239808 deletions(-)

**Modified files:**

- `.azure/pipelines/build.yaml`
- `.azure/pipelines/templates/build.yaml`
- `.azure/pipelines/templates/vars.yaml`
- `.coveragerc`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/dev/Dockerfile`
- `.devcontainer/dev/devcontainer.json`
- `.devcontainer/devcontainer.json`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/full/Dockerfile`
- `.devcontainer/full/devcontainer.json`
- `.devcontainer/startup.sh`
- `.devcontainer/studio/Dockerfile`
- `.devcontainer/studio/devcontainer.json`
- `.gitattributes`
- `.github/ISSUE_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/1-bug_report.yml`
- `.github/ISSUE_TEMPLATE/2-doc_issue.yml`
- `.github/ISSUE_TEMPLATE/3-maintainer_only.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/general_issue.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/copilot-instructions.md`
- `.github/workflows/build.yml`
- `.github/workflows/checks.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/contrib-openai.yml`
- `.github/workflows/contrib-tests.yml`
- `.github/workflows/deploy-website.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dotnet-build.yml`
- `.github/workflows/dotnet-release.yml`
- `.github/workflows/integration.yml`
- `.github/workflows/issue-user-responded.yml`
- `.github/workflows/lfs-check.yml`
- `.github/workflows/openai.yml`
- `.github/workflows/pre-commit.yml`
- `.github/workflows/pytest-mem0.yml`
- `.github/workflows/pytest-redis-memory.yml`
- `.github/workflows/python-package-0.2.yml`
- `.github/workflows/python-package.yml`
- `.github/workflows/single-python-package.yml`
- `.gitignore`
- `.pre-commit-config.yaml`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `FAQ.md`
- ... and 2228 more files

---
