# JIRA Analysis - RUDIS Development Insights

## Context

This analysis was conducted to understand development patterns, priorities, and work trends for Rudis/CQL collaboration. The goal is to identify actionable insights for optimizing digital technology to drive business value and growth.

## Files

- **`analyze_jira.py`** - Python script that parses the JIRA CSV export and generates comprehensive statistics
- **`RUDIS-JIRA-Insights.md`** - Generated analysis report with all insights and findings
- **`RUDIS-JIRA.csv`** - Source data (located in `../../data/RUDIS-JIRA.csv`)

## Running the Analysis

```bash
python3 analyze_jira.py
```

The script will:
1. Parse the JIRA CSV export from `../../data/RUDIS-JIRA.csv`
2. Extract key metrics and patterns
3. Generate a comprehensive markdown report

## Analysis Scope

- **Total Issues Analyzed:** ~8,102 JIRA issues
- **Time Period:** All-time analysis with deep dive into last 3 months (Aug-Nov 2025)
- **Key Metrics:** Work types, priorities, request patterns, resolution times, team activity, challenging work identification

## Next Steps

Review the insights in `RUDIS-JIRA-Insights.md` and determine:
1. Which findings should be promoted to long-term documentation
2. What additional analysis or questions need investigation
3. Action items for optimization and process improvement

