#!/usr/bin/env python3
"""Analyze Team Store/B2B issues to understand budget allocation."""

import csv
from pathlib import Path
from datetime import datetime as dt
import json
import sys
sys.path.insert(0, '/Users/pete/dev/shopify/rudis-documentation/requests/jira-analysis')
from generate_report import categorize_work

# Load time tracking
with open('jira-analysis-data.json', 'r') as f:
    data = json.load(f)
all_estimation = data.get('time_tracking', {}).get('estimation_accuracy', [])

csv_path = Path('/Users/pete/dev/shopify/rudis-documentation/data/RUDIS-JIRA.csv')
team_store_issues = []

if csv_path.exists():
    with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            created_str = row.get('Created', '').strip()
            if created_str:
                try:
                    created_date = dt.strptime(created_str, '%d/%b/%y %I:%M %p')
                    if created_date.year == 2025:
                        issue = {
                            'key': row.get('Issue key', '').strip(),
                            'summary': row.get('Summary', '').strip(),
                            'description': row.get('Description', '').strip(),
                            'type': row.get('Issue Type', '').strip(),
                            'status': row.get('Status', '').strip(),
                            'priority': row.get('Priority', '').strip() or 'None'
                        }
                        category = categorize_work(issue)
                        if category == 'Team Store / B2B':
                            team_store_issues.append(issue)

print(f'=== TEAM STORE / B2B ANALYSIS ===\n')
print(f'Total Issues: {len(team_store_issues)}\n')

# Issue types
issue_types = {}
for issue in team_store_issues:
    itype = issue.get('type', 'Unknown')
    issue_types[itype] = issue_types.get(itype, 0) + 1

print('Issue Types:')
for itype, count in sorted(issue_types.items(), key=lambda x: x[1], reverse=True):
    print(f'  {itype}: {count}')
print()

# Status breakdown
resolved = [i for i in team_store_issues if i['status'] in ['Done', 'Closed']]
stuck = [i for i in team_store_issues if i['status'] in ['Hold', 'Update Requirements', 'Needs Estimate', 'Waiting for Approval']]
in_process = [i for i in team_store_issues if i['status'] in ['Approved', 'Ongoing', 'New']]

print(f'Status Breakdown:')
print(f'  Resolved: {len(resolved)} ({len(resolved)/len(team_store_issues)*100:.0f}%)')
print(f'  Stuck: {len(stuck)} ({len(stuck)/len(team_store_issues)*100:.0f}%)')
print(f'  In Process: {len(in_process)} ({len(in_process)/len(team_store_issues)*100:.0f}%)')
print()

# Priority breakdown
priorities = {}
for issue in team_store_issues:
    priority = issue.get('priority', 'None')
    priorities[priority] = priorities.get(priority, 0) + 1

print('Priority Breakdown:')
for priority, count in sorted(priorities.items(), key=lambda x: {'Critical': 0, 'Blocker': 1, 'Major': 2, 'Minor': 3, 'None': 4}.get(x[0], 5)):
    print(f'  {priority}: {count}')
print()

# Bug analysis
bug_issues = [i for i in team_store_issues if 'bug' in i['summary'].lower() or 'fix' in i['summary'].lower() or i['type'] == 'Bug']
print(f'Issues with bug keywords: {len(bug_issues)} ({len(bug_issues)/len(team_store_issues)*100:.0f}%)')
print()

# Time tracking analysis
team_store_keys = [i['key'] for i in team_store_issues]
team_store_keys_set = set(team_store_keys)
team_store_tracked = [est for est in all_estimation if est.get('issue_key') in team_store_keys_set]
team_store_hours = sum(est.get('time_spent_seconds', 0) / 3600 for est in team_store_tracked)
team_store_avg = team_store_hours / len(team_store_tracked) if team_store_tracked else 0

print('Time Tracking:')
print(f'  Issues with time tracking: {len(team_store_tracked)}')
print(f'  Total hours tracked: {team_store_hours:.0f}h')
print(f'  Average hours per tracked issue: {team_store_avg:.1f}h')
print()

# Compare to other categories
print('=== COMPARISON TO OTHER CATEGORIES ===\n')
categories_to_compare = ['Product Display (PDP)', 'Cart/Checkout/Conversion']
for cat in categories_to_compare:
    cat_issues = []
    if csv_path.exists():
        with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.DictReader(f)
            for row in reader:
                created_str = row.get('Created', '').strip()
                if created_str:
                    try:
                        created_date = dt.strptime(created_str, '%d/%b/%y %I:%M %p')
                        if created_date.year == 2025:
                            issue = {
                                'key': row.get('Issue key', '').strip(),
                                'summary': row.get('Summary', '').strip(),
                                'description': row.get('Description', '').strip(),
                                'type': row.get('Issue Type', '').strip(),
                                'status': row.get('Status', '').strip()
                            }
                            if categorize_work(issue) == cat:
                                cat_issues.append(issue)
                    except:
                        pass
    
    cat_resolved = len([i for i in cat_issues if i['status'] in ['Done', 'Closed']])
    cat_stuck = len([i for i in cat_issues if i['status'] in ['Hold', 'Update Requirements', 'Needs Estimate', 'Waiting for Approval']])
    cat_bugs = len([i for i in cat_issues if 'bug' in i['summary'].lower() or i['type'] == 'Bug'])
    
    cat_keys_set = set([i['key'] for i in cat_issues])
    cat_tracked = [est for est in all_estimation if est.get('issue_key') in cat_keys_set]
    cat_hours = sum(est.get('time_spent_seconds', 0) / 3600 for est in cat_tracked)
    cat_avg = cat_hours / len(cat_tracked) if cat_tracked else 0
    
    print(f'{cat}:')
    print(f'  Total Issues: {len(cat_issues)}')
    print(f'  Resolved: {cat_resolved} ({cat_resolved/len(cat_issues)*100:.0f}%)' if cat_issues else '  Resolved: 0')
    print(f'  Stuck: {cat_stuck} ({cat_stuck/len(cat_issues)*100:.0f}%)' if cat_issues else '  Stuck: 0')
    print(f'  Bugs: {cat_bugs} ({cat_bugs/len(cat_issues)*100:.0f}%)' if cat_issues else '  Bugs: 0')
    print(f'  Hours Tracked: {cat_hours:.0f}h')
    print(f'  Avg Hours/Issue: {cat_avg:.1f}h')
    print()

# Show stuck issues
print('=== STUCK ISSUES (Potential Blockers) ===\n')
for issue in stuck[:10]:
    print(f'{issue["key"]}: {issue["summary"][:80]}')
    print(f'  Status: {issue["status"]}, Priority: {issue["priority"]}')
    print()

# Show bug issues
print('=== BUG ISSUES ===\n')
for issue in bug_issues[:10]:
    print(f'{issue["key"]}: {issue["summary"][:80]}')
    print(f'  Status: {issue["status"]}, Type: {issue["type"]}')
    print()
