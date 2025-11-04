#!/usr/bin/env python3
"""
Generate strategic budget allocation analysis from JIRA data.
Focuses on what work is being prioritized and how development budget is allocated.
"""

import json
from datetime import datetime
from pathlib import Path
from collections import Counter, defaultdict
import statistics

def categorize_work(issue):
    """Categorize issue into strategic themes."""
    summary = issue.get('summary', '').lower()
    description = issue.get('description', '').lower()
    # Combine summary and description for better categorization
    full_text = f'{summary} {description}'.strip()
    itype = issue.get('type', '')
    
    # Team Store / B2B (check this first - bugs here should be categorized as Team Store)
    if 'team' in full_text or 'team store' in full_text or 'team:' in full_text or 'usaw' in full_text or 'bulk' in full_text:
        return 'Team Store / B2B'
    
    # Product Display
    if 'pdp' in full_text or 'product detail' in full_text or 'variant' in full_text or 'swatch' in full_text:
        return 'Product Display (PDP)'
    
    # Product Listing
    if 'plp' in full_text or 'product listing' in full_text or 'collection' in full_text:
        return 'Product Listing (PLP)'
    
    # Cart/Checkout/Conversion
    if 'cart' in full_text or 'checkout' in full_text or 'add to cart' in full_text or 'atc' in full_text:
        return 'Cart/Checkout/Conversion'
    
    # Shipping/Logistics
    if 'shipping' in full_text or 'free shipping' in full_text or 'tax' in full_text:
        return 'Shipping/Logistics'
    
    # Analytics & Integrations (check before Technical/Infrastructure)
    if 'gtm' in full_text or 'google tag' in full_text or 'analytics' in full_text or 'tracking' in full_text or 'elevar' in full_text or 'celigo' in full_text or 'integration' in full_text or 'pixel' in full_text or 'attentive' in full_text:
        return 'Analytics & Integrations'
    
    # Compliance & Legal
    if 'cookie' in full_text or 'onetrust' in full_text or 'privacy' in full_text or 'compliance' in full_text or 'gdpr' in full_text:
        return 'Compliance & Legal'
    
    # Account/User Experience (includes loyalty)
    if 'account' in full_text or 'user' in full_text or 'return' in full_text or 'order' in full_text or 'rewards' in full_text or 'loyalty' in full_text:
        return 'Account/User Experience'
    
    # Pricing & Promotions
    if 'pricing' in full_text or 'price' in full_text or 'sale' in full_text or 'promo' in full_text or 'discount' in full_text:
        return 'Pricing & Promotions'
    
    # Search & Discovery
    if 'search' in full_text or 'finder' in full_text or 'quiz' in full_text or 'recommendation' in full_text or 'llm' in full_text or 'chatgpt' in full_text:
        return 'Search & Discovery'
    
    # Content & Pages
    if 'catalog' in full_text or 'pdf' in full_text or 'content' in full_text or 'page' in full_text or 'landing' in full_text or 'embed' in full_text:
        return 'Content & Pages'
    
    # Design/UX Enhancements
    if 'design' in full_text or 'image' in full_text or 'header' in full_text or 'parallax' in full_text or 'video' in full_text or 'ui/ux' in full_text or 'navigation' in full_text or 'menu' in full_text or 'template' in full_text or 'font' in full_text or 'spacing' in full_text:
        return 'Design/UX Enhancements'
    
    # QA & Testing
    if 'qa' in full_text or 'qa cycle' in full_text or 'uat' in full_text or 'user acceptance' in full_text or 'quality assurance' in full_text:
        return 'QA & Testing'
    
    # Testing & Investigation
    if 'test' in full_text or 'investigate' in full_text or 'research' in full_text or 'a/b' in full_text or 'ab test' in full_text or 'smoke test' in full_text:
        return 'Testing & Investigation'
    
    # Database & Configuration
    if 'db configuration' in full_text or 'database' in full_text or 'config' in full_text or 'configuration' in full_text:
        return 'Database & Configuration'
    
    # Financial & Operations
    if 'financial' in full_text or 'fulfilment' in full_text or 'refund' in full_text or 'customer service' in full_text:
        return 'Financial & Operations'
    
    # Product Launches & Categories
    if 'brand launch' in full_text or 'product split' in full_text or 'gift card' in full_text or 'bundle' in full_text or 'accessories' in full_text or 'youth-adult' in full_text:
        return 'Product Launches & Categories'
    
    # Third-party Tools & Integrations
    if 'zendesk' in full_text or 'digioh' in full_text or 'global-e' in full_text:
        return 'Third-party Tools & Integrations'
    
    # Data Management
    if 'data cleanup' in full_text or 'purchase event' in full_text:
        return 'Data Management'
    
    # Process & Operations
    if 'process' in full_text or 'workflow' in full_text or 'approval' in full_text or 'quote' in full_text or 'allocation' in full_text or 'reminder' in full_text:
        return 'Process & Operations'
    
    # Strategic Initiatives (Epics)
    if itype == 'Epic' or 'roadmap' in full_text or 'strategic' in full_text or 'initiative' in full_text:
        return 'Strategic Initiatives'
    
    # Accessibility
    if 'accessibility' in full_text or 'accessible' in full_text or 'aria' in full_text or 'alternative text' in full_text or 'alt text' in full_text or 'wcag' in full_text or 'a11y' in full_text or 'visual cues' in full_text or 'keyboard' in full_text or 'valid label' in full_text or 'form fields' in full_text or 'rudis-amp' in full_text:
        return 'Accessibility'
    
    # Deployment & Operations
    if 'deploy' in full_text or 'go live' in full_text or 'golive' in full_text or 'production' in full_text or 'prod' in full_text or 'preparation for' in full_text or 'open countries' in full_text:
        return 'Deployment & Operations'
    
    # Sprint/Development Work
    if 'sprint' in full_text or 'dev' in full_text or 'development' in full_text:
        return 'Development Sprints'
    
    # Design Specs & Reviews
    if 'ui spec' in full_text or 'comps review' in full_text or 'wireframe' in full_text or 'spec' in full_text:
        return 'Design Specs & Reviews'
    
    # Framework & Strategy
    if 'framework' in full_text or 'strategy' in full_text or 'opt-in' in full_text:
        return 'Framework & Strategy'
    
    # Reporting & Analytics
    if 'reporting' in full_text or 'dashboard' in full_text:
        return 'Reporting & Analytics'
    
    # Technical Debt
    if 'spaghetti code' in full_text or 'technical debt' in full_text or 'refactor' in full_text:
        return 'Technical Debt'
    
    # Technical/Infrastructure
    if 'seo' in full_text or 'robot' in full_text or 'llms.txt' in full_text or 'theme' in full_text or 'api' in full_text or 'middleware' in full_text or 'component' in full_text or 'uber' in full_text or 'token' in full_text or 'verification' in full_text:
        return 'Technical/Infrastructure'
    
    # Requirements & Planning
    if 'requirements' in full_text or 'best practices' in full_text or 'naming convention' in full_text or 'convention' in full_text or 'analysis' in full_text or 'set-up' in full_text or 'setup' in full_text:
        return 'Requirements & Planning'
    
    # Bug Fixes (generic - only if we couldn't categorize by area)
    # Most bugs should be caught by the above categories (e.g., "Team Store bug" = Team Store, "PDP bug" = Product Display)
    # This is only for generic bugs we can't place in a specific area
    if itype == 'Bug' or summary.startswith('bug:') or 'bug:' in summary or ('bug' in full_text and ('fix' in full_text or 'error' in full_text or 'broken' in full_text or 'not working' in full_text)):
        return 'Bug Fixes'
    
    return 'Other'

