# Branch Comparison Report

This directory contains a comprehensive analysis of all branches in the repository compared to the main branch.

## Files

- **BRANCH_COMPARISON_REPORT.md** - The generated report containing analysis of all 192 branches
- **generate_branch_report.py** - Python script to regenerate the report
- **BRANCH_REPORT_README.md** - This file

## Report Contents

The `BRANCH_COMPARISON_REPORT.md` file contains:

1. **Summary Statistics**
   - Total number of branches analyzed
   - Count of branches ahead/behind/in sync with main
   - Top 10 branches most ahead of main
   - Top 10 branches with most file changes

2. **Detailed Branch Information**
   - For each of the 192 branches:
     - Last commit details (hash, author, date, message)
     - Number of commits ahead/behind main
     - File change statistics (files changed, insertions, deletions)
     - List of modified files (up to 50 files shown per branch)

## Regenerating the Report

To regenerate the report with the latest data:

```bash
cd /home/runner/work/autogen/autogen
python3 generate_branch_report.py
```

The script will:
1. Fetch all remote branches
2. Analyze each branch compared to main
3. Generate a new `BRANCH_COMPARISON_REPORT.md` file

**Note:** The script takes approximately 3-5 minutes to run due to the large number of branches (192).

## Key Findings

Based on the current report:

- **Total branches:** 192
- **Branches ahead of main:** 191
- **Branches behind main:** 190
- **Branches in sync with main:** 1 (the main branch itself)
- **Branches with file changes:** 190

### Most Divergent Branches

The branches most ahead of main include:
- copilot/fix-6542 (3655 commits ahead)
- copilot/fix-6210 (3633 commits ahead)
- ekzhu-optional-thought-as-content (3621 commits ahead)

### Largest Changes

The branches with the most file changes include:
- metaagent (2629 files changed)
- gagb-mednav (2626 files changed)
- five-trace (2624 files changed)

## Requirements

- Python 3.x
- Git
- Access to the repository

## Technical Details

The script uses git commands to:
- List all remote branches
- Get commit information for each branch
- Calculate commits ahead/behind using `git rev-list`
- Compare file changes using `git diff`
- Find common ancestors using `git merge-base`

For branches without a common ancestor with main, the script falls back to direct comparison.
