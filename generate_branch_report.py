#!/usr/bin/env python3
"""
Script to generate a comprehensive report of all branches in the repository
compared to the main branch.
"""

import subprocess
import sys
from datetime import datetime
from typing import Dict, List, Tuple
import re


def run_git_command(command: List[str]) -> str:
    """Execute a git command and return its output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            cwd="/home/runner/work/autogen/autogen"
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command {' '.join(command)}: {e.stderr}", file=sys.stderr)
        return ""


def get_all_branches() -> List[str]:
    """Get list of all remote branches except HEAD."""
    output = run_git_command(["git", "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/"])
    branches = [b for b in output.split('\n') if b and 'HEAD' not in b]
    return sorted(branches)


def get_branch_info(branch: str) -> Dict:
    """Get detailed information about a branch."""
    info = {
        'name': branch.replace('origin/', ''),
        'full_name': branch,
        'exists': True,
        'error': None
    }
    
    try:
        # Get last commit info
        commit_info = run_git_command([
            "git", "log", "-1", 
            "--format=%H|%an|%ae|%ai|%s", 
            branch
        ])
        
        if commit_info:
            parts = commit_info.split('|', 4)
            info['last_commit_hash'] = parts[0][:8]
            info['last_commit_author'] = parts[1]
            info['last_commit_email'] = parts[2]
            info['last_commit_date'] = parts[3]
            info['last_commit_message'] = parts[4]
        
        # Get commits ahead/behind main
        try:
            rev_list = run_git_command([
                "git", "rev-list", "--left-right", "--count", 
                f"main...{branch}"
            ])
            if rev_list:
                parts = rev_list.split()
                info['commits_behind'] = int(parts[0])
                info['commits_ahead'] = int(parts[1])
        except:
            info['commits_behind'] = 0
            info['commits_ahead'] = 0
        
        # Get file changes summary
        try:
            # Use merge-base to find common ancestor
            merge_base_result = run_git_command(["git", "merge-base", "main", branch])
            
            # If merge-base fails or returns empty, try direct comparison
            if merge_base_result and merge_base_result.strip():
                merge_base = merge_base_result.strip()
            else:
                # If there's no common ancestor, use main directly
                merge_base = "main"
            
            # Get diff stats
            diff_stat = run_git_command([
                "git", "diff", "--shortstat", 
                merge_base, branch
            ])
            
            if diff_stat:
                info['diff_stat'] = diff_stat
                
                # Parse the stat
                files_match = re.search(r'(\d+) files? changed', diff_stat)
                insertions_match = re.search(r'(\d+) insertions?', diff_stat)
                deletions_match = re.search(r'(\d+) deletions?', diff_stat)
                
                info['files_changed'] = int(files_match.group(1)) if files_match else 0
                info['insertions'] = int(insertions_match.group(1)) if insertions_match else 0
                info['deletions'] = int(deletions_match.group(1)) if deletions_match else 0
            else:
                info['diff_stat'] = "No changes"
                info['files_changed'] = 0
                info['insertions'] = 0
                info['deletions'] = 0
            
            # Get list of changed files (limit to 50 for brevity)
            changed_files = run_git_command([
                "git", "diff", "--name-only", 
                merge_base, branch
            ])
            
            if changed_files:
                files = changed_files.split('\n')
                info['changed_files'] = files[:50]
                info['changed_files_count'] = len(files)
                info['has_more_files'] = len(files) > 50
            else:
                info['changed_files'] = []
                info['changed_files_count'] = 0
                info['has_more_files'] = False
                
        except Exception as e:
            info['diff_stat'] = f"Error getting diff: {str(e)}"
            info['files_changed'] = 0
            info['insertions'] = 0
            info['deletions'] = 0
            info['changed_files'] = []
            info['changed_files_count'] = 0
            
    except Exception as e:
        info['exists'] = False
        info['error'] = str(e)
    
    return info


def generate_markdown_report(branches_info: List[Dict]) -> str:
    """Generate a markdown report from branch information."""
    report = []
    
    # Header
    report.append("# Branch Comparison Report")
    report.append("")
    report.append(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    report.append(f"**Total branches analyzed:** {len(branches_info)}")
    report.append(f"**Comparison base:** main branch")
    report.append("")
    report.append("---")
    report.append("")
    
    # Table of Contents
    report.append("## Table of Contents")
    report.append("")
    report.append("- [Summary Statistics](#summary-statistics)")
    report.append("- [Branch Details](#branch-details)")
    report.append("")
    report.append("---")
    report.append("")
    
    # Summary Statistics
    report.append("## Summary Statistics")
    report.append("")
    
    branches_ahead = [b for b in branches_info if b.get('commits_ahead', 0) > 0]
    branches_behind = [b for b in branches_info if b.get('commits_behind', 0) > 0]
    branches_synced = [b for b in branches_info if b.get('commits_ahead', 0) == 0 and b.get('commits_behind', 0) == 0]
    branches_with_changes = [b for b in branches_info if b.get('files_changed', 0) > 0]
    
    report.append(f"- **Branches ahead of main:** {len(branches_ahead)}")
    report.append(f"- **Branches behind main:** {len(branches_behind)}")
    report.append(f"- **Branches in sync with main:** {len(branches_synced)}")
    report.append(f"- **Branches with file changes:** {len(branches_with_changes)}")
    report.append("")
    
    # Top 10 most divergent branches
    most_ahead = sorted(branches_info, key=lambda x: x.get('commits_ahead', 0), reverse=True)[:10]
    if most_ahead and most_ahead[0].get('commits_ahead', 0) > 0:
        report.append("### Top 10 Branches Most Ahead of Main")
        report.append("")
        report.append("| Branch | Commits Ahead | Last Commit |")
        report.append("|--------|---------------|-------------|")
        for branch in most_ahead:
            if branch.get('commits_ahead', 0) > 0:
                report.append(f"| {branch['name']} | {branch.get('commits_ahead', 0)} | {branch.get('last_commit_date', 'N/A')[:10]} |")
        report.append("")
    
    # Largest changes
    most_changes = sorted(branches_info, key=lambda x: x.get('files_changed', 0), reverse=True)[:10]
    if most_changes and most_changes[0].get('files_changed', 0) > 0:
        report.append("### Top 10 Branches with Most File Changes")
        report.append("")
        report.append("| Branch | Files Changed | Insertions | Deletions |")
        report.append("|--------|---------------|------------|-----------|")
        for branch in most_changes:
            if branch.get('files_changed', 0) > 0:
                report.append(f"| {branch['name']} | {branch.get('files_changed', 0)} | +{branch.get('insertions', 0)} | -{branch.get('deletions', 0)} |")
        report.append("")
    
    report.append("---")
    report.append("")
    
    # Detailed branch information
    report.append("## Branch Details")
    report.append("")
    report.append("Detailed information for each branch, sorted alphabetically.")
    report.append("")
    
    for branch in sorted(branches_info, key=lambda x: x['name'].lower()):
        report.append(f"### {branch['name']}")
        report.append("")
        
        if not branch.get('exists', True):
            report.append(f"**Error:** {branch.get('error', 'Unknown error')}")
            report.append("")
            continue
        
        # Basic info
        report.append("**Last Commit:**")
        report.append(f"- Hash: `{branch.get('last_commit_hash', 'N/A')}`")
        report.append(f"- Author: {branch.get('last_commit_author', 'N/A')}")
        report.append(f"- Date: {branch.get('last_commit_date', 'N/A')}")
        report.append(f"- Message: {branch.get('last_commit_message', 'N/A')}")
        report.append("")
        
        # Divergence from main
        report.append("**Comparison with main:**")
        commits_ahead = branch.get('commits_ahead', 0)
        commits_behind = branch.get('commits_behind', 0)
        report.append(f"- Commits ahead: {commits_ahead}")
        report.append(f"- Commits behind: {commits_behind}")
        report.append("")
        
        # File changes
        if branch.get('diff_stat'):
            report.append("**Changes:**")
            report.append(f"- {branch.get('diff_stat', 'N/A')}")
            
            if branch.get('changed_files'):
                report.append("")
                report.append("**Modified files:**")
                report.append("")
                for file in branch['changed_files']:
                    report.append(f"- `{file}`")
                
                if branch.get('has_more_files'):
                    remaining = branch.get('changed_files_count', 0) - 50
                    report.append(f"- ... and {remaining} more files")
            report.append("")
        
        report.append("---")
        report.append("")
    
    return '\n'.join(report)


def main():
    """Main function to generate the branch comparison report."""
    print("Generating branch comparison report...")
    print("This may take a few minutes due to the large number of branches...")
    print()
    
    # Get all branches
    print("Fetching branch list...")
    branches = get_all_branches()
    print(f"Found {len(branches)} branches to analyze")
    print()
    
    # Analyze each branch
    branches_info = []
    for i, branch in enumerate(branches, 1):
        print(f"Analyzing branch {i}/{len(branches)}: {branch}")
        info = get_branch_info(branch)
        branches_info.append(info)
    
    print()
    print("Generating report...")
    
    # Generate markdown report
    report = generate_markdown_report(branches_info)
    
    # Save to file
    output_file = "/home/runner/work/autogen/autogen/BRANCH_COMPARISON_REPORT.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Report generated successfully: {output_file}")
    print(f"Total branches analyzed: {len(branches_info)}")
    
    # Print some quick stats
    branches_with_changes = [b for b in branches_info if b.get('files_changed', 0) > 0]
    print(f"Branches with changes: {len(branches_with_changes)}")
    

if __name__ == "__main__":
    main()
