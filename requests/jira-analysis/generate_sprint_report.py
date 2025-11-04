#!/usr/bin/env python3
"""
Generate sprint-over-sprint analysis for the last 3 sprints.
Assumes 2-week sprints starting on Monday.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict, Counter
import statistics

def categorize_work(issue):
    """Categorize issue into strategic themes - same as main report."""
    summary = issue.get('summary', '').lower()
    itype = issue.get('type', '')
    
    if itype == 'Bug' or summary.startswith('bug:') or 'bug:' in summary:
        return 'Bug Fixes'
    if 'team' in summary or 'team store' in summary or 'team:' in summary or 'usaw' in summary or 'bulk' in summary:
        return 'Team Store / B2B'
    if 'pdp' in summary or 'product detail' in summary or 'variant' in summary or 'swatch' in summary:
        return 'Product Display (PDP)'
    if 'plp' in summary or 'product listing' in summary or 'collection' in summary:
        return 'Product Listing (PLP)'
    if 'cart' in summary or 'checkout' in summary or 'add to cart' in summary or 'atc' in summary:
        return 'Cart/Checkout/Conversion'
    if 'shipping' in summary or 'free shipping' in summary or 'tax' in summary:
        return 'Shipping/Logistics'
    if 'gtm' in summary or 'google tag' in summary or 'analytics' in summary or 'tracking' in summary or 'elevar' in summary or 'celigo' in summary or 'integration' in summary or 'pixel' in summary or 'attentive' in summary:
        return 'Analytics & Integrations'
    if 'cookie' in summary or 'onetrust' in summary or 'privacy' in summary or 'compliance' in summary or 'gdpr' in summary:
        return 'Compliance & Legal'
    if 'account' in summary or 'user' in summary or 'return' in summary or 'order' in summary or 'rewards' in summary or 'loyalty' in summary:
        return 'Account/User Experience'
    if 'pricing' in summary or 'price' in summary or 'sale' in summary or 'promo' in summary or 'discount' in summary:
        return 'Pricing & Promotions'
    if 'search' in summary or 'finder' in summary or 'quiz' in summary or 'recommendation' in summary or 'llm' in summary or 'chatgpt' in summary:
        return 'Search & Discovery'
    if 'catalog' in summary or 'pdf' in summary or 'content' in summary or 'page' in summary or 'landing' in summary or 'embed' in summary:
        return 'Content & Pages'
    if 'design' in summary or 'image' in summary or 'header' in summary or 'parallax' in summary or 'video' in summary or 'ui/ux' in summary or 'navigation' in summary or 'menu' in summary or 'template' in summary or 'font' in summary or 'spacing' in summary:
        return 'Design/UX Enhancements'
    if 'qa' in summary or 'qa cycle' in summary or 'uat' in summary or 'user acceptance' in summary or 'quality assurance' in summary:
        return 'QA & Testing'
    if 'test' in summary or 'investigate' in summary or 'research' in summary or 'a/b' in summary or 'ab test' in summary or 'smoke test' in summary:
        return 'Testing & Investigation'
    if 'db configuration' in summary or 'database' in summary or 'config' in summary or 'configuration' in summary:
        return 'Database & Configuration'
    if 'financial' in summary or 'fulfilment' in summary or 'refund' in summary or 'customer service' in summary:
        return 'Financial & Operations'
    if 'brand launch' in summary or 'product split' in summary or 'gift card' in summary or 'bundle' in summary or 'accessories' in summary or 'youth-adult' in summary:
        return 'Product Launches & Categories'
    if 'zendesk' in summary or 'digioh' in summary or 'global-e' in summary:
        return 'Third-party Tools & Integrations'
    if 'data cleanup' in summary or 'purchase event' in summary:
        return 'Data Management'
    if 'process' in summary or 'workflow' in summary or 'approval' in summary or 'quote' in summary or 'allocation' in summary or 'reminder' in summary:
        return 'Process & Operations'
    if itype == 'Epic' or 'roadmap' in summary or 'strategic' in summary or 'initiative' in summary:
        return 'Strategic Initiatives'
    if 'accessibility' in summary or 'accessible' in summary or 'aria' in summary or 'alternative text' in summary or 'alt text' in summary or 'wcag' in summary or 'a11y' in summary or 'visual cues' in summary or 'keyboard' in summary or 'valid label' in summary or 'form fields' in summary or 'rudis-amp' in summary:
        return 'Accessibility'
    if 'deploy' in summary or 'go live' in summary or 'golive' in summary or 'production' in summary or 'prod' in summary or 'preparation for' in summary or 'open countries' in summary:
        return 'Deployment & Operations'
    if 'sprint' in summary or 'dev' in summary or 'development' in summary:
        return 'Development Sprints'
    if 'ui spec' in summary or 'comps review' in summary or 'wireframe' in summary or 'spec' in summary:
        return 'Design Specs & Reviews'
    if 'framework' in summary or 'strategy' in summary or 'opt-in' in summary:
        return 'Framework & Strategy'
    if 'reporting' in summary or 'dashboard' in summary:
        return 'Reporting & Analytics'
    if 'spaghetti code' in summary or 'technical debt' in summary or 'refactor' in summary:
        return 'Technical Debt'
    if 'requirements' in summary or 'best practices' in summary or 'naming convention' in summary or 'convention' in summary or 'analysis' in summary or 'set-up' in summary or 'setup' in summary:
        return 'Requirements & Planning'
    if 'seo' in summary or 'robot' in summary or 'llms.txt' in summary or 'theme' in summary or 'api' in summary or 'middleware' in summary or 'component' in summary or 'uber' in summary or 'token' in summary or 'verification' in summary:
        return 'Technical/Infrastructure'
    return 'Other'

def parse_time_seconds(time_str):
    """Parse JIRA time format to seconds."""
    if not time_str or not time_str.strip():
        return None
    
    import re
    total_seconds = 0
    
    # Match patterns like "2h 30m", "1d 4h", "45m"
    patterns = [
        (r'(\d+)d', 86400),  # days
        (r'(\d+)h', 3600),   # hours
        (r'(\d+)m', 60)      # minutes
    ]
    
    for pattern, multiplier in patterns:
        matches = re.findall(pattern, time_str)
        for match in matches:
            total_seconds += int(match) * multiplier
    
    return total_seconds if total_seconds > 0 else None

def generate_sprint_report(json_path, csv_path, output_path):
    """Generate sprint-over-sprint analysis."""
    import csv
    
    # Load JSON data for time tracking
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Define last 3 sprints (2-week sprints, Monday-Sunday)
    # As of Nov 4, 2025 (Monday)
    today = datetime(2025, 11, 4)
    
    # Sprint 3: Oct 21 - Nov 3 (ending today)
    sprint3_start = datetime(2025, 10, 21)
    sprint3_end = datetime(2025, 11, 3)
    
    # Sprint 2: Oct 7 - Oct 20
    sprint2_start = datetime(2025, 10, 7)
    sprint2_end = datetime(2025, 10, 20)
    
    # Sprint 1: Sep 23 - Oct 6
    sprint1_start = datetime(2025, 9, 23)
    sprint1_end = datetime(2025, 10, 6)
    
    sprints = [
        ('Sprint 3', 'Oct 21 - Nov 3, 2025', sprint3_start, sprint3_end),
        ('Sprint 2', 'Oct 7 - Oct 20, 2025', sprint2_start, sprint2_end),
        ('Sprint 1', 'Sep 23 - Oct 6, 2025', sprint1_start, sprint1_end)
    ]
    
    # Load issues from CSV
    all_issues = []
    csv_file = Path(csv_path)
    if not csv_file.exists():
        csv_file = Path(__file__).parent.parent / 'data' / csv_path
    if not csv_file.exists():
        csv_file = Path('/Users/pete/dev/shopify/rudis-documentation/data') / csv_path
    
    if csv_file.exists():
        with open(csv_file, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.DictReader(f)
            for row in reader:
                created_str = row.get('Created', '').strip()
                if created_str:
                    try:
                        created_date = datetime.strptime(created_str, "%d/%b/%y %I:%M %p")
                        if created_date.year == 2025:
                            resolved_str = row.get('Resolved', '').strip()
                            resolved_date = None
                            if resolved_str:
                                try:
                                    resolved_date = datetime.strptime(resolved_str, "%d/%b/%y %I:%M %p")
                                except:
                                    pass
                            
                            issue_key = row.get('Issue key', '').strip()
                            all_issues.append({
                                'key': issue_key,
                                'summary': row.get('Summary', '').strip(),
                                'type': row.get('Issue Type', '').strip(),
                                'status': row.get('Status', '').strip(),
                                'priority': row.get('Priority', '').strip() or 'None',
                                'created': created_date,
                                'resolved': resolved_date,
                                'request_type': row.get('Custom field (Request Type)', '').strip(),
                                'category': row.get('Custom field (Category)', '').strip()
                            })
                    except:
                        continue
    
    # Analyze each sprint
    sprint_data = []
    all_estimation = data.get('time_tracking', {}).get('estimation_accuracy', [])
    
    for sprint_name, sprint_period, sprint_start, sprint_end in sprints:
        # Issues created in this sprint
        sprint_issues = [i for i in all_issues if sprint_start <= i['created'] <= sprint_end]
        
        # Issues resolved in this sprint (regardless of when created)
        sprint_resolved = [i for i in all_issues 
                          if i['resolved'] and sprint_start <= i['resolved'] <= sprint_end]
        
        # Categorize issues
        categorized = defaultdict(list)
        for issue in sprint_issues:
            category = categorize_work(issue)
            categorized[category].append(issue)
        
        # Resolution stats
        resolved_in_sprint = [i for i in sprint_issues if i['status'] in ['Done', 'Closed']]
        unresolved_in_sprint = [i for i in sprint_issues if i['status'] not in ['Done', 'Closed']]
        stuck_in_sprint = [i for i in sprint_issues if i['status'] in ['Hold', 'Update Requirements', 'Needs Estimate', 'Waiting for Approval']]
        
        # Time tracking
        sprint_keys = {i['key'] for i in sprint_issues}
        sprint_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                   for est in all_estimation 
                                   if est.get('issue_key') in sprint_keys)
        sprint_tracked_count = sum(1 for est in all_estimation if est.get('issue_key') in sprint_keys)
        
        # Estimate hours (tracked + estimated for untracked)
        avg_hours = sprint_tracked_hours / sprint_tracked_count if sprint_tracked_count > 0 else 0
        all_tracked_avg = data['time_tracking']['summary'].get('average_time_spent_hours', 0) or 10
        estimated_hours = sprint_tracked_hours + (avg_hours if avg_hours > 0 else all_tracked_avg) * (len(sprint_issues) - sprint_tracked_count)
        
        # Resolution times (for issues resolved in sprint)
        resolution_times = []
        for issue in sprint_resolved:
            if issue.get('created') and issue.get('resolved'):
                rt = (issue['resolved'] - issue['created']).days
                if rt <= 180:  # Exclude outliers
                    resolution_times.append(rt)
        
        avg_resolution = statistics.mean(resolution_times) if resolution_times else None
        
        sprint_data.append({
            'name': sprint_name,
            'period': sprint_period,
            'start': sprint_start,
            'end': sprint_end,
            'issues_created': len(sprint_issues),
            'issues_resolved': len(resolved_in_sprint),
            'issues_resolved_in_sprint': len(sprint_resolved),  # Resolved during sprint (any created date)
            'unresolved': len(unresolved_in_sprint),
            'stuck': len(stuck_in_sprint),
            'resolution_rate': len(resolved_in_sprint) / len(sprint_issues) * 100 if sprint_issues else 0,
            'tracked_hours': sprint_tracked_hours,
            'estimated_hours': estimated_hours,
            'avg_resolution_days': avg_resolution,
            'categories': dict(categorized),
            'resolved_issues': resolved_in_sprint,
            'unresolved_issues': unresolved_in_sprint,
            'stuck_issues': stuck_in_sprint
        })
    
    # Generate report
    report = []
    report.append("# RUDIS Sprint-Over-Sprint Analysis")
    report.append("")
    report.append(f"*Analysis Date: {datetime.now().strftime('%B %d, %Y')}*  ")
    report.append(f"*Report Period: Last 3 Sprints (2-week sprints, Monday-Sunday)*")
    report.append("")
    report.append("---")
    report.append("")
    
    # Sprint comparison table
    report.append("## Sprint Comparison Overview")
    report.append("")
    report.append("| Sprint | Period | Created | Resolved | Unresolved | Stuck | Resolution Rate | Est. Hours | Resolved in Sprint |")
    report.append("|--------|--------|---------|----------|------------|-------|-----------------|------------|-------------------|")
    
    for sprint in sprint_data:
        report.append(f"| {sprint['name']} | {sprint['period']} | {sprint['issues_created']} | {sprint['issues_resolved']} | {sprint['unresolved']} | {sprint['stuck']} | {sprint['resolution_rate']:.0f}% | {sprint['estimated_hours']:.0f}h | {sprint['issues_resolved_in_sprint']} |")
    
    report.append("")
    report.append("*Note: 'Resolved' = issues created in sprint that are now resolved. 'Resolved in Sprint' = issues resolved during sprint period (any created date).*")
    report.append("")
    
    # Trends and insights
    report.append("### Key Trends & Insights")
    report.append("")
    
    if len(sprint_data) >= 2:
        # Velocity trend
        created_trend = sprint_data[0]['issues_created'] - sprint_data[1]['issues_created']
        resolved_trend = sprint_data[0]['issues_resolved'] - sprint_data[1]['issues_resolved']
        resolved_in_sprint_trend = sprint_data[0]['issues_resolved_in_sprint'] - sprint_data[1]['issues_resolved_in_sprint']
        
        if sprint_data[1]['issues_created'] > 0:
            pct_change = created_trend / sprint_data[1]['issues_created'] * 100
            report.append(f"**Velocity:** {sprint_data[0]['name']} created {created_trend:+d} issues vs {sprint_data[1]['name']} ({pct_change:+.0f}% change)")
        else:
            report.append(f"**Velocity:** {sprint_data[0]['name']} created {created_trend:+d} issues vs {sprint_data[1]['name']}")
        
        report.append(f"**Completion Rate:** {sprint_data[0]['name']} resolved {sprint_data[0]['issues_resolved']}/{sprint_data[0]['issues_created']} ({sprint_data[0]['resolution_rate']:.0f}%) vs {sprint_data[1]['name']} {sprint_data[1]['issues_resolved']}/{sprint_data[1]['issues_created']} ({sprint_data[1]['resolution_rate']:.0f}%)")
        report.append(f"**Work Completed:** {sprint_data[0]['name']} completed {resolved_in_sprint_trend:+d} issues during sprint vs {sprint_data[1]['name']}")
        report.append("")
        
        # Stuck work trend
        stuck_trend = sprint_data[0]['stuck'] - sprint_data[1]['stuck']
        if sprint_data[0]['stuck'] > 0:
            report.append(f"**Stuck Work:** {sprint_data[0]['name']} has {sprint_data[0]['stuck']} stuck issues ({stuck_trend:+d} vs {sprint_data[1]['name']})")
            if sprint_data[0]['issues_created'] > 0 and sprint_data[0]['stuck'] > sprint_data[0]['issues_created'] * 0.5:
                report.append(f"  ⚠️ **Warning:** {sprint_data[0]['stuck']/sprint_data[0]['issues_created']*100:.0f}% of created issues are stuck")
            report.append("")
        
        if len(sprint_data) >= 3:
            # 3-sprint average
            avg_created = statistics.mean([s['issues_created'] for s in sprint_data])
            avg_resolved = statistics.mean([s['issues_resolved'] for s in sprint_data])
            avg_resolved_in_sprint = statistics.mean([s['issues_resolved_in_sprint'] for s in sprint_data])
            avg_hours = statistics.mean([s['estimated_hours'] for s in sprint_data])
            
            report.append(f"**3-Sprint Average:**")
            report.append(f"- {avg_created:.1f} issues created per sprint")
            if avg_created > 0:
                report.append(f"- {avg_resolved:.1f} issues resolved per sprint ({avg_resolved/avg_created*100:.0f}% resolution rate)")
            report.append(f"- {avg_resolved_in_sprint:.1f} issues resolved during sprint period")
            report.append(f"- {avg_hours:.0f}h estimated hours per sprint")
            report.append("")
            
            # Budget utilization
            monthly_budget = 70
            sprint_budget = monthly_budget * 2 / 4.33  # 2 weeks = ~32 hours
            budget_utilization = avg_hours / sprint_budget * 100
            report.append(f"**Budget Utilization:** {avg_hours:.0f}h per sprint vs {sprint_budget:.0f}h budget ({budget_utilization:.0f}%)")
            if budget_utilization > 100:
                report.append(f"  ⚠️ **Over Budget:** {(avg_hours - sprint_budget):.0f}h over per sprint ({((avg_hours - sprint_budget) / sprint_budget) * 100:.0f}%)")
            report.append("")
    
    # Category breakdown by sprint
    report.append("## Work Allocation by Category (Sprint Comparison)")
    report.append("")
    
    # Get all categories
    all_categories = set()
    for sprint in sprint_data:
        all_categories.update(sprint['categories'].keys())
    
    report.append("| Category | Sprint 3 | Sprint 2 | Sprint 1 | Trend |")
    report.append("|----------|----------|---------|----------|-------|")
    
    for category in sorted(all_categories):
        counts = []
        for sprint in sprint_data:
            counts.append(len(sprint['categories'].get(category, [])))
        
        trend = ""
        if len(counts) >= 2:
            if counts[0] > counts[1]:
                trend = "↑"
            elif counts[0] < counts[1]:
                trend = "↓"
            else:
                trend = "→"
        
        report.append(f"| {category} | {counts[0]} | {counts[1] if len(counts) > 1 else 0} | {counts[2] if len(counts) > 2 else 0} | {trend} |")
    
    report.append("")
    
    # Detailed sprint analysis
    for sprint in sprint_data:
        report.append(f"## {sprint['name']} ({sprint['period']})")
        report.append("")
        
        report.append(f"**Issues Created:** {sprint['issues_created']}")
        report.append(f"**Issues Resolved:** {sprint['issues_resolved']} ({sprint['resolution_rate']:.0f}%)")
        report.append(f"**Issues Resolved During Sprint:** {sprint['issues_resolved_in_sprint']} (includes issues from previous sprints)")
        report.append(f"**Unresolved:** {sprint['unresolved']}")
        report.append(f"**Stuck:** {sprint['stuck']}")
        report.append(f"**Estimated Hours:** {sprint['estimated_hours']:.0f}h")
        if sprint['avg_resolution_days']:
            report.append(f"**Avg Resolution Time:** {sprint['avg_resolution_days']:.1f} days")
        report.append("")
        
        # Top categories
        if sprint['categories']:
            report.append("**Top Categories:**")
            for category, issues in sorted(sprint['categories'].items(), key=lambda x: len(x[1]), reverse=True)[:5]:
                resolved = len([i for i in issues if i['status'] in ['Done', 'Closed']])
                report.append(f"- {category}: {len(issues)} issues ({resolved} resolved)")
            report.append("")
        
        # Stuck issues
        if sprint['stuck_issues']:
            report.append("**Stuck Issues:**")
            for issue in sprint['stuck_issues'][:5]:
                report.append(f"- {issue['key']}: {issue['summary'][:70]} ({issue['status']})")
            if len(sprint['stuck_issues']) > 5:
                report.append(f"- ...and {len(sprint['stuck_issues']) - 5} more")
            report.append("")
    
    # Write report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print(f"Sprint-over-sprint report generated: {output_path}")

if __name__ == '__main__':
    import sys
    
    json_path = Path(__file__).parent / 'jira-analysis-data.json'
    csv_path = 'RUDIS-JIRA.csv'
    output_path = Path(__file__).parent / 'RUDIS-Sprint-Analysis.md'
    
    if len(sys.argv) > 1:
        json_path = Path(sys.argv[1])
    if len(sys.argv) > 2:
        csv_path = sys.argv[2]
    if len(sys.argv) > 3:
        output_path = Path(sys.argv[3])
    
    generate_sprint_report(str(json_path), csv_path, str(output_path))

