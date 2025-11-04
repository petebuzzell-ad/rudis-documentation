#!/usr/bin/env python3
"""
JIRA Data Analysis Script
Analyzes RUDIS JIRA CSV export and outputs structured data for AI analysis.
This script handles data extraction and aggregation; AI handles analysis and report generation.
"""

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import statistics

# Date format: "03/Nov/25 2:40 PM"
DATE_FORMAT = "%d/%b/%y %I:%M %p"
MONTH_NAMES = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

# Threshold for extreme outliers - issues with resolution times > 180 days are likely
# strategic initiatives or work that happened outside JIRA, not typical development work
OUTLIER_THRESHOLD_DAYS = 180


def parse_date(date_str: str) -> Optional[datetime]:
    """Parse JIRA date format to datetime object."""
    if not date_str or date_str.strip() == '':
        return None
    try:
        # Handle format: "03/Nov/25 2:40 PM"
        return datetime.strptime(date_str.strip(), DATE_FORMAT)
    except (ValueError, AttributeError):
        return None


def parse_story_points(points_str: str) -> Optional[float]:
    """Parse story points to float."""
    if not points_str or points_str.strip() == '':
        return None
    try:
        return float(points_str.strip())
    except (ValueError, AttributeError):
        return None


def parse_time_seconds(time_str: str) -> Optional[float]:
    """Parse JIRA time format to seconds (e.g., '2h 30m' or '1d 4h' or seconds as number)."""
    if not time_str or time_str.strip() == '':
        return None
    try:
        # Try direct number first (seconds)
        return float(time_str.strip())
    except (ValueError, AttributeError):
        pass
    
    # Parse time format (e.g., "2h 30m", "1d 4h", "30m")
    time_str = time_str.strip().lower()
    total_seconds = 0.0
    
    # Days
    if 'd' in time_str:
        days_match = re.search(r'(\d+(?:\.\d+)?)\s*d', time_str)
        if days_match:
            total_seconds += float(days_match.group(1)) * 86400
    
    # Hours
    if 'h' in time_str:
        hours_match = re.search(r'(\d+(?:\.\d+)?)\s*h', time_str)
        if hours_match:
            total_seconds += float(hours_match.group(1)) * 3600
    
    # Minutes
    if 'm' in time_str:
        minutes_match = re.search(r'(\d+(?:\.\d+)?)\s*m', time_str)
        if minutes_match:
            total_seconds += float(minutes_match.group(1)) * 60
    
    # Seconds
    if 's' in time_str and 'm' not in time_str:  # Avoid matching 'ms'
        seconds_match = re.search(r'(\d+(?:\.\d+)?)\s*s', time_str)
        if seconds_match:
            total_seconds += float(seconds_match.group(1))
    
    return total_seconds if total_seconds > 0 else None


def parse_comments(row_data: List[str], headers: List[str]) -> List[Dict[str, Any]]:
    """Extract all comment fields from row by index (since multiple Comment columns exist)."""
    comments = []
    # Find all Comment column indices
    comment_indices = [i for i, h in enumerate(headers) if h == 'Comment']
    
    for idx in comment_indices:
        if idx < len(row_data):
            comment = row_data[idx].strip() if row_data[idx] else ''
            if not comment:
                continue
            
            # Parse comment (format: "timestamp;user_id;comment_text" based on JIRA export)
            comment_parts = comment.split(';', 2)
            if len(comment_parts) >= 3:
                comments.append({
                    'timestamp': comment_parts[0].strip(),
                    'user_id': comment_parts[1].strip(),
                    'text': comment_parts[2].strip() if len(comment_parts) > 2 else ''
                })
            elif comment:  # If format is different, just store the text
                comments.append({
                    'text': comment,
                    'timestamp': None,
                    'user_id': None
                })
    
    return comments


def calculate_resolution_time(created: Optional[datetime], resolved: Optional[datetime]) -> Optional[int]:
    """Calculate resolution time in days."""
    if not created or not resolved:
        return None
    delta = resolved - created
    return delta.days


def is_in_last_3_months(date: Optional[datetime]) -> bool:
    """Check if date is in last 3 months (Aug 2025 - Nov 2025)."""
    if not date:
        return False
    # Aug 1, 2025 to Nov 30, 2025
    start = datetime(2025, 8, 1)
    end = datetime(2025, 11, 30, 23, 59, 59)
    return start <= date <= end


