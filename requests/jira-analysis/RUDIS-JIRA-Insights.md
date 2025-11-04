# RUDIS Development Budget Allocation Analysis

*Analysis Date: November 04, 2025*  
*Data Source: RUDIS-JIRA.csv*  
*Focus Period: Full Year 2025 (January - December 2025)*

---

## Methodology & Data Transparency

### Data Source

- **Source:** JIRA CSV export (RUDIS-JIRA.csv)
- **Total Issues in Dataset:** 395
- **Issues in Analysis Period:** 231
- **Date Range:** Issues created January 1, 2025 - December 31, 2025

### Development Budget

- **Monthly Budget:** 70 hours ($14,000/month)
- **Annual Budget (2025):** 840 hours ($168,000)
- **Blended Developer Rate:** $200/hour
- **Budget Allocation Method:** Issue count used as proxy where time tracking unavailable

### Categorization Methodology

Issues are categorized into strategic areas based on issue summary text, description text, and issue type:

- **Text Analysis:** Both summary and description fields are analyzed for categorization keywords
- **Coverage:** 68% of 2025 issues have descriptions (average 655 characters)
- **Issue Type:** Issue type (Bug, Epic, Story, etc.) is also considered for categorization

- **Team Store / B2B:** Issues containing 'team', 'team store', 'usaw', or 'bulk'
- **Product Display (PDP):** Issues containing 'pdp', 'product detail', 'variant', or 'swatch'
- **Product Listing (PLP):** Issues containing 'plp', 'product listing', or 'collection'
- **Cart/Checkout/Conversion:** Issues containing 'cart', 'checkout', 'add to cart', or 'atc'
- **Shipping/Logistics:** Issues containing 'shipping' or 'free shipping'
- **Account/User Experience:** Issues containing 'account', 'user', 'return', 'order', or 'rewards'
- **Design/UX Enhancements:** Issues containing 'design', 'image', 'header', 'parallax', or 'video'
- **Technical/Infrastructure:** Issues containing 'seo', 'robot', 'llms.txt', 'attentive', 'pixel', or 'theme'
- **Bug Fixes:** Issues with Issue Type = 'Bug'
- **Other:** Issues that don't match above categories

**Note:** Categorization is automated based on keywords. Some issues may be miscategorized. Manual review recommended for strategic decisions.

### Business Value Classification

Business value categories are inferred from issue content:

- **Revenue Impact:** Issues directly affecting cart, checkout, conversion, or free shipping
- **Operational Efficiency:** Issues related to Team Store/B2B operations or bulk ordering
- **Technical Debt:** Issues with Issue Type = 'Bug'
- **User Experience:** Issues related to design, UX, account, or user-facing features

**Limitation:** Business value is inferred, not explicitly stated in JIRA data. Actual ROI/impact requires business metrics.

### Status Definitions

- **Resolved:** Status = 'Done' or 'Closed'
- **Unresolved:** Status not 'Done' or 'Closed'
- **Stuck:** Status in 'Hold', 'Update Requirements', 'Needs Estimate', or 'Waiting for Approval'
- **Resolution Rate:** (Resolved Issues / Total Issues) × 100

### Priority Definitions

- **High Priority:** Priority = 'Critical', 'Blocker', or 'Major'
- **None Priority:** Priority field is empty or 'None'

**Note:** 71% of issues have no priority assigned. This suggests priority may not be used systematically for planning.

### Assumptions & Limitations

1. **Budget Allocation Proxy:** Issue count is used as a proxy for development budget allocation. Actual time/cost per issue is not available for most issues.

2. **Categorization Accuracy:** Automated categorization based on keywords may misclassify issues. Manual review of key issues recommended.

3. **Business Value Inference:** Business value categories are inferred from issue content, not actual measured impact. No revenue/ROI data available.

4. **Time Period:** Analysis covers all issues created in 2025 (January - December). Work in progress from prior years not included.

5. **Resolution Context:** 'Stuck' status may indicate legitimate planning phases (e.g., 'Needs Estimate' for new work). Not all stuck work is problematic.

6. **Priority System:** High percentage of issues without priority suggests priority system may not be used systematically.

### Data Quality

- **Issues with Time Tracking (2025):** 44 (19% of 2025 issues)
- **Issues with Time Tracking (All Time):** 59 (15% of all issues)
- **Issues with Comments:** 269 (68% of all issues)
- **Issues with Priority:** 90 (23% of all issues)

**Recommendation:** Improve data quality by ensuring time tracking, priority assignment, and clear categorization for better analysis.

---

## Executive Summary

### Budget Allocation by Strategic Theme