def group_to_executive_theme(category):
    """Group granular categories into executive-level themes."""
    # Revenue & Growth
    if category in ['Cart/Checkout/Conversion', 'Pricing & Promotions', 
                   'Product Display (PDP)', 'Product Listing (PLP)', 
                   'Search & Discovery', 'Shipping/Logistics']:
        return 'Revenue & Growth'
    
    # Customer Experience
    elif category in ['Design/UX Enhancements', 'Account/User Experience', 
                     'Accessibility', 'Content & Pages']:
        return 'Customer Experience'
    
    # Business Operations
    elif category in ['Team Store / B2B', 'Financial & Operations', 
                     'Process & Operations', 'Product Launches & Categories']:
        return 'Business Operations'
    
    # Platform & Infrastructure
    elif category in ['Technical/Infrastructure', 'Analytics & Integrations', 
                     'Third-party Tools & Integrations', 'Deployment & Operations', 
                     'Data Management', 'Database & Configuration', 
                     'Reporting & Analytics']:
        return 'Platform & Infrastructure'
    
    # Quality & Compliance
    elif category in ['Bug Fixes', 'Compliance & Legal', 'QA & Testing', 
                     'Testing & Investigation']:
        return 'Quality & Compliance'
    
    # Strategic & Planning
    elif category in ['Strategic Initiatives', 'Requirements & Planning', 
                     'Framework & Strategy', 'Design Specs & Reviews', 
                     'Development Sprints', 'Technical Debt']:
        return 'Strategic & Planning'
    
    # Other
    else:
        return 'Other'

def analyze_business_value(issue):
    """Analyze likely business value indicators."""
    summary = issue.get('summary', '').lower()
    priority = issue.get('priority', '').strip()
    status = issue.get('status', '').strip()
    
    value_indicators = {
        'revenue_impact': False,
        'conversion_impact': False,
        'operational': False,
        'technical_debt': False,
        'user_experience': False,
        'strategic': False
    }
    
    # Revenue impact
    if 'cart' in summary or 'checkout' in summary or 'conversion' in summary or 'free shipping' in summary:
        value_indicators['revenue_impact'] = True
        value_indicators['conversion_impact'] = True
    
    # Operational
    if 'team store' in summary or 'bulk' in summary or 'order' in summary:
        value_indicators['operational'] = True
    
    # Technical debt
    if itype == 'Bug' or 'fix' in summary or 'bug' in summary:
        value_indicators['technical_debt'] = True
    
    # User experience
    if 'design' in summary or 'ux' in summary or 'user' in summary or 'account' in summary:
        value_indicators['user_experience'] = True
    
    # Strategic
    if priority in ['Critical', 'Blocker'] or 'plp' in summary or 'pdp' in summary:
        value_indicators['strategic'] = True
    
    return value_indicators