def analyze_jira_data(csv_path: str) -> Dict[str, Any]:
    """Main analysis function."""
    results = {
        'total_issues': 0,
        'issue_types': Counter(),
        'statuses': Counter(),
        'priorities': Counter(),
        'request_types': Counter(),
        'teams': Counter(),
        'categories': Counter(),
        'epics': Counter(),
        'assignees': Counter(),
        'reporters': Counter(),
        'story_points': [],
        'resolved_issues': [],
        'resolution_times': [],
        'outlier_issues': [],  # Strategic initiatives/long-running projects
        'last_3_months': {
            'issues': [],
            'issue_types': Counter(),
            'statuses': Counter(),
            'request_types': Counter(),
            'resolved': 0,
            'resolution_times': []
        },
        'challenging_work': [],
        'unresolved_high_priority': [],
        'recent_activity': [],
        'none_priority_analysis': {
            'all_none_priority': [],
            'resolved_none_priority': [],
            'quick_resolution_none': [],  # Resolved in < 7 days
            'very_quick_resolution_none': []  # Resolved in < 3 days
        },
        'priority_comparison': {
            'None': {'count': 0, 'resolution_times': []},
            'Critical': {'count': 0, 'resolution_times': []},
            'Blocker': {'count': 0, 'resolution_times': []},
            'Major': {'count': 0, 'resolution_times': []},
            'Minor': {'count': 0, 'resolution_times': []}
        },
        'time_tracking': {
            'original_estimates': [],  # In seconds
            'remaining_estimates': [],  # In seconds
            'time_spent': [],  # In seconds
            'baseline_estimates': [],  # Story points or time
            'estimation_accuracy': []  # List of {original, actual, ratio, issue_key}
        },
        'comment_analysis': {
            'total_comments': 0,
            'issues_with_comments': 0,
            'comment_counts_per_issue': [],
            'average_comments_per_issue': 0
        }
    }
    
    with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
        # Read headers first to get column positions
        header_line = f.readline()
        headers = next(csv.reader([header_line]))
        reader = csv.reader(f)
        
        # Create a list version for comment parsing
        row_dict = {}
        for i, row in enumerate(reader):
            # Convert row list to dict for easier access to named fields
            if len(row) < len(headers):
                row.extend([''] * (len(headers) - len(row)))
            
            row_dict = dict(zip(headers, row))
            
            # Also keep row as list for comment parsing
            row_list = row
            results['total_issues'] += 1
            
            # Basic fields
            issue_type = row_dict.get('Issue Type', '').strip()
            status = row_dict.get('Status', '').strip()
            priority = row_dict.get('Priority', '').strip()
            request_type = row_dict.get('Custom field (Request Type)', '').strip()
            team = row_dict.get('Custom field (Team)', '').strip()
            category = row_dict.get('Custom field (Category)', '').strip()
            epic = row_dict.get('Custom field (Epic Name)', '').strip()
            assignee = row_dict.get('Assignee', '').strip()
            reporter = row_dict.get('Reporter', '').strip()
            summary = row_dict.get('Summary', '').strip()
            issue_key = row_dict.get('Issue key', '').strip()
            
            # Counters
            if issue_type:
                results['issue_types'][issue_type] += 1
            if status:
                results['statuses'][status] += 1
            if priority:
                results['priorities'][priority] += 1
            if request_type:
                results['request_types'][request_type] += 1
            if team:
                results['teams'][team] += 1
            if category:
                results['categories'][category] += 1
            if epic:
                results['epics'][epic] += 1
            if assignee:
                results['assignees'][assignee] += 1
            if reporter:
                results['reporters'][reporter] += 1
            
            # Dates
            created = parse_date(row_dict.get('Created', ''))
            updated = parse_date(row_dict.get('Updated', ''))
            resolved = parse_date(row_dict.get('Resolved', ''))
            
            # Calculate resolution time early (used in multiple places)
            resolution_time = None
            if created and resolved:
                resolution_time = calculate_resolution_time(created, resolved)
            
            # Story points
            story_points = parse_story_points(row_dict.get('Custom field (Story point estimate)', ''))
            if story_points:
                results['story_points'].append(story_points)
            
            # Time tracking - estimates and actual time
            original_estimate = parse_time_seconds(row_dict.get('Original estimate', ''))
            remaining_estimate = parse_time_seconds(row_dict.get('Remaining Estimate', ''))
            time_spent = parse_time_seconds(row_dict.get('Time Spent', ''))
            baseline_estimate = parse_time_seconds(row_dict.get('Custom field (Baseline Estimate)', ''))
            
            if original_estimate:
                results['time_tracking']['original_estimates'].append(original_estimate)
            if remaining_estimate:
                results['time_tracking']['remaining_estimates'].append(remaining_estimate)
            if time_spent:
                results['time_tracking']['time_spent'].append(time_spent)
            if baseline_estimate:
                results['time_tracking']['baseline_estimates'].append(baseline_estimate)
            
            # Estimation accuracy - compare original estimate to time spent
            if original_estimate and time_spent and time_spent > 0:
                ratio = original_estimate / time_spent
                results['time_tracking']['estimation_accuracy'].append({
                    'issue_key': issue_key,
                    'original_estimate_seconds': original_estimate,
                    'time_spent_seconds': time_spent,
                    'ratio': ratio,  # >1 = overestimated, <1 = underestimated
                    'overestimate': original_estimate > time_spent,
                    'underestimate': original_estimate < time_spent
                })
            
            # Comment analysis - use row_list to access by index
            comments = parse_comments(row_list, headers)
            comment_count = len(comments)
            if comment_count > 0:
                results['comment_analysis']['total_comments'] += comment_count
                results['comment_analysis']['issues_with_comments'] += 1
                results['comment_analysis']['comment_counts_per_issue'].append({
                    'issue_key': issue_key,
                    'comment_count': comment_count,
                    'type': issue_type,
                    'status': status
                })
            
            # Priority analysis - track by priority for comparison
            if resolution_time is not None and resolution_time <= OUTLIER_THRESHOLD_DAYS:
                priority_key = priority if priority and priority != 'None' else 'None'
                if priority_key in results['priority_comparison']:
                    results['priority_comparison'][priority_key]['count'] += 1
                    results['priority_comparison'][priority_key]['resolution_times'].append(resolution_time)
                else:
                    # Handle unlisted priorities - add to None bucket
                    results['priority_comparison']['None']['count'] += 1
                    results['priority_comparison']['None']['resolution_times'].append(resolution_time)
            
            # Track None priority issues specifically
            if priority == '' or priority == 'None':
                results['none_priority_analysis']['all_none_priority'].append({
                    'key': issue_key,
                    'summary': summary,
                    'type': issue_type,
                    'status': status,
                    'resolution_time': resolution_time,
                    'request_type': request_type,
                    'category': category
                })
                if resolution_time is not None and resolution_time <= OUTLIER_THRESHOLD_DAYS:
                    results['none_priority_analysis']['resolved_none_priority'].append({
                        'key': issue_key,
                        'summary': summary,
                        'type': issue_type,
                        'resolution_time': resolution_time,
                        'request_type': request_type,
                        'category': category
                    })
                    # Quick resolution suggests urgency despite no priority
                    if resolution_time <= 7:
                        results['none_priority_analysis']['quick_resolution_none'].append({
                            'key': issue_key,
                            'summary': summary,
                            'type': issue_type,
                            'resolution_time': resolution_time,
                            'request_type': request_type,
                            'category': category
                        })
                    if resolution_time <= 3:
                        results['none_priority_analysis']['very_quick_resolution_none'].append({
                            'key': issue_key,
                            'summary': summary,
                            'type': issue_type,
                            'resolution_time': resolution_time,
                            'request_type': request_type,
                            'category': category
                        })
            
            # Resolution analysis - separate outliers from typical work
            if resolution_time is not None:
                if resolution_time > OUTLIER_THRESHOLD_DAYS:
                    # Track as outlier (strategic initiative, work outside JIRA)
                    results['outlier_issues'].append({
                        'key': issue_key,
                        'summary': summary,
                        'type': issue_type,
                        'priority': priority,
                        'resolution_time': resolution_time,
                        'story_points': story_points,
                        'request_type': request_type
                    })
                else:
                    # Include in normal statistics
                    results['resolution_times'].append(resolution_time)
                    results['resolved_issues'].append({
                        'key': issue_key,
                        'summary': summary,
                        'type': issue_type,
                        'priority': priority,
                        'resolution_time': resolution_time,
                        'story_points': story_points,
                        'request_type': request_type
                    })
            
            # Last 3 months analysis
            if created and is_in_last_3_months(created):
                results['last_3_months']['issues'].append({
                    'key': issue_key,
                    'summary': summary,
                    'type': issue_type,
                    'status': status,
                    'priority': priority,
                    'request_type': request_type,
                    'created': created,
                    'resolved': resolved,
                    'story_points': story_points
                })
                if issue_type:
                    results['last_3_months']['issue_types'][issue_type] += 1
                if status:
                    results['last_3_months']['statuses'][status] += 1
                if request_type:
                    results['last_3_months']['request_types'][request_type] += 1
                if resolved:
                    results['last_3_months']['resolved'] += 1
                    # Only include non-outlier resolution times in last 3 months stats
                    if resolution_time is not None and resolution_time <= OUTLIER_THRESHOLD_DAYS:
                        results['last_3_months']['resolution_times'].append(resolution_time)
            
            # Challenging work (high story points or long resolution, but not outliers)
            # Only include issues that are challenging but within normal timeframe
            if story_points and story_points >= 5:
                results['challenging_work'].append({
                    'key': issue_key,
                    'summary': summary,
                    'story_points': story_points,
                    'resolution_time': resolution_time,
                    'type': issue_type,
                    'status': status
                })
            elif resolution_time is not None and 30 <= resolution_time <= OUTLIER_THRESHOLD_DAYS:
                results['challenging_work'].append({
                    'key': issue_key,
                    'summary': summary,
                    'resolution_time': resolution_time,
                    'story_points': story_points,
                    'type': issue_type,
                    'status': status
                })
            
            # Unresolved high priority
            if status and status not in ['Done', 'Closed', 'Resolved'] and priority in ['Critical', 'High', 'Major']:
                results['unresolved_high_priority'].append({
                    'key': issue_key,
                    'summary': summary,
                    'priority': priority,
                    'status': status,
                    'type': issue_type,
                    'created': created,
                    'request_type': request_type
                })
            
            # Recent activity (last 30 days)
            if updated:
                thirty_days_ago = datetime.now() - timedelta(days=30)
                if updated >= thirty_days_ago:
                    results['recent_activity'].append({
                        'key': issue_key,
                        'summary': summary,
                        'status': status,
                        'updated': updated,
                        'type': issue_type
                    })
    
    # Calculate average comments per issue
    if results['total_issues'] > 0:
        results['comment_analysis']['average_comments_per_issue'] = results['comment_analysis']['total_comments'] / results['total_issues']
    
    return results