| Theme                     | Issues | Assumed Hours | Assumed Cost | % of Budget | Resolved | Unresolved | Stuck | Resolution Rate |
| ------------------------- | ------ | ------------- | ------------ | ----------- | -------- | ---------- | ----- | --------------- |
| Revenue & Growth          | 63     | 223h          | $44,650      | 27%         | 45       | 18         | 12    | 71%             |
| Business Operations       | 61     | 182h          | $36,450      | 22%         | 35       | 26         | 17    | 57%             |
| Platform & Infrastructure | 25     | 22h           | $4,500       | 3%          | 22       | 3          | 2     | 88%             |
| Customer Experience       | 59     | 18h           | $3,650       | 2%          | 42       | 17         | 15    | 71%             |
| Quality & Compliance      | 11     | 3h            | $550         | 0%          | 7        | 4          | 0     | 64%             |
| Strategic & Planning      | 12     | -             | -            | -           | 8        | 4          | 1     | 67%             |

---

## Budget Allocation Overview

**Total Issues:** 231
**Resolved:** 159 (69%)
**Unresolved:** 72 (31%)

### Assumed Spend vs. Estimated Total Cost

#### Assumed Spend (Tracked Hours)

**Resolved Issues:** 43 issues, 444 hours ($88,800)
**Unresolved Issues:** 1 issues, 5 hours ($1,000)
**Total Assumed Spend:** 449 hours ($89,800)

#### Estimated Additional Costs (Untracked Issues)

**Resolved but Untracked:** 116 issues
  - Estimated: 1198 hours ($239,553)
  - *Based on average of 10.3 hours per tracked resolved issue*

**Unresolved but Untracked:** 71 issues
  - Estimated: 355 hours ($71,000)
  - *Based on average of 5.0 hours per tracked unresolved issue*

#### Total Estimated Cost

**Assumed Spend:** 449 hours ($89,800)
**Estimated Remaining:** 1553 hours ($310,553)
**Estimated Total Cost:** 2002 hours ($400,353)

*Note: Estimates for untracked issues use averages from tracked issues of the same resolution status. This provides a more accurate projection than a single average across all issues.*

**Budget Available (2025):** 840 hours ($168,000)
**Budget Utilization (Assumed Spend):** 53%

#### Backlog Capacity Analysis

**Estimated Total Work:** 2002 hours ($400,353)
**Budget Capacity:** 840 hours ($168,000)
**Backlog Beyond Budget:** 1162 hours ($232,353)

*Note: The estimated work volume exceeds available budget capacity. This indicates a backlog that will require ongoing prioritization and selective deferral of lower-priority items. This is a normal part of managing a fixed-budget development program.*

### Unresolved Issues Analysis

**Issues with Time Logged:** 1 issues have time logged but are unresolved
  - **Hours Invested:** 5 hours ($1,000)
  - **Interpretation:** Work in progress - these issues are actively being worked on

### Detailed Work Allocation by Category

*Note: Categories are grouped into executive themes above. This section provides detailed breakdown.*