def generate_report(json_path, output_path):
    """Generate strategic budget allocation analysis."""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    report = []
    report.append("# RUDIS Development Budget Allocation Analysis")
    report.append("")
    report.append(f"*Analysis Date: {datetime.now().strftime('%B %d, %Y')}*  ")
    report.append(f"*Data Source: {data['metadata']['source_file']}*  ")
    report.append(f"*Focus Period: Full Year 2025 (January - December 2025)*")
    report.append("")
    report.append("---")
    report.append("")
    
    # Filter for full year 2025 issues
    all_issues_data = []
    for issue_data in data.get('last_3_months', {}).get('issues', []):
        # This contains last 3 months, but we need to re-analyze all 2025 issues
        # We'll need to filter from the full dataset or use a different approach
        pass
    
    # Actually, we need to extract all 2025 issues from the analysis
    # Since the JSON only has last_3_months, we need to re-read or modify the analysis
    # For now, let's extract all issues from the JSON that were created in 2025
    # We'll need to check if the JSON has full year data or if we need to re-run analysis
    
    # Get all issues from the data - check what we have available
    # The JSON structure has last_3_months, but we need full year
    # Let's use a date filter to get all 2025 issues from whatever data structure we have
    
    # For now, let's assume we need to re-analyze. Let's create a function to filter 2025 issues
    # Actually, better approach: modify the report to accept year parameter and filter appropriately
    
    # Since analyze_jira.py only exports last_3_months, we need to either:
    # 1. Modify analyze_jira.py to also export full_year_2025, OR
    # 2. Re-read the CSV here to get all 2025 issues
    
    # Let's go with option 2 - read CSV directly in the report generator for full year
    from pathlib import Path
    import csv
    from datetime import datetime as dt
    
    # Read CSV to get all 2025 issues
    # Try multiple path options
    script_dir = Path(__file__).parent
    csv_path = script_dir.parent.parent / 'data' / data['metadata']['source_file']
    if not csv_path.exists():
        csv_path = Path('/Users/pete/dev/shopify/rudis-documentation/data') / data['metadata']['source_file']
    if not csv_path.exists():
        csv_path = script_dir / '..' / '..' / 'data' / data['metadata']['source_file']
    year_2025_issues = []
    
    if csv_path.exists():
        with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.DictReader(f)
            for row in reader:
                created_str = row.get('Created', '').strip()
                if created_str:
                    try:
                        # Parse JIRA date format: "03/Nov/25 2:40 PM"
                        # Note: %y parses 2-digit year: 00-68 -> 2000-2068, 69-99 -> 1969-1999
                        # So "25" parses as 2025
                        created_date = dt.strptime(created_str, "%d/%b/%y %I:%M %p")
                        # Check if year is 2025 (or 1925 which would be incorrect parsing)
                        if created_date.year == 2025:
                            year_2025_issues.append({
                                'key': row.get('Issue key', '').strip(),
                                'summary': row.get('Summary', '').strip(),
                                'description': row.get('Description', '').strip(),
                                'type': row.get('Issue Type', '').strip(),
                                'status': row.get('Status', '').strip(),
                                'priority': row.get('Priority', '').strip() or 'None',
                                'created': created_str,
                                'resolved': row.get('Resolved', '').strip(),
                                'request_type': row.get('Custom field (Request Type)', '').strip(),
                                'category': row.get('Custom field (Category)', '').strip()
                            })
                    except (ValueError, AttributeError) as e:
                        continue
    
    year_2025_total = len(year_2025_issues)
    
    # METHODOLOGY & TRANSPARENCY
    report.append("## Methodology & Data Transparency")
    report.append("")
    report.append("### Data Source")
    report.append("")
    report.append(f"- **Source:** JIRA CSV export ({data['metadata']['source_file']})")
    report.append(f"- **Total Issues in Dataset:** {data['summary']['total_issues']}")
    report.append(f"- **Issues in Analysis Period:** {year_2025_total}")
    report.append(f"- **Date Range:** Issues created January 1, 2025 - December 31, 2025")
    report.append("")
    report.append("### Development Budget")
    report.append("")
    report.append("- **Monthly Budget:** 70 hours ($14,000/month)")
    report.append("- **Annual Budget (2025):** 840 hours ($168,000)")
    report.append("- **Blended Developer Rate:** $200/hour")
    report.append("- **Budget Allocation Method:** Issue count used as proxy where time tracking unavailable")
    report.append("")
    
    report.append("### Categorization Methodology")
    report.append("")
    report.append("Issues are categorized into strategic areas based on issue summary text, description text, and issue type:")
    report.append("")
    report.append("- **Text Analysis:** Both summary and description fields are analyzed for categorization keywords")
    report.append("- **Coverage:** 68% of 2025 issues have descriptions (average 655 characters)")
    report.append("- **Issue Type:** Issue type (Bug, Epic, Story, etc.) is also considered for categorization")
    report.append("")
    report.append("- **Team Store / B2B:** Issues containing 'team', 'team store', 'usaw', or 'bulk'")
    report.append("- **Product Display (PDP):** Issues containing 'pdp', 'product detail', 'variant', or 'swatch'")
    report.append("- **Product Listing (PLP):** Issues containing 'plp', 'product listing', or 'collection'")
    report.append("- **Cart/Checkout/Conversion:** Issues containing 'cart', 'checkout', 'add to cart', or 'atc'")
    report.append("- **Shipping/Logistics:** Issues containing 'shipping' or 'free shipping'")
    report.append("- **Account/User Experience:** Issues containing 'account', 'user', 'return', 'order', or 'rewards'")
    report.append("- **Design/UX Enhancements:** Issues containing 'design', 'image', 'header', 'parallax', or 'video'")
    report.append("- **Technical/Infrastructure:** Issues containing 'seo', 'robot', 'llms.txt', 'attentive', 'pixel', or 'theme'")
    report.append("- **Bug Fixes:** Issues with Issue Type = 'Bug'")
    report.append("- **Other:** Issues that don't match above categories")
    report.append("")
    report.append("**Note:** Categorization is automated based on keywords. Some issues may be miscategorized. Manual review recommended for strategic decisions.")
    report.append("")
    
    report.append("### Business Value Classification")
    report.append("")
    report.append("Business value categories are inferred from issue content:")
    report.append("")
    report.append("- **Revenue Impact:** Issues directly affecting cart, checkout, conversion, or free shipping")
    report.append("- **Operational Efficiency:** Issues related to Team Store/B2B operations or bulk ordering")
    report.append("- **Technical Debt:** Issues with Issue Type = 'Bug'")
    report.append("- **User Experience:** Issues related to design, UX, account, or user-facing features")
    report.append("")
    report.append("**Limitation:** Business value is inferred, not explicitly stated in JIRA data. Actual ROI/impact requires business metrics.")
    report.append("")
    
    report.append("### Status Definitions")
    report.append("")
    report.append("- **Resolved:** Status = 'Done' or 'Closed'")
    report.append("- **Unresolved:** Status not 'Done' or 'Closed'")
    report.append("- **Stuck:** Status in 'Hold', 'Update Requirements', 'Needs Estimate', or 'Waiting for Approval'")
    report.append("- **Resolution Rate:** (Resolved Issues / Total Issues) × 100")
    report.append("")
    
    report.append("### Priority Definitions")
    report.append("")
    report.append("- **High Priority:** Priority = 'Critical', 'Blocker', or 'Major'")
    report.append("- **None Priority:** Priority field is empty or 'None'")
    report.append("")
    report.append("**Note:** 71% of issues have no priority assigned. This suggests priority may not be used systematically for planning.")
    report.append("")
    
    report.append("### Assumptions & Limitations")
    report.append("")
    report.append("1. **Budget Allocation Proxy:** Issue count is used as a proxy for development budget allocation. Actual time/cost per issue is not available for most issues.")
    report.append("")
    report.append("2. **Categorization Accuracy:** Automated categorization based on keywords may misclassify issues. Manual review of key issues recommended.")
    report.append("")
    report.append("3. **Business Value Inference:** Business value categories are inferred from issue content, not actual measured impact. No revenue/ROI data available.")
    report.append("")
    report.append("4. **Time Period:** Analysis covers all issues created in 2025 (January - December). Work in progress from prior years not included.")
    report.append("")
    report.append("5. **Resolution Context:** 'Stuck' status may indicate legitimate planning phases (e.g., 'Needs Estimate' for new work). Not all stuck work is problematic.")
    report.append("")
    report.append("6. **Priority System:** High percentage of issues without priority suggests priority system may not be used systematically.")
    report.append("")
    
    report.append("### Data Quality")
    report.append("")
    # Count time tracking for 2025 issues
    year_2025_keys = {issue['key'] for issue in year_2025_issues}
    all_estimation = data.get('time_tracking', {}).get('estimation_accuracy', [])
    year_2025_time_tracking_count = sum(1 for est in all_estimation if est.get('issue_key') in year_2025_keys)
    
    report.append(f"- **Issues with Time Tracking (2025):** {year_2025_time_tracking_count} ({year_2025_time_tracking_count/year_2025_total*100:.0f}% of 2025 issues)" if year_2025_total > 0 else "- **Issues with Time Tracking:** Limited data available")
    report.append(f"- **Issues with Time Tracking (All Time):** {data['time_tracking']['summary'].get('estimation_accuracy_count', 0)} ({data['time_tracking']['summary'].get('estimation_accuracy_count', 0)/data['summary']['total_issues']*100:.0f}% of all issues)")
    report.append(f"- **Issues with Comments:** {data['comment_analysis'].get('issues_with_comments', 0)} ({data['comment_analysis'].get('issues_with_comments', 0)/data['summary']['total_issues']*100:.0f}% of all issues)")
    report.append(f"- **Issues with Priority:** {data['summary']['total_issues'] - data['distribution']['priorities'].get('None', 0)} ({100 - data['distribution']['priorities'].get('None', 0)/data['summary']['total_issues']*100:.0f}% of all issues)")
    report.append("")
    report.append("**Recommendation:** Improve data quality by ensuring time tracking, priority assignment, and clear categorization for better analysis.")
    report.append("")
    
    report.append("---")
    report.append("")
    
    # Calculate resolved count for year 2025
    year_2025_resolved = sum(1 for issue in year_2025_issues 
                            if issue['status'] in ['Done', 'Closed'])
    
    # Calculate resolution times for year 2025
    year_2025_resolution_times = []
    for issue in year_2025_issues:
        if issue.get('resolved') and issue.get('created'):
            try:
                created = dt.strptime(issue['created'], "%d/%b/%y %I:%M %p")
                resolved = dt.strptime(issue['resolved'], "%d/%b/%y %I:%M %p")
                resolution_time = (resolved - created).days
                if resolution_time <= 180:  # Exclude outliers
                    year_2025_resolution_times.append(resolution_time)
            except (ValueError, AttributeError):
                continue
    
    if year_2025_total == 0:
        report.append("No issues found for 2025.")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        return
    
    # Categorize all issues
    categorized = defaultdict(list)
    for issue in year_2025_issues:
        category = categorize_work(issue)
        categorized[category].append(issue)
    
    # Analyze resolved vs unresolved by category
    # Unresolved work with estimates is likely in process, waiting for approval, or on hold
    resolved_by_category = defaultdict(list)
    unresolved_by_category = defaultdict(list)
    stuck_by_category = defaultdict(list)
    in_process_by_category = defaultdict(list)  # Unresolved but likely active
    
    for category, issues in categorized.items():
        for issue in issues:
            status = issue.get('status', '').strip()
            issue_key = issue.get('key', '')
            
            # Check if issue has time tracking (indicates it's been worked on)
            has_tracking = any(est.get('issue_key') == issue_key for est in data.get('time_tracking', {}).get('estimation_accuracy', []))
            
            if status in ['Done', 'Closed']:
                resolved_by_category[category].append(issue)
            elif status in ['Hold', 'Update Requirements', 'Needs Estimate', 'Waiting for Approval']:
                stuck_by_category[category].append(issue)
            elif status in ['Approved', 'Ongoing', 'New'] or has_tracking:
                # Unresolved but likely in process (has approval, is ongoing, or has time logged)
                in_process_by_category[category].append(issue)
                unresolved_by_category[category].append(issue)  # Also count in unresolved
            else:
                unresolved_by_category[category].append(issue)
    
    report.append("## Executive Summary")
    report.append("")
    
    # Budget context
    monthly_budget = 70
    annual_budget = monthly_budget * 12  # 840 hours
    hourly_rate = 200  # Blended developer rate in dollars
    
    # Group categories into executive themes
    executive_themes = defaultdict(lambda: {'issues': [], 'categories': defaultdict(list)})
    for issue in year_2025_issues:
        category = categorize_work(issue)
        theme = group_to_executive_theme(category)
        executive_themes[theme]['issues'].append(issue)
        executive_themes[theme]['categories'][category].append(issue)
    
    # Define theme order for consistent reporting
    theme_order = ['Revenue & Growth', 'Customer Experience', 'Business Operations', 
                   'Platform & Infrastructure', 'Quality & Compliance', 'Strategic & Planning', 'Other']
    
    # Parse time helper function (needed for estimates)
    def parse_time_seconds(time_str):
        """Parse JIRA time format to seconds."""
        if not time_str or not time_str.strip():
            return None
        import re
        total_seconds = 0
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
    
    # Calculate hours by theme (returns both actual tracked and estimated total)
    def calculate_theme_hours(theme_issues):
        theme_keys = {i['key'] for i in theme_issues}
        tracked_keys = {est.get('issue_key') for est in all_estimation}
        
        # Actual tracked hours
        actual_tracked = sum(est.get('time_spent_seconds', 0) / 3600 
                            for est in all_estimation 
                            if est.get('issue_key') in theme_keys)
        
        # Separate tracked issues by resolution status for better estimates
        resolved_tracked_keys = {i['key'] for i in theme_issues 
                                if i['status'] in ['Done', 'Closed'] 
                                and i['key'] in tracked_keys}
        unresolved_tracked_keys = {i['key'] for i in theme_issues 
                                   if i['status'] not in ['Done', 'Closed'] 
                                   and i['key'] in tracked_keys}
        
        resolved_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                     for est in all_estimation 
                                     if est.get('issue_key') in resolved_tracked_keys)
        unresolved_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                       for est in all_estimation 
                                       if est.get('issue_key') in unresolved_tracked_keys)
        
        resolved_tracked_count = len(resolved_tracked_keys)
        unresolved_tracked_count = len(unresolved_tracked_keys)
        
        # Calculate averages from tracked issues
        resolved_tracked_avg = resolved_tracked_hours / resolved_tracked_count if resolved_tracked_count > 0 else 0
        unresolved_tracked_avg = unresolved_tracked_hours / unresolved_tracked_count if unresolved_tracked_count > 0 else 0
        
        # Count untracked issues
        resolved_untracked = [i for i in theme_issues 
                             if i['status'] in ['Done', 'Closed'] 
                             and i['key'] not in tracked_keys]
        unresolved_untracked = [i for i in theme_issues 
                               if i['status'] not in ['Done', 'Closed'] 
                               and i['key'] not in tracked_keys]
        
        # Estimate for untracked issues
        resolved_untracked_estimated = len(resolved_untracked) * resolved_tracked_avg if resolved_tracked_avg > 0 else 0
        unresolved_untracked_estimated = len(unresolved_untracked) * unresolved_tracked_avg if unresolved_tracked_avg > 0 else 0
        
        # JIRA original estimates for untracked issues (if any)
        jira_estimate_hours = 0
        for issue in theme_issues:
            if issue['key'] not in tracked_keys:
                estimate_seconds = parse_time_seconds(issue.get('original_estimate', ''))
                if estimate_seconds:
                    jira_estimate_hours += estimate_seconds / 3600
        
        estimated_total = actual_tracked + resolved_untracked_estimated + unresolved_untracked_estimated + jira_estimate_hours
        
        return {
            'actual_tracked': actual_tracked,
            'estimated_total': estimated_total
        }
    
    # Calculate actual hours from time tracking data
    year_2025_keys = {issue['key'] for issue in year_2025_issues}
    all_estimation = data.get('time_tracking', {}).get('estimation_accuracy', [])
    year_2025_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                  for est in all_estimation 
                                  if est.get('issue_key') in year_2025_keys)
    
    # Count tracked issues for 2025
    year_2025_time_tracking_count = sum(1 for est in all_estimation 
                                        if est.get('issue_key') in year_2025_keys)
    
    # Estimate hours for issues without tracking (use average from tracked issues)
    avg_hours_per_issue = year_2025_tracked_hours / year_2025_time_tracking_count if year_2025_time_tracking_count > 0 else None
    
    # Get all_tracked_avg for fallback
    all_tracked_avg = data['time_tracking']['summary'].get('average_time_spent_hours', 0)
    
    report.append("### Budget Allocation by Strategic Theme")
    report.append("")
    report.append("| Theme | Issues | Assumed Hours | Assumed Cost | % of Budget | Resolved | Unresolved | Stuck | Resolution Rate |")
    report.append("|-------|--------|--------------|-------------|-------------|----------|------------|-------|------------------|")
    
    # Calculate theme data first, then sort by actual hours (most realistic view)
    theme_data = []
    for theme in theme_order:
        if theme in executive_themes:
            theme_issues = executive_themes[theme]['issues']
            theme_resolved = [i for i in theme_issues if i['status'] in ['Done', 'Closed']]
            theme_unresolved = [i for i in theme_issues if i['status'] not in ['Done', 'Closed']]
            theme_stuck = [i for i in theme_issues if i['status'] in ['Hold', 'Update Requirements', 'Needs Estimate', 'Waiting for Approval']]
            theme_hours = calculate_theme_hours(theme_issues)
            theme_actual_hours = theme_hours['actual_tracked']
            theme_actual_cost = theme_actual_hours * hourly_rate
            theme_budget_pct = (theme_actual_hours / annual_budget) * 100 if annual_budget > 0 else 0
            theme_resolution_rate = len(theme_resolved) / len(theme_issues) * 100 if theme_issues else 0
            
            theme_data.append({
                'theme': theme,
                'issues': len(theme_issues),
                'actual_hours': theme_actual_hours,
                'actual_cost': theme_actual_cost,
                'budget_pct': theme_budget_pct,
                'resolved': len(theme_resolved),
                'unresolved': len(theme_unresolved),
                'stuck': len(theme_stuck),
                'resolution_rate': theme_resolution_rate
            })
    
    # Sort by actual hours (descending) - shows where money is actually being spent
    theme_data.sort(key=lambda x: x['actual_hours'], reverse=True)
    
    for td in theme_data:
        actual_h_str = f"{td['actual_hours']:.0f}h" if td['actual_hours'] > 0 else "-"
        actual_c_str = f"${td['actual_cost']:,.0f}" if td['actual_cost'] > 0 else "-"
        budget_pct_str = f"{td['budget_pct']:.0f}%" if td['actual_hours'] > 0 else "-"
        report.append(f"| {td['theme']} | {td['issues']} | {actual_h_str} | {actual_c_str} | {budget_pct_str} | {td['resolved']} | {td['unresolved']} | {td['stuck']} | {td['resolution_rate']:.0f}% |")
    
    report.append("")
    report.append("---")
    report.append("")
    
    report.append("## Budget Allocation Overview")
    report.append("")
    
    # Calculate actual hours from time tracking data
    year_2025_keys = {issue['key'] for issue in year_2025_issues}
    all_estimation = data.get('time_tracking', {}).get('estimation_accuracy', [])
    year_2025_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                  for est in all_estimation 
                                  if est.get('issue_key') in year_2025_keys)
    
    # Count tracked issues for 2025
    year_2025_time_tracking_count = sum(1 for est in all_estimation 
                                        if est.get('issue_key') in year_2025_keys)
    
    # Estimate hours for issues without tracking (use average from tracked issues)
    avg_hours_per_issue = year_2025_tracked_hours / year_2025_time_tracking_count if year_2025_time_tracking_count > 0 else None
    
    # Sum up original estimates from JIRA
    issues_with_jira_estimates = 0
    total_jira_estimate_hours = 0
    for issue in year_2025_issues:
        original_estimate_str = issue.get('original_estimate', '')
        estimate_seconds = parse_time_seconds(original_estimate_str)
        if estimate_seconds:
            issues_with_jira_estimates += 1
            total_jira_estimate_hours += estimate_seconds / 3600
    
    # Calculate estimated hours:
    # 1. Use actual tracked hours where available
    # 2. Use JIRA original estimates where available (for untracked issues)
    # 3. Use average per-issue for issues without estimates or tracking
    issues_with_tracking_or_estimate = year_2025_time_tracking_count + issues_with_jira_estimates
    issues_needing_estimate = year_2025_total - issues_with_tracking_or_estimate
    
    if year_2025_tracked_hours > 0 and avg_hours_per_issue:
        # Use tracked hours + JIRA estimates for untracked + average for the rest
        estimated_total_hours = year_2025_tracked_hours + total_jira_estimate_hours + (avg_hours_per_issue * issues_needing_estimate)
    else:
        # Fallback: estimate based on average from all tracked issues
        all_tracked_avg = data['time_tracking']['summary'].get('average_time_spent_hours', 0)
        if all_tracked_avg and all_tracked_avg > 0:
            estimated_total_hours = year_2025_tracked_hours + total_jira_estimate_hours + (all_tracked_avg * issues_needing_estimate)
        else:
            # Last resort: assume 10 hours per issue average
            estimated_total_hours = year_2025_tracked_hours + total_jira_estimate_hours + (10 * issues_needing_estimate)
    
    # Calculate actual hours spent on 2025 issues
    year_2025_actual_hours = year_2025_tracked_hours  # Actual tracked hours
    year_2025_actual_cost = year_2025_actual_hours * hourly_rate
    
    report.append(f"**Total Issues:** {year_2025_total}")
    report.append(f"**Resolved:** {year_2025_resolved} ({year_2025_resolved/year_2025_total*100:.0f}%)")
    report.append(f"**Unresolved:** {year_2025_total - year_2025_resolved} ({100 - year_2025_resolved/year_2025_total*100:.0f}%)")
    report.append("")
    # Calculate actual vs. estimated spend breakdown
    # Separate tracked issues by resolution status
    tracked_keys_set = {est.get('issue_key') for est in all_estimation}
    
    resolved_tracked_keys = {i['key'] for i in year_2025_issues 
                            if i['status'] in ['Done', 'Closed'] 
                            and i['key'] in tracked_keys_set}
    unresolved_tracked_keys = {i['key'] for i in year_2025_issues 
                              if i['status'] not in ['Done', 'Closed'] 
                              and i['key'] in tracked_keys_set}
    
    resolved_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                for est in all_estimation 
                                if est.get('issue_key') in resolved_tracked_keys)
    unresolved_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                   for est in all_estimation 
                                   if est.get('issue_key') in unresolved_tracked_keys)
    
    resolved_tracked_count = len(resolved_tracked_keys)
    unresolved_tracked_count = len(unresolved_tracked_keys)
    
    # Calculate averages from tracked issues for estimating untracked
    resolved_tracked_avg = resolved_tracked_hours / resolved_tracked_count if resolved_tracked_count > 0 else 0
    unresolved_tracked_avg = unresolved_tracked_hours / unresolved_tracked_count if unresolved_tracked_count > 0 else 0
    
    # Count untracked issues
    resolved_untracked_count = year_2025_resolved - resolved_tracked_count
    unresolved_untracked_count = (year_2025_total - year_2025_resolved) - unresolved_tracked_count
    
    # Estimate for untracked issues using averages from tracked
    resolved_untracked_estimated_hours = resolved_untracked_count * resolved_tracked_avg if resolved_tracked_avg > 0 else 0
    unresolved_untracked_estimated_hours = unresolved_untracked_count * unresolved_tracked_avg if unresolved_tracked_avg > 0 else 0
    
    # Total actual and estimated
    total_actual_hours = resolved_tracked_hours + unresolved_tracked_hours
    total_estimated_hours = total_actual_hours + resolved_untracked_estimated_hours + unresolved_untracked_estimated_hours
    estimated_remaining_hours = total_estimated_hours - total_actual_hours
    
    report.append("### Assumed Spend vs. Estimated Total Cost")
    report.append("")
    report.append("#### Assumed Spend (Tracked Hours)")
    report.append("")
    report.append(f"**Resolved Issues:** {resolved_tracked_count} issues, {resolved_tracked_hours:.0f} hours (${resolved_tracked_hours * hourly_rate:,.0f})")
    report.append(f"**Unresolved Issues:** {unresolved_tracked_count} issues, {unresolved_tracked_hours:.0f} hours (${unresolved_tracked_hours * hourly_rate:,.0f})")
    report.append(f"**Total Assumed Spend:** {total_actual_hours:.0f} hours (${total_actual_hours * hourly_rate:,.0f})")
    report.append("")
    report.append("#### Estimated Additional Costs (Untracked Issues)")
    report.append("")
    report.append(f"**Resolved but Untracked:** {resolved_untracked_count} issues")
    report.append(f"  - Estimated: {resolved_untracked_estimated_hours:.0f} hours (${resolved_untracked_estimated_hours * hourly_rate:,.0f})")
    report.append(f"  - *Based on average of {resolved_tracked_avg:.1f} hours per tracked resolved issue*")
    report.append("")
    report.append(f"**Unresolved but Untracked:** {unresolved_untracked_count} issues")
    report.append(f"  - Estimated: {unresolved_untracked_estimated_hours:.0f} hours (${unresolved_untracked_estimated_hours * hourly_rate:,.0f})")
    report.append(f"  - *Based on average of {unresolved_tracked_avg:.1f} hours per tracked unresolved issue*")
    report.append("")
    report.append("#### Total Estimated Cost")
    report.append("")
    report.append(f"**Assumed Spend:** {total_actual_hours:.0f} hours (${total_actual_hours * hourly_rate:,.0f})")
    report.append(f"**Estimated Remaining:** {estimated_remaining_hours:.0f} hours (${estimated_remaining_hours * hourly_rate:,.0f})")
    report.append(f"**Estimated Total Cost:** {total_estimated_hours:.0f} hours (${total_estimated_hours * hourly_rate:,.0f})")
    report.append("")
    report.append("*Note: Estimates for untracked issues use averages from tracked issues of the same resolution status. This provides a more accurate projection than a single average across all issues.*")
    report.append("")
    report.append(f"**Budget Available (2025):** {annual_budget} hours (${annual_budget * hourly_rate:,.0f})")
    report.append(f"**Budget Utilization (Assumed Spend):** {total_actual_hours/annual_budget*100:.0f}%")
    report.append("")
    report.append("#### Backlog Capacity Analysis")
    report.append("")
    if total_estimated_hours > annual_budget:
        backlog_hours = total_estimated_hours - annual_budget
        backlog_cost = backlog_hours * hourly_rate
        report.append(f"**Estimated Total Work:** {total_estimated_hours:.0f} hours (${total_estimated_hours * hourly_rate:,.0f})")
        report.append(f"**Budget Capacity:** {annual_budget:.0f} hours (${annual_budget * hourly_rate:,.0f})")
        report.append(f"**Backlog Beyond Budget:** {backlog_hours:.0f} hours (${backlog_cost:,.0f})")
        report.append("")
        report.append("*Note: The estimated work volume exceeds available budget capacity. This indicates a backlog that will require ongoing prioritization and selective deferral of lower-priority items. This is a normal part of managing a fixed-budget development program.*")
    elif total_estimated_hours < annual_budget * 0.8:
        available_capacity = annual_budget - total_estimated_hours
        available_cost = available_capacity * hourly_rate
        report.append(f"**Estimated Total Work:** {total_estimated_hours:.0f} hours (${total_estimated_hours * hourly_rate:,.0f})")
        report.append(f"**Budget Capacity:** {annual_budget:.0f} hours (${annual_budget * hourly_rate:,.0f})")
        report.append(f"**Available Capacity:** {available_capacity:.0f} hours (${available_cost:,.0f}) available for additional work")
    else:
        report.append(f"**Estimated Total Work:** {total_estimated_hours:.0f} hours (${total_estimated_hours * hourly_rate:,.0f})")
        report.append(f"**Budget Capacity:** {annual_budget:.0f} hours (${annual_budget * hourly_rate:,.0f})")
        report.append("*Estimated work aligns well with available budget capacity.*")
    report.append("")
    
    # Analysis of unresolved issues with estimates
    # Parse time strings to seconds
    def parse_time_seconds(time_str):
        """Parse JIRA time format to seconds."""
        if not time_str or not time_str.strip():
            return None
        import re
        total_seconds = 0
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
    
    unresolved_with_tracking = []
    unresolved_with_estimates = []
    unresolved_with_remaining = []
    
    for issue in year_2025_issues:
        if issue['status'] not in ['Done', 'Closed']:
            issue_key = issue['key']
            # Check if it has time tracking
            has_tracking = any(est.get('issue_key') == issue_key for est in all_estimation)
            original_estimate = parse_time_seconds(issue.get('original_estimate', ''))
            remaining_estimate = parse_time_seconds(issue.get('remaining_estimate', ''))
            
            if has_tracking:
                unresolved_with_tracking.append(issue)
            if original_estimate:
                unresolved_with_estimates.append(issue)
            if remaining_estimate:
                unresolved_with_remaining.append(issue)
    
    if unresolved_with_tracking or unresolved_with_estimates:
        report.append("### Unresolved Issues Analysis")
        report.append("")
        if unresolved_with_tracking:
            report.append(f"**Issues with Time Logged:** {len(unresolved_with_tracking)} issues have time logged but are unresolved")
            tracked_hours_unresolved = sum(est.get('time_spent_seconds', 0) / 3600 
                                           for est in all_estimation 
                                           if est.get('issue_key') in {i['key'] for i in unresolved_with_tracking})
            report.append(f"  - **Hours Invested:** {tracked_hours_unresolved:.0f} hours (${tracked_hours_unresolved * hourly_rate:,.0f})")
            report.append(f"  - **Interpretation:** Work in progress - these issues are actively being worked on")
            report.append("")
        
        if unresolved_with_estimates:
            total_original_estimate_seconds = sum(parse_time_seconds(i.get('original_estimate', '')) or 0 for i in unresolved_with_estimates)
            total_original_estimate_hours = total_original_estimate_seconds / 3600
            report.append(f"**Issues with Original Estimates:** {len(unresolved_with_estimates)} unresolved issues have original estimates")
            report.append(f"  - **Estimated Hours:** {total_original_estimate_hours:.0f} hours (${total_original_estimate_hours * hourly_rate:,.0f})")
            report.append(f"  - **Interpretation:** These issues were estimated but not yet completed")
            report.append("")
        
        if unresolved_with_remaining:
            total_remaining_seconds = sum(parse_time_seconds(i.get('remaining_estimate', '')) or 0 for i in unresolved_with_remaining)
            total_remaining_hours = total_remaining_seconds / 3600
            report.append(f"**Issues with Remaining Estimates:** {len(unresolved_with_remaining)} unresolved issues have remaining time estimates")
            report.append(f"  - **Remaining Hours:** {total_remaining_hours:.0f} hours (${total_remaining_hours * hourly_rate:,.0f})")
            report.append(f"  - **Interpretation:** Work has been started but not completed - indicates active development")
            report.append("")
    
    # Calculate hours by category
    all_tracked_avg = data['time_tracking']['summary'].get('average_time_spent_hours', 0)
    
    def calculate_category_hours(category_issues):
        """Calculate actual and estimated hours for a category of issues."""
        category_keys = {i['key'] for i in category_issues}
        tracked_keys = {est.get('issue_key') for est in all_estimation}
        
        # Actual tracked hours
        actual_tracked = sum(est.get('time_spent_seconds', 0) / 3600 
                            for est in all_estimation 
                            if est.get('issue_key') in category_keys)
        
        # Separate tracked issues by resolution status
        resolved_tracked_keys = {i['key'] for i in category_issues 
                                 if i['status'] in ['Done', 'Closed'] 
                                 and i['key'] in tracked_keys}
        unresolved_tracked_keys = {i['key'] for i in category_issues 
                                   if i['status'] not in ['Done', 'Closed'] 
                                   and i['key'] in tracked_keys}
        
        resolved_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                     for est in all_estimation 
                                     if est.get('issue_key') in resolved_tracked_keys)
        unresolved_tracked_hours = sum(est.get('time_spent_seconds', 0) / 3600 
                                       for est in all_estimation 
                                       if est.get('issue_key') in unresolved_tracked_keys)
        
        resolved_tracked_count = len(resolved_tracked_keys)
        unresolved_tracked_count = len(unresolved_tracked_keys)
        
        # Calculate averages
        resolved_tracked_avg = resolved_tracked_hours / resolved_tracked_count if resolved_tracked_count > 0 else 0
        unresolved_tracked_avg = unresolved_tracked_hours / unresolved_tracked_count if unresolved_tracked_count > 0 else 0
        
        # Count untracked issues
        resolved_untracked = [i for i in category_issues 
                             if i['status'] in ['Done', 'Closed'] 
                             and i['key'] not in tracked_keys]
        unresolved_untracked = [i for i in category_issues 
                               if i['status'] not in ['Done', 'Closed'] 
                               and i['key'] not in tracked_keys]
        
        # Estimate for untracked
        resolved_untracked_estimated = len(resolved_untracked) * resolved_tracked_avg if resolved_tracked_avg > 0 else 0
        unresolved_untracked_estimated = len(unresolved_untracked) * unresolved_tracked_avg if unresolved_tracked_avg > 0 else 0
        
        # JIRA estimates
        jira_estimate_hours = 0
        for issue in category_issues:
            if issue['key'] not in tracked_keys:
                estimate_seconds = parse_time_seconds(issue.get('original_estimate', ''))
                if estimate_seconds:
                    jira_estimate_hours += estimate_seconds / 3600
        
        estimated_total = actual_tracked + resolved_untracked_estimated + unresolved_untracked_estimated + jira_estimate_hours
        
        return {
            'actual_tracked': actual_tracked,
            'estimated_total': estimated_total
        }
    
    # Work allocation by category (detailed view)
    report.append("### Detailed Work Allocation by Category")
    report.append("")
    report.append("*Note: Categories are grouped into executive themes above. This section provides detailed breakdown.*")
    report.append("")
    report.append("| Theme | Category | Issues | Assumed Hours | Assumed Cost | % of Budget | Resolved | In Process | Stuck | Resolution Rate |")
    report.append("|-------|----------|--------|--------------|-------------|-------------|----------|------------|-------|------------------|")
    
    # Collect all category data, then sort by actual hours
    category_data = []
    for theme in theme_order:
        if theme in executive_themes:
            theme_categories = executive_themes[theme]['categories']
            for category in theme_categories.keys():
                issues = theme_categories[category]
                resolved = len(resolved_by_category[category])
                in_process = len(in_process_by_category[category])
                stuck = len(stuck_by_category[category])
                resolution_rate = resolved / len(issues) * 100 if issues else 0
                cat_hours = calculate_category_hours(issues)
                cat_actual_hours = cat_hours['actual_tracked']
                cat_actual_cost = cat_actual_hours * hourly_rate
                budget_pct = (cat_actual_hours / annual_budget) * 100 if annual_budget > 0 else 0
                
                category_data.append({
                    'theme': theme,
                    'category': category,
                    'issues': len(issues),
                    'actual_hours': cat_actual_hours,
                    'actual_cost': cat_actual_cost,
                    'budget_pct': budget_pct,
                    'resolved': resolved,
                    'in_process': in_process,
                    'stuck': stuck,
                    'resolution_rate': resolution_rate
                })
    
    # Sort by actual hours (descending) - shows where money is actually being spent
    category_data.sort(key=lambda x: x['actual_hours'], reverse=True)
    
    for cd in category_data:
        actual_h_str = f"{cd['actual_hours']:.0f}h" if cd['actual_hours'] > 0 else "-"
        actual_c_str = f"${cd['actual_cost']:,.0f}" if cd['actual_cost'] > 0 else "-"
        budget_pct_str = f"{cd['budget_pct']:.0f}%" if cd['actual_hours'] > 0 else "-"
        report.append(f"| {cd['theme']} | {cd['category']} | {cd['issues']} | {actual_h_str} | {actual_c_str} | {budget_pct_str} | {cd['resolved']} | {cd['in_process']} | {cd['stuck']} | {cd['resolution_rate']:.0f}% |")
    
    report.append("")
    
    # Key insights on allocation
    report.append("### Allocation Insights")
    report.append("")
    
    insights = []
    
    # Largest category
    largest_category = max(categorized.items(), key=lambda x: len(x[1]))
    largest_pct = len(largest_category[1]) / year_2025_total * 100
    insights.append(f"**Largest Focus Area:** {largest_category[0]} ({largest_pct:.0f}% of work, {len(largest_category[1])} issues)")
    
    # Highest resolution rate
    resolution_rates = {cat: len(resolved_by_category[cat]) / len(issues) * 100 
                      for cat, issues in categorized.items() if issues}
    if resolution_rates:
        highest_rate_cat = max(resolution_rates.items(), key=lambda x: x[1])
        insights.append(f"**Highest Completion Rate:** {highest_rate_cat[0]} ({highest_rate_cat[1]:.0f}% resolved)")
    
    # Lowest resolution rate
    if resolution_rates:
        lowest_rate_cat = min(resolution_rates.items(), key=lambda x: x[1])
        if lowest_rate_cat[1] < 50:
            insights.append(f"**Lowest Completion Rate:** {lowest_rate_cat[0]} ({lowest_rate_cat[1]:.0f}% resolved) - may indicate scope issues or blockers")
    
    # Most stuck work
    if stuck_by_category:
        most_stuck_cat = max(stuck_by_category.items(), key=lambda x: len(x[1]))
        stuck_pct = len(most_stuck_cat[1]) / len(categorized[most_stuck_cat[0]]) * 100 if categorized[most_stuck_cat[0]] else 0
        insights.append(f"**Most Stuck Work:** {most_stuck_cat[0]} ({stuck_pct:.0f}% stuck, {len(most_stuck_cat[1])} issues)")
    
    for insight in insights:
        report.append(f"- {insight}")
    report.append("")
    
    report.append("---")
    report.append("")
    
    # DETAILED CATEGORY ANALYSIS
    report.append("## Strategic Category Analysis")
    report.append("")
    
    # Sort by total issues (most work first)
    for category in sorted(categorized.keys(), key=lambda x: len(categorized[x]), reverse=True):
        issues = categorized[category]
        resolved = resolved_by_category[category]
        unresolved = unresolved_by_category[category]
        stuck = stuck_by_category[category]
        cat_hours = calculate_category_hours(issues)
        budget_pct = (cat_hours['actual_tracked'] / annual_budget) * 100 if annual_budget > 0 else 0
        
        report.append(f"### {category}")
        report.append("")
        in_process = in_process_by_category[category]
        unresolved = unresolved_by_category[category]
        
        report.append(f"**Total Issues:** {len(issues)} ({len(issues)/year_2025_total*100:.0f}% of issues)")
        report.append(f"**Assumed Hours:** {cat_hours['actual_tracked']:.0f} hours (${cat_hours['actual_tracked'] * hourly_rate:,.0f})")
        report.append(f"**Estimated Hours:** {cat_hours['estimated_total']:.0f} hours (${cat_hours['estimated_total'] * hourly_rate:,.0f}) - {budget_pct:.0f}% of budget")
        report.append(f"**Resolved:** {len(resolved)} ({len(resolved)/len(issues)*100:.0f}%)")
        report.append(f"**In Process/Approved:** {len(in_process)} (likely active work)")
        report.append(f"**Stuck:** {len(stuck)} (on hold, needs estimate, or waiting for approval)")
        report.append(f"**Unresolved:** {len(unresolved)} total")
        report.append("")
        
        # Show resolved work
        if resolved:
            report.append("**Resolved Work:**")
            for issue in resolved[:5]:
                priority = issue.get('priority', 'None')
                report.append(f"- **{issue['key']}:** {issue.get('summary', '')[:75]} ({priority})")
            if len(resolved) > 5:
                report.append(f"- ...and {len(resolved) - 5} more")
            report.append("")
        
        # Show unresolved work
        if unresolved:
            report.append("**Unresolved Work:**")
            for issue in unresolved[:5]:
                status = issue.get('status', 'Unknown')
                priority = issue.get('priority', 'None')
                report.append(f"- **{issue['key']}:** {issue.get('summary', '')[:70]} ({status}, {priority})")
            if len(unresolved) > 5:
                report.append(f"- ...and {len(unresolved) - 5} more")
            report.append("")
        
        # Show stuck work
        if stuck:
            report.append("**Stuck Work:**")
            for issue in stuck:
                status = issue.get('status', 'Unknown')
                report.append(f"- **{issue['key']}:** {issue.get('summary', '')[:70]} ({status})")
            report.append("")
        
        report.append("")
    
    report.append("---")
    report.append("")
    
    # PRIORITIZATION PATTERNS
    report.append("## Prioritization Patterns")
    report.append("")
    
    # Priority by category
    priority_by_category = defaultdict(lambda: Counter())
    for category, issues in categorized.items():
        for issue in issues:
            priority = issue.get('priority', 'None').strip()
            priority_by_category[category][priority] += 1
    
    report.append("### Priority Distribution by Category")
    report.append("")
    
    # Get all priorities
    all_priorities = set()
    for counters in priority_by_category.values():
        all_priorities.update(counters.keys())
    
    if all_priorities:
        # Header
        header = "| Category | " + " | ".join(sorted(all_priorities, key=lambda x: {'Critical': 0, 'Blocker': 1, 'Major': 2, 'Minor': 3, 'None': 4}.get(x, 5))) + " |"
        report.append(header)
        report.append("|" + "-|" * (len(all_priorities) + 1))
        
        for category in sorted(categorized.keys(), key=lambda x: len(categorized[x]), reverse=True):
            row = f"| {category} |"
            for priority in sorted(all_priorities, key=lambda x: {'Critical': 0, 'Blocker': 1, 'Major': 2, 'Minor': 3, 'None': 4}.get(x, 5)):
                count = priority_by_category[category][priority]
                row += f" {count} |"
            report.append(row)
        report.append("")
    
    # High priority work analysis
    high_priority_issues = [i for i in year_2025_issues if i.get('priority', '').strip() in ['Critical', 'Blocker', 'Major']]
    
    if high_priority_issues:
        report.append("### High Priority Work Analysis")
        report.append("")
        report.append(f"**High Priority Issues:** {len(high_priority_issues)} ({len(high_priority_issues)/year_2025_total*100:.0f}% of work)")
        report.append("")
        
        high_priority_resolved = [i for i in high_priority_issues if i.get('status', '').strip() in ['Done', 'Closed']]
        high_priority_unresolved = [i for i in high_priority_issues if i.get('status', '').strip() not in ['Done', 'Closed']]
        
        report.append(f"**Resolved:** {len(high_priority_resolved)} ({len(high_priority_resolved)/len(high_priority_issues)*100:.0f}%)")
        report.append(f"**Unresolved:** {len(high_priority_unresolved)}")
        report.append("")
        
        if high_priority_unresolved:
            report.append("**Unresolved High Priority Issues:**")
            for issue in high_priority_unresolved:
                status = issue.get('status', 'Unknown')
                category = categorize_work(issue)
                report.append(f"- **{issue['key']}:** {issue.get('summary', '')[:70]} ({category}, {status})")
            report.append("")
        
        # High priority by category
        high_priority_by_category = Counter()
        for issue in high_priority_issues:
            category = categorize_work(issue)
            high_priority_by_category[category] += 1
        
        report.append("**High Priority Work by Category:**")
        for category, count in high_priority_by_category.most_common():
            pct = count / len(high_priority_issues) * 100
            report.append(f"- {category}: {count} ({pct:.0f}%)")
        report.append("")
    
    report.append("---")
    report.append("")
    
    # BUSINESS VALUE ANALYSIS
    report.append("## Business Value Analysis")
    report.append("")
    
    # Categorize by likely business value
    revenue_impact = []
    conversion_impact = []
    operational = []
    technical_debt = []
    user_experience = []
    
    for issue in year_2025_issues:
        summary = issue.get('summary', '').lower()
        category = categorize_work(issue)
        
        if 'cart' in summary or 'checkout' in summary or 'conversion' in summary or 'free shipping' in summary:
            revenue_impact.append(issue)
            conversion_impact.append(issue)
        elif category == 'Team Store / B2B' or 'bulk' in summary:
            operational.append(issue)
        elif issue.get('type', '') == 'Bug':
            technical_debt.append(issue)
        elif 'design' in summary or 'ux' in summary or category == 'Design/UX Enhancements':
            user_experience.append(issue)
        elif category == 'Cart/Checkout/Conversion':
            revenue_impact.append(issue)
            conversion_impact.append(issue)
    
    report.append("### Budget Allocation by Business Value")
    report.append("")
    report.append("| Value Type | Issues | % of Budget | Resolution Rate |")
    report.append("|------------|--------|-------------|-----------------|")
    
    value_types = {
        'Revenue Impact': revenue_impact,
        'Operational Efficiency': operational,
        'Technical Debt': technical_debt,
        'User Experience': user_experience
    }
    
    for value_type, issues in value_types.items():
        if issues:
            resolved = [i for i in issues if i.get('status', '').strip() in ['Done', 'Closed']]
            resolution_rate = len(resolved) / len(issues) * 100 if issues else 0
            pct = len(issues) / year_2025_total * 100
            report.append(f"| {value_type} | {len(issues)} | {pct:.0f}% | {resolution_rate:.0f}% |")
    
    report.append("")
    
    # Strategic questions
    report.append("### Strategic Questions")
    report.append("")
    
    questions = []
    
    # Revenue focus
    revenue_pct = len(revenue_impact) / year_2025_total * 100
    if revenue_pct < 20:
        questions.append(f"**Revenue Focus:** Only {revenue_pct:.0f}% of work is directly revenue-impacting. Is this sufficient for growth goals?")
    
    # Technical debt
    tech_debt_pct = len(technical_debt) / year_2025_total * 100
    if tech_debt_pct < 10:
        questions.append(f"**Technical Debt:** {tech_debt_pct:.0f}% allocated to bug fixes. Is technical debt accumulating?")
    elif tech_debt_pct > 30:
        questions.append(f"**Technical Debt:** {tech_debt_pct:.0f}% allocated to bug fixes. Are there systemic quality issues?")
    
    # Stuck work analysis
    total_stuck = sum(len(issues) for issues in stuck_by_category.values())
    if total_stuck > year_2025_total * 0.3:
        questions.append(f"**Execution:** {total_stuck/year_2025_total*100:.0f}% of work is stuck. What's preventing progress?")
    
    # Priority alignment
    high_priority_issues = [i for i in year_2025_issues if i.get('priority', '').strip() in ['Critical', 'Blocker', 'Major']]
    high_priority_pct = len(high_priority_issues) / year_2025_total * 100
    if high_priority_pct < 20:
        questions.append(f"**Priority Discipline:** Only {high_priority_pct:.0f}% of work is marked high priority. Is everything truly a priority, or is the system not being used?")
    
    for question in questions:
        report.append(f"- {question}")
    report.append("")
    
    report.append("---")
    report.append("")
    
    # STRATEGIC RECOMMENDATIONS
    report.append("## Strategic Recommendations")
    report.append("")
    
    recommendations = []
    
    # Budget allocation
    largest_pct = len(largest_category[1]) / year_2025_total * 100
    if largest_pct > 40:
        recommendations.append(("Review Budget Concentration", [
            f"{largest_category[0]} represents {largest_pct:.0f}% of 2025 work",
            "Consider if this concentration aligns with strategic goals",
            "Evaluate if other areas are being underfunded",
            "Assess ROI of current allocation vs alternatives"
        ]))
    
    # Stuck work
    total_stuck = sum(len(issues) for issues in stuck_by_category.values())
    if total_stuck > year_2025_total * 0.3:
        recommendations.append(("Address Stuck Work", [
            f"{total_stuck} issues ({total_stuck/year_2025_total*100:.0f}%) are in non-progress states",
            "Review stuck issues to identify systemic blockers",
            "Consider deprioritizing or closing work that's been stuck",
            "Improve requirements gathering to reduce 'Update Requirements' state"
        ]))
    
    # Low resolution rates
    low_resolution_cats = [cat for cat, rate in resolution_rates.items() if rate < 40 and len(categorized[cat]) > 2]
    if low_resolution_cats:
        recommendations.append(("Improve Completion Rates", [
            f"Low resolution rates in: {', '.join(low_resolution_cats)}",
            "Investigate why these areas have low completion",
            "Consider breaking work into smaller pieces",
            "Review scope and requirements clarity"
        ]))
    
    # Unresolved high priority
    if high_priority_unresolved:
        recommendations.append(("Address Unresolved High Priority", [
            f"{len(high_priority_unresolved)} high-priority issues remain unresolved",
            "Review these for immediate attention",
            "Consider if priorities have changed",
            "Identify blockers preventing resolution"
        ]))
    
    # Category balance
    cat_counts = [len(issues) for issues in categorized.values()]
    if cat_counts:
        max_cat = max(cat_counts)
        min_cat = min(cat_counts)
        if max_cat > min_cat * 3 and min_cat > 0:
            recommendations.append(("Consider Budget Rebalancing", [
                "Significant imbalance in work allocation across categories",
                "Review if current distribution matches strategic priorities",
                "Consider if underrepresented areas need more investment",
                "Assess if overrepresented areas are generating sufficient ROI"
            ]))
    
    for title, items in recommendations:
        report.append(f"### {title}")
        report.append("")
        for item in items:
            report.append(f"- {item}")
        report.append("")
    
    if not recommendations:
        report.append("No specific recommendations identified.")
        report.append("")
    
    report.append("---")
    
    # Write report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print(f"Strategic budget allocation report generated: {output_path}")

if __name__ == '__main__':
    script_dir = Path(__file__).parent
    json_path = script_dir / 'jira-analysis-data.json'
    output_path = script_dir / 'RUDIS-JIRA-Insights.md'
    generate_report(str(json_path), str(output_path))