def serialize_for_json(obj: Any) -> Any:
    """Convert objects to JSON-serializable format."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, Counter):
        return dict(obj)
    elif isinstance(obj, dict):
        return {k: serialize_for_json(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [serialize_for_json(item) for item in obj]
    elif isinstance(obj, set):
        return list(obj)
    else:
        return obj


def export_analysis_data(results: Dict[str, Any], output_path: str):
    """Export structured data to JSON for AI analysis."""
    
    # Calculate summary statistics
    summary_stats = {
        'total_issues': results['total_issues'],
        'resolved_issues': {
            'typical': len(results['resolved_issues']),
            'outliers': len(results['outlier_issues']),
            'total': len(results['resolved_issues']) + len(results['outlier_issues']),
            'percentage': (len(results['resolved_issues']) + len(results['outlier_issues'])) / results['total_issues'] * 100 if results['total_issues'] > 0 else 0
        },
        'resolution_times': {
            'average': float(statistics.mean(results['resolution_times'])) if results['resolution_times'] else None,
            'median': float(statistics.median(results['resolution_times'])) if results['resolution_times'] else None,
            'min': float(min(results['resolution_times'])) if results['resolution_times'] else None,
            'max': float(max(results['resolution_times'])) if results['resolution_times'] else None,
            'outlier_threshold_days': OUTLIER_THRESHOLD_DAYS
        },
        'story_points': {
            'total': float(sum(results['story_points'])) if results['story_points'] else None,
            'average': float(statistics.mean(results['story_points'])) if results['story_points'] else None,
            'median': float(statistics.median(results['story_points'])) if results['story_points'] else None,
            'min': float(min(results['story_points'])) if results['story_points'] else None,
            'max': float(max(results['story_points'])) if results['story_points'] else None
        },
        'last_3_months': {
            'total_issues': len(results['last_3_months']['issues']),
            'resolved': results['last_3_months']['resolved'],
            'average_resolution_time': float(statistics.mean(results['last_3_months']['resolution_times'])) if results['last_3_months']['resolution_times'] else None
        }
    }
    
    # Prepare priority comparison stats
    priority_stats = {}
    for priority_name, priority_data in results['priority_comparison'].items():
        if priority_data['resolution_times']:
            priority_stats[priority_name] = {
                'count': priority_data['count'],
                'average_days': float(statistics.mean(priority_data['resolution_times'])),
                'median_days': float(statistics.median(priority_data['resolution_times']))
            }
    
    # Prepare export data structure
    export_data = {
        'metadata': {
            'analysis_date': datetime.now().isoformat(),
            'source_file': 'RUDIS-JIRA.csv',
            'outlier_threshold_days': OUTLIER_THRESHOLD_DAYS
        },
        'summary': summary_stats,
        'distribution': {
            'priorities': dict(results['priorities']),
            'issue_types': dict(results['issue_types']),
            'statuses': dict(results['statuses']),
            'request_types': dict(results['request_types']),
            'teams': dict(results['teams']),
            'categories': dict(results['categories']),
            'epics': dict(results['epics']),
            'assignees': dict(results['assignees']),
            'reporters': dict(results['reporters'])
        },
        'priority_comparison': priority_stats,
        'challenging_work': {
            'outliers': results['outlier_issues'][:20],  # Top 20
            'typical': sorted(results['challenging_work'], 
                            key=lambda x: (x.get('story_points') or 0, x.get('resolution_time') or 0), 
                            reverse=True)[:20]
        },
        'unresolved_high_priority': results['unresolved_high_priority'],
        'none_priority_analysis': {
            'total': len(results['none_priority_analysis']['all_none_priority']),
            'resolved': len(results['none_priority_analysis']['resolved_none_priority']),
            'resolved_issues': results['none_priority_analysis']['resolved_none_priority'],
            'quick_resolution': results['none_priority_analysis']['quick_resolution_none'],
            'very_quick_resolution': results['none_priority_analysis']['very_quick_resolution_none'],
            'statistics': {
                'average_resolution': float(statistics.mean([item['resolution_time'] for item in results['none_priority_analysis']['resolved_none_priority']])) if results['none_priority_analysis']['resolved_none_priority'] else None,
                'median_resolution': float(statistics.median([item['resolution_time'] for item in results['none_priority_analysis']['resolved_none_priority']])) if results['none_priority_analysis']['resolved_none_priority'] else None
            }
        },
        'last_3_months': {
            'issues': results['last_3_months']['issues'],
            'issue_types': dict(results['last_3_months']['issue_types']),
            'statuses': dict(results['last_3_months']['statuses']),
            'request_types': dict(results['last_3_months']['request_types']),
            'resolved_count': results['last_3_months']['resolved'],
            'resolution_times': results['last_3_months']['resolution_times']
        },
        'time_tracking': {
            'summary': {
                'total_original_estimate_hours': sum(results['time_tracking']['original_estimates']) / 3600 if results['time_tracking']['original_estimates'] else None,
                'total_time_spent_hours': sum(results['time_tracking']['time_spent']) / 3600 if results['time_tracking']['time_spent'] else None,
                'average_original_estimate_hours': statistics.mean([x / 3600 for x in results['time_tracking']['original_estimates']]) if results['time_tracking']['original_estimates'] else None,
                'average_time_spent_hours': statistics.mean([x / 3600 for x in results['time_tracking']['time_spent']]) if results['time_tracking']['time_spent'] else None,
                'estimation_accuracy_count': len(results['time_tracking']['estimation_accuracy']),
                'overestimated_count': sum(1 for x in results['time_tracking']['estimation_accuracy'] if x['overestimate']),
                'underestimated_count': sum(1 for x in results['time_tracking']['estimation_accuracy'] if x['underestimate']),
                'average_estimate_ratio': statistics.mean([x['ratio'] for x in results['time_tracking']['estimation_accuracy']]) if results['time_tracking']['estimation_accuracy'] else None
            },
            'estimation_accuracy': results['time_tracking']['estimation_accuracy'][:50]  # Top 50 for analysis
        },
        'comment_analysis': {
            'total_comments': results['comment_analysis']['total_comments'],
            'issues_with_comments': results['comment_analysis']['issues_with_comments'],
            'issues_without_comments': results['total_issues'] - results['comment_analysis']['issues_with_comments'],
            'average_comments_per_issue': results['comment_analysis']['average_comments_per_issue'],
            'high_comment_issues': sorted(results['comment_analysis']['comment_counts_per_issue'], 
                                        key=lambda x: x['comment_count'], reverse=True)[:20]  # Top 20 by comment count
        }
    }
    
    # Serialize and write JSON
    serialized = serialize_for_json(export_data)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(serialized, f, indent=2, ensure_ascii=False)


def main():
    """Main execution."""
    script_dir = Path(__file__).parent
    csv_path = script_dir.parent.parent / 'data' / 'RUDIS-JIRA.csv'
    output_path = script_dir / 'jira-analysis-data.json'
    
    print("Extracting and analyzing JIRA data...")
    results = analyze_jira_data(str(csv_path))
    
    print("Exporting structured data...")
    export_analysis_data(results, str(output_path))
    
    print(f"Data extraction complete! Structured data saved to: {output_path}")
    print("Next step: Review the JSON data and have AI generate the analysis report.")


if __name__ == '__main__':
    main()