| Theme                     | Category                         | Issues | Assumed Hours | Assumed Cost | % of Budget | Resolved | In Process | Stuck | Resolution Rate |
| ------------------------- | -------------------------------- | ------ | ------------- | ------------ | ----------- | -------- | ---------- | ----- | --------------- |
| Business Operations       | Team Store / B2B                 | 54     | 182h          | $36,450      | 22%         | 30       | 8          | 16    | 56%             |
| Revenue & Growth          | Product Display (PDP)            | 27     | 144h          | $28,700      | 17%         | 20       | 3          | 4     | 74%             |
| Revenue & Growth          | Cart/Checkout/Conversion         | 16     | 36h           | $7,150       | 4%          | 12       | 0          | 4     | 75%             |
| Revenue & Growth          | Product Listing (PLP)            | 9      | 28h           | $5,550       | 3%          | 5        | 1          | 3     | 56%             |
| Platform & Infrastructure | Technical/Infrastructure         | 6      | 18h           | $3,500       | 2%          | 5        | 0          | 1     | 83%             |
| Customer Experience       | Account/User Experience          | 36     | 11h           | $2,250       | 1%          | 22       | 0          | 14    | 61%             |
| Revenue & Growth          | Pricing & Promotions             | 5      | 11h           | $2,200       | 1%          | 3        | 1          | 1     | 60%             |
| Revenue & Growth          | Shipping/Logistics               | 2      | 5h            | $1,050       | 1%          | 1        | 1          | 0     | 50%             |
| Platform & Infrastructure | Analytics & Integrations         | 8      | 5h            | $1,000       | 1%          | 6        | 1          | 1     | 75%             |
| Customer Experience       | Design/UX Enhancements           | 16     | 4h            | $900         | 1%          | 13       | 2          | 1     | 81%             |
| Quality & Compliance      | Compliance & Legal               | 3      | 3h            | $550         | 0%          | 3        | 0          | 0     | 100%            |
| Customer Experience       | Content & Pages                  | 7      | 2h            | $500         | 0%          | 7        | 0          | 0     | 100%            |
| Revenue & Growth          | Search & Discovery               | 4      | -             | -            | -           | 4        | 0          | 0     | 100%            |
| Business Operations       | Process & Operations             | 2      | -             | -            | -           | 0        | 1          | 1     | 0%              |
| Business Operations       | Financial & Operations           | 3      | -             | -            | -           | 3        | 0          | 0     | 100%            |
| Business Operations       | Product Launches & Categories    | 2      | -             | -            | -           | 2        | 0          | 0     | 100%            |
| Platform & Infrastructure | Deployment & Operations          | 6      | -             | -            | -           | 6        | 0          | 0     | 100%            |
| Platform & Infrastructure | Database & Configuration         | 1      | -             | -            | -           | 1        | 0          | 0     | 100%            |
| Platform & Infrastructure | Third-party Tools & Integrations | 4      | -             | -            | -           | 4        | 0          | 0     | 100%            |
| Quality & Compliance      | Testing & Investigation          | 3      | -             | -            | -           | 0        | 3          | 0     | 0%              |
| Quality & Compliance      | QA & Testing                     | 4      | -             | -            | -           | 3        | 1          | 0     | 75%             |
| Quality & Compliance      | Bug Fixes                        | 1      | -             | -            | -           | 1        | 0          | 0     | 100%            |
| Strategic & Planning      | Requirements & Planning          | 3      | -             | -            | -           | 1        | 2          | 0     | 33%             |
| Strategic & Planning      | Strategic Initiatives            | 3      | -             | -            | -           | 1        | 1          | 1     | 33%             |
| Strategic & Planning      | Development Sprints              | 2      | -             | -            | -           | 2        | 0          | 0     | 100%            |
| Strategic & Planning      | Framework & Strategy             | 1      | -             | -            | -           | 1        | 0          | 0     | 100%            |
| Strategic & Planning      | Design Specs & Reviews           | 3      | -             | -            | -           | 3        | 0          | 0     | 100%            |

### Allocation Insights

- **Largest Focus Area:** Team Store / B2B (23% of work, 54 issues)
- **Highest Completion Rate:** Compliance & Legal (100% resolved)
- **Lowest Completion Rate:** Testing & Investigation (0% resolved) - may indicate scope issues or blockers
- **Most Stuck Work:** Team Store / B2B (30% stuck, 16 issues)

---

## Strategic Category Analysis

### Team Store / B2B

**Total Issues:** 54 (23% of issues)
**Assumed Hours:** 182 hours ($36,450)
**Estimated Hours:** 563 hours ($112,625) - 22% of budget
**Resolved:** 30 (56%)
**In Process/Approved:** 8 (likely active work)
**Stuck:** 16 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 8 total

**Resolved Work:**
- **RUDS25-450:** TEAM BUG: RUDIS+ member Free shipping on team store (None)
- **RUDS25-436:** Team: Closed store for non-sales / coach experience (None)
- **RUDS25-434:** TEAM: Opp Collection does not pass variable to product to remember OPP (None)
- **RUDS25-403:** Grid PLP layout for improved ordering (None)
- **RUDS25-394:** Email Reminder template for Minimums (None)
- ...and 25 more

**Unresolved Work:**
- **RUDS25-463:** Expand image limit for team store orders (Approved, None)
- **RUDS25-441:** Team Store Price Does Not Convert Internationally (New, None)
- **RUDS25-429:** PDF Catalog Embed (New, None)
- **RUDS25-416:** LLM / ChatGPT Product Recommendations (Client QA, None)
- **RUDS25-412:** Set non-SearchSpring collection as the default template (Approved, None)
- ...and 3 more

**Stuck Work:**
- **RUDS25-464:** Custom Team Gear - Product Bundles (Needs Estimate)
- **RUDS25-454:** Team Store: Theme not showing Custom Image on PLP (Waiting for Approval)
- **RUDS25-451:** TEAM: New Functionality for USAW bulk customer ordering (Needs Estimate)
- **RUDS25-444:** Update Celigo Flow to use new API Version (Waiting for Approval)
- **RUDS25-443:** NEW: Collection Component(s) / Automation? (Update Requirements)
- **RUDS25-389:** Post-Order Communication to Coaches (Update Requirements)
- **RUDS25-388:** Checkout Issues for Bulk Orders (Update Requirements)
- **RUDS25-386:** Improve Item Creation Process (Update Requirements)
- **RUDS25-383:** Make art approval public (Hold)
- **RUDS25-375:** Product Naming Convention Change [PLACEHOLDER] (Update Requirements)
- **RUDS25-342:** Team Store - Kickflip POC (Hold)
- **RUDS25-305:** Team Store - Add a builder app for singlets (Hold)
- **RUDS25-289:** Youth-Adult Product Split (Hold)
- **RUDS25-288:** Ecommerce product only orders for teams does not link to opportunity (Update Requirements)
- **RUDS25-271:** rudis-AMP80 Provide synchronized audio description for video (which in (Hold)
- **RUDS25-270:** rudis-AMP79 Provide synchronized captions for video (which includes au (Hold)


### Account/User Experience

**Total Issues:** 36 (16% of issues)
**Assumed Hours:** 11 hours ($2,250)
**Estimated Hours:** 41 hours ($8,250) - 1% of budget
**Resolved:** 22 (61%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 14 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-461:** Create Video Section (Major)
- **RUDS25-442:** Add llms.txt file (None)
- **RUDS25-420:** Robot.txt modification (None)
- **RUDS25-414:** BUG: Homepage slider dots unable to scroll on Mobile (Major)
- **RUDS25-411:** Create Account Block for Rewards Info (None)
- ...and 17 more

**Stuck Work:**
- **RUDS25-439:** New Design Component: Image banner that supports flexible content alig (Update Requirements)
- **RUDS25-385:** Improve Order Modification Delays (Hold)
- **RUDS25-380:** Inaccessible Filter Tool (also rendered in a pop-up) (Hold)
- **RUDS25-379:** Information Conveyed Solely via Visual Cues (e.g., dimmed sizes for ou (Hold)
- **RUDS25-377:** Missing or Inadequate Alternative Text for Non-Text Elements (e.g., pr (Hold)
- **RUDS25-267:** rudis-AMP47 Indicate live regions for dynamically changing content (Hold)
- **RUDS25-266:** rudis-AMP46 Ensure custom controls are keyboard accessible (Hold)
- **RUDS25-265:** rudis-AMP45 Ensure custom controls are keyboard accessible (Hold)
- **RUDS25-264:** rudis-AMP34 Indicate live regions for dynamically changing content (Hold)
- **RUDS25-263:** rudis-AMP31 Ensure content updates define focus updates appropriately (Hold)
- **RUDS25-262:** rudis-AMP19 Indicate live regions for dynamically changing content (Hold)
- **RUDS25-261:** rudis-AMP17 Ensure custom controls are keyboard accessible (Hold)
- **RUDS25-260:** rudis-AMP11 Provide a valid label for form fields (Hold)
- **RUDS25-239:** Make Navigation Menu ADA Compliant (Hold)


### Product Display (PDP)

**Total Issues:** 27 (12% of issues)
**Assumed Hours:** 144 hours ($28,700)
**Estimated Hours:** 319 hours ($63,778) - 17% of budget
**Resolved:** 20 (74%)
**In Process/Approved:** 3 (likely active work)
**Stuck:** 4 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 3 total

**Resolved Work:**
- **RUDS25-448:** Free Shipping Threshold Change (None)
- **RUDS25-447:** BUG: Shoes Notify PopUp (None)
- **RUDS25-445:** PDP Variant color showing both variant images (None)
- **RUDS25-435:** Design: Apparel Product Cards - Color Swatches (None)
- **RUDS25-402:** Sticky Promo Bar Issue (None)
- ...and 15 more

**Unresolved Work:**
- **RUDS25-446:** Parallax Scrolling Content Pages (Approved, None)
- **RUDS25-432:** PDP metafield for promotions (New, None)
- **RUDS25-430:** PDP Size cross-link (New, None)

**Stuck Work:**
- **RUDS25-467:** SWATCH PLP Bug - Double Price on Click (Update Requirements)
- **RUDS25-465:** Swatches PDP "You May Also Like" update (Needs Estimate)
- **RUDS25-455:** Product Listing Pages (PLPs) & Filter/Sort Updates (Update Requirements)
- **RUDS25-395:** "Colorblock" Bundles not displaying variants (Hold)


### Cart/Checkout/Conversion

**Total Issues:** 16 (7% of issues)
**Assumed Hours:** 36 hours ($7,150)
**Estimated Hours:** 143 hours ($28,600) - 4% of budget
**Resolved:** 12 (75%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 4 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-456:** BUG: Add to cart, Checkout and bounces to RUDIS.com and cart empty (Blocker)
- **RUDS25-449:** Free Shipping Offered In Cart: RUDIS-PLUS-SHIP (None)
- **RUDS25-415:** Add Start a Return to Orders dropdown (None)
- **RUDS25-409:** Image Carousel to use Slider not Dots (Major)
- **RUDS25-332:** BUG: Recommended Search - text overlap (None)
- ...and 7 more

**Stuck Work:**
- **RUDS25-462:** Free Shipping Mini Cart dollar threshold Global Theme Setting (Needs Estimate)
- **RUDS25-437:** Shopify.com Checkout URL (Waiting for Approval)
- **RUDS25-269:** rudis-AMP70 Indicate live regions for dynamically changing content (Hold)
- **RUDS25-268:** rudis-AMP64 Indicate live regions for dynamically changing content (Hold)


### Design/UX Enhancements

**Total Issues:** 16 (7% of issues)
**Assumed Hours:** 4 hours ($900)
**Estimated Hours:** 58 hours ($11,700) - 1% of budget
**Resolved:** 13 (81%)
**In Process/Approved:** 2 (likely active work)
**Stuck:** 1 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 2 total

**Resolved Work:**
- **RUDS25-433:** Font weights on mobile Buy Stack (None)
- **RUDS25-413:** Mobile Spacing - Filter Bar (None)
- **RUDS25-374:** Designs and UX improvements for Elevating Women's Products (None)
- **RUDS25-373:** M/F Faceout Imagery for Unisex Products (None)
- **RUDS25-369:** Parallax Scrolling (Major)
- ...and 8 more

**Unresolved Work:**
- **RUDS25-457:** Add "Complete the Look" to Bundles template + (New, None)
- **RUDS25-398:** UI/UX Improvements (Ongoing, None)

**Stuck Work:**
- **RUDS25-384:** Art Task Middleware Not Working (Update Requirements)


### Product Listing (PLP)

**Total Issues:** 9 (4% of issues)
**Assumed Hours:** 28 hours ($5,550)
**Estimated Hours:** 35 hours ($6,938) - 3% of budget
**Resolved:** 5 (56%)
**In Process/Approved:** 1 (likely active work)
**Stuck:** 3 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 1 total

**Resolved Work:**
- **RUDS25-440:** Add Collection pill header customization on Pages (Major)
- **RUDS25-418:** Native TS Collection - Product isn't retaining QTY during ATC (None)
- **RUDS25-392:** Collection Component (Blocker)
- **RUDS25-372:** PLP Web flow exploration (Critical)
- **RUDS25-258:** Collection Component (Critical)

**Unresolved Work:**
- **RUDS25-458:** Dynamic PLP Header Image Experience (Approved, None)

**Stuck Work:**
- **RUDS25-460:** Change the strike out price from green to red on the PLP (Hold)
- **RUDS25-338:** PLP Product Cards (Update Requirements)
- **RUDS25-259:** rudis-AMP6 Ensure custom controls are keyboard accessible (Hold)


### Analytics & Integrations

**Total Issues:** 8 (3% of issues)
**Assumed Hours:** 5 hours ($1,000)
**Estimated Hours:** 30 hours ($6,000) - 1% of budget
**Resolved:** 6 (75%)
**In Process/Approved:** 1 (likely active work)
**Stuck:** 1 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 1 total

**Resolved Work:**
- **RUDS25-459:** Attentive Theme Pixel App Embed Tag (Major)
- **RUDS25-410:** Elevar Post-Purchase GTM Tracking on Shopify (None)
- **RUDS25-404:** Shopify Notice: Thank you page upgrade (None)
- **RUDS25-401:** Update Tags in GTM (None)
- **RUDS25-358:** Frontend Integration, Catalogue upload/classification (None)
- ...and 1 more

**Unresolved Work:**
- **RUDS25-431:** UGC / TikTok / Social Video Feed integration support (New, None)

**Stuck Work:**
- **RUDS25-438:** Google Verification Token Removal (Update Requirements)


### Content & Pages

**Total Issues:** 7 (3% of issues)
**Assumed Hours:** 2 hours ($500)
**Estimated Hours:** 9 hours ($1,750) - 0% of budget
**Resolved:** 7 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-315:** Yotpo Landing Page Review (None)
- **RUDS25-296:** Design Updates - Featured Links Section Width Control (None)
- **RUDS25-291:** Catalog Store Enhancements (None)
- **RUDS25-285:** SEO - Duplicated H1 Tag in Page Content (Major)
- **RUDS25-280:** SEO - CSS & JS Minification & Review (Major)
- ...and 2 more


### Technical/Infrastructure

**Total Issues:** 6 (3% of issues)
**Assumed Hours:** 18 hours ($3,500)
**Estimated Hours:** 88 hours ($17,500) - 2% of budget
**Resolved:** 5 (83%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 1 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-426:** Implement Uber component on Rudis (None)
- **RUDS25-407:** Old Component Mockup - Feature Links (Minor)
- **RUDS25-365:** Fixes / Verification (2) (None)
- **RUDS25-362:** Fixes / Verification (None)
- **RUDS25-277:** SEO - Fix Global 404 in Country Selector (Minor)

**Stuck Work:**
- **RUDS25-408:** “Social Media Feed” Component / Suggestions for this feature (Hold)


### Deployment & Operations

**Total Issues:** 6 (3% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 6 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-368:** Open Countries / Go Live (None)
- **RUDS25-367:** Deploy in Prod (None)
- **RUDS25-366:** Preparation for Go-Live (None)
- **RUDS25-363:** Deployment to Pre Production environment (None)
- **RUDS25-335:** BUG: Personalization (recommended products) NOT in buy stack (None)
- ...and 1 more


### Pricing & Promotions

**Total Issues:** 5 (2% of issues)
**Assumed Hours:** 11 hours ($2,200)
**Estimated Hours:** 16 hours ($3,300) - 1% of budget
**Resolved:** 3 (60%)
**In Process/Approved:** 1 (likely active work)
**Stuck:** 1 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 1 total

**Resolved Work:**
- **RUDS25-406:** Change sale price from red to green (None)
- **RUDS25-354:** Business and pricing Rules (None)
- **RUDS25-306:** Sticky Promo Message when scrolling (None)

**Unresolved Work:**
- **RUDS25-427:** Pricing A/B testing - 3rd Party options investigation (New, None)

**Stuck Work:**
- **RUDS25-466:** "Submit A Request" - Auto Pop Chat Widget (Needs Estimate)


### Search & Discovery

**Total Issues:** 4 (2% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 4 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-400:** Shoe Finder/Quiz (None)
- **RUDS25-391:** Possible Navigation Menu Refresh (Search) (Major)
- **RUDS25-345:** Desktop Predictive Search Bug Fix (None)
- **RUDS25-286:** SEO - RUDIS Meta Data Review & Best Practices (Major)


### QA & Testing

**Total Issues:** 4 (2% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 3 (75%)
**In Process/Approved:** 1 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 1 total

**Resolved Work:**
- **RUDS25-364:** UAT & 2nd QA Cycle (None)
- **RUDS25-361:** 1st QA Cycle (None)
- **RUDS25-350:** Global-e: Pre-Prod Testing (UAT) (None)

**Unresolved Work:**
- **RUDS25-233:** QA (Ongoing, None)


### Third-party Tools & Integrations

**Total Issues:** 4 (2% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 4 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-351:** Global-e: Go Live (None)
- **RUDS25-349:** Global-e: Development (None)
- **RUDS25-348:** Global-e: Discovery (None)
- **RUDS25-255:** Deactivate Zendesk from storefront (None)


### Testing & Investigation

**Total Issues:** 3 (1% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 0 (0%)
**In Process/Approved:** 3 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 3 total

**Unresolved Work:**
- **RUDS25-425:** Investigate POS next steps (New, None)
- **RUDS25-422:** Investigate Roblox and how to implement (New, None)
- **RUDS25-417:** Nested Block Smoke Test Validation (New, None)


### Requirements & Planning

**Total Issues:** 3 (1% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 1 (33%)
**In Process/Approved:** 2 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 2 total

**Resolved Work:**
- **RUDS25-352:** Initial Analysis & Set-up (None)

**Unresolved Work:**
- **RUDS25-424:** CRO Best Practices (New, None)
- **RUDS25-423:** UWW TShirt requirements (New, None)


### Strategic Initiatives

**Total Issues:** 3 (1% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 1 (33%)
**In Process/Approved:** 1 (likely active work)
**Stuck:** 1 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 1 total

**Resolved Work:**
- **RUDS25-301:** Marketing & Merchandising (None)

**Unresolved Work:**
- **RUDS25-421:** Strategic Roadmap Initiatives (New, None)

**Stuck Work:**
- **RUDS25-299:** Elevate Women Products (Update Requirements)


### Compliance & Legal

**Total Issues:** 3 (1% of issues)
**Assumed Hours:** 3 hours ($550)
**Estimated Hours:** 8 hours ($1,650) - 0% of budget
**Resolved:** 3 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-419:** Cookie Preference footer link (None)
- **RUDS25-397:** OneTrust (None)
- **RUDS25-292:** OneTrust: Planning & Workshops (None)


### Financial & Operations

**Total Issues:** 3 (1% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 3 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-359:** Fulfilment & Refunds (None)
- **RUDS25-357:** Customer Service Aspects (None)
- **RUDS25-356:** Financial Aspects (None)


### Design Specs & Reviews

**Total Issues:** 3 (1% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 3 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-319:** B1: UI Spec (None)
- **RUDS25-318:** B1: Comps Review (None)
- **RUDS25-317:** B1: Wireframe Review (None)


### Shipping/Logistics

**Total Issues:** 2 (1% of issues)
**Assumed Hours:** 5 hours ($1,050)
**Estimated Hours:** 5 hours ($1,050) - 1% of budget
**Resolved:** 1 (50%)
**In Process/Approved:** 1 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 1 total

**Resolved Work:**
- **RUDS25-343:** BUG: INTL Orders displaying free shipping banner (None)

**Unresolved Work:**
- **RUDS25-428:** Geographically targeted tax holidays (New, None)


### Process & Operations

**Total Issues:** 2 (1% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 0 (0%)
**In Process/Approved:** 1 (likely active work)
**Stuck:** 1 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 1 total

**Unresolved Work:**
- **RUDS25-405:** Project Allocation (Ongoing, None)

**Stuck Work:**
- **RUDS25-387:** Improve quoting process in Shopify (Update Requirements)


### Development Sprints

**Total Issues:** 2 (1% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 2 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-327:** Sprint 3 Dev (None)
- **RUDS25-326:** Sprint 2 Dev (None)


### Product Launches & Categories

**Total Issues:** 2 (1% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 2 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-298:** Sarah H. Shoe Brand launch (None)
- **RUDS25-245:** Gift cards, bundles, & Accessories (None)


### Database & Configuration

**Total Issues:** 1 (0% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 1 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-360:** DB configuration (None)


### Framework & Strategy

**Total Issues:** 1 (0% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 1 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-324:** Framework Strategy Sessions (None)


### Bug Fixes

**Total Issues:** 1 (0% of issues)
**Assumed Hours:** 0 hours ($0)
**Estimated Hours:** 0 hours ($0) - 0% of budget
**Resolved:** 1 (100%)
**In Process/Approved:** 0 (likely active work)
**Stuck:** 0 (on hold, needs estimate, or waiting for approval)
**Unresolved:** 0 total

**Resolved Work:**
- **RUDS25-234:** Shopify Fraud Filter App deprecation (None)


---

## Prioritization Patterns

### Priority Distribution by Category

| Category                         | Critical | Blocker | Major | Minor | None |
| -------------------------------- | -------- | ------- | ----- | ----- | ---- |
| Team Store / B2B                 | 3        | 3       | 3     | 2     | 43   |
| Account/User Experience          | 1        | 8       | 2     | 0     | 25   |
| Product Display (PDP)            | 2        | 1       | 0     | 1     | 23   |
| Cart/Checkout/Conversion         | 1        | 3       | 1     | 0     | 11   |
| Design/UX Enhancements           | 0        | 0       | 2     | 0     | 14   |
| Product Listing (PLP)            | 3        | 2       | 1     | 0     | 3    |
| Analytics & Integrations         | 0        | 0       | 1     | 0     | 7    |
| Content & Pages                  | 0        | 0       | 2     | 0     | 5    |
| Technical/Infrastructure         | 0        | 0       | 0     | 2     | 4    |
| Deployment & Operations          | 1        | 0       | 0     | 0     | 5    |
| Pricing & Promotions             | 0        | 0       | 0     | 0     | 5    |
| Search & Discovery               | 0        | 0       | 2     | 0     | 2    |
| QA & Testing                     | 0        | 0       | 0     | 0     | 4    |
| Third-party Tools & Integrations | 0        | 0       | 0     | 0     | 4    |
| Testing & Investigation          | 0        | 0       | 0     | 0     | 3    |
| Requirements & Planning          | 0        | 0       | 0     | 0     | 3    |
| Strategic Initiatives            | 0        | 0       | 0     | 0     | 3    |
| Compliance & Legal               | 0        | 0       | 0     | 0     | 3    |
| Financial & Operations           | 0        | 0       | 0     | 0     | 3    |
| Design Specs & Reviews           | 0        | 0       | 0     | 0     | 3    |
| Shipping/Logistics               | 0        | 0       | 0     | 0     | 2    |
| Process & Operations             | 0        | 0       | 0     | 0     | 2    |
| Development Sprints              | 0        | 0       | 0     | 0     | 2    |
| Product Launches & Categories    | 0        | 0       | 0     | 0     | 2    |
| Database & Configuration         | 0        | 0       | 0     | 0     | 1    |
| Framework & Strategy             | 0        | 0       | 0     | 0     | 1    |
| Bug Fixes                        | 0        | 0       | 0     | 0     | 1    |

### High Priority Work Analysis

**High Priority Issues:** 42 (18% of work)

**Resolved:** 26 (62%)
**Unresolved:** 16

**Unresolved High Priority Issues:**
- **RUDS25-460:** Change the strike out price from green to red on the PLP (Product Listing (PLP), Hold)
- **RUDS25-455:** Product Listing Pages (PLPs) & Filter/Sort Updates (Product Display (PDP), Update Requirements)
- **RUDS25-439:** New Design Component: Image banner that supports flexible content alig (Account/User Experience, Update Requirements)
- **RUDS25-271:** rudis-AMP80 Provide synchronized audio description for video (which in (Team Store / B2B, Hold)
- **RUDS25-270:** rudis-AMP79 Provide synchronized captions for video (which includes au (Team Store / B2B, Hold)
- **RUDS25-269:** rudis-AMP70 Indicate live regions for dynamically changing content (Cart/Checkout/Conversion, Hold)
- **RUDS25-268:** rudis-AMP64 Indicate live regions for dynamically changing content (Cart/Checkout/Conversion, Hold)
- **RUDS25-267:** rudis-AMP47 Indicate live regions for dynamically changing content (Account/User Experience, Hold)
- **RUDS25-266:** rudis-AMP46 Ensure custom controls are keyboard accessible (Account/User Experience, Hold)
- **RUDS25-265:** rudis-AMP45 Ensure custom controls are keyboard accessible (Account/User Experience, Hold)
- **RUDS25-264:** rudis-AMP34 Indicate live regions for dynamically changing content (Account/User Experience, Hold)
- **RUDS25-263:** rudis-AMP31 Ensure content updates define focus updates appropriately (Account/User Experience, Hold)
- **RUDS25-262:** rudis-AMP19 Indicate live regions for dynamically changing content (Account/User Experience, Hold)
- **RUDS25-261:** rudis-AMP17 Ensure custom controls are keyboard accessible (Account/User Experience, Hold)
- **RUDS25-260:** rudis-AMP11 Provide a valid label for form fields (Account/User Experience, Hold)
- **RUDS25-259:** rudis-AMP6 Ensure custom controls are keyboard accessible (Product Listing (PLP), Hold)

**High Priority Work by Category:**
- Account/User Experience: 11 (26%)
- Team Store / B2B: 9 (21%)
- Product Listing (PLP): 6 (14%)
- Cart/Checkout/Conversion: 5 (12%)
- Product Display (PDP): 3 (7%)
- Search & Discovery: 2 (5%)
- Design/UX Enhancements: 2 (5%)
- Content & Pages: 2 (5%)
- Analytics & Integrations: 1 (2%)
- Deployment & Operations: 1 (2%)

---

## Business Value Analysis

### Budget Allocation by Business Value

| Value Type             | Issues | % of Budget | Resolution Rate |
| ---------------------- | ------ | ----------- | --------------- |
| Revenue Impact         | 25     | 11%         | 80%             |
| Operational Efficiency | 46     | 20%         | 50%             |
| Technical Debt         | 25     | 11%         | 88%             |
| User Experience        | 17     | 7%          | 82%             |

### Strategic Questions

- **Revenue Focus:** Only 11% of work is directly revenue-impacting. Is this sufficient for growth goals?
- **Priority Discipline:** Only 18% of work is marked high priority. Is everything truly a priority, or is the system not being used?

---

## Strategic Recommendations

### Improve Completion Rates

- Low resolution rates in: Testing & Investigation, Requirements & Planning, Strategic Initiatives
- Investigate why these areas have low completion
- Consider breaking work into smaller pieces
- Review scope and requirements clarity

### Address Unresolved High Priority

- 16 high-priority issues remain unresolved
- Review these for immediate attention
- Consider if priorities have changed
- Identify blockers preventing resolution

### Consider Budget Rebalancing

- Significant imbalance in work allocation across categories
- Review if current distribution matches strategic priorities
- Consider if underrepresented areas need more investment
- Assess if overrepresented areas are generating sufficient ROI

---