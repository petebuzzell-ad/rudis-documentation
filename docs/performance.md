# RUDIS Performance Documentation

**Last Updated:** October 31, 2025  
**Data Source:** Shopify CRUX Field Data (August 2 - October 31, 2025, 75th percentile)  
**Synthetic Data:** Lighthouse/PageSpeed Insights  
**Report Files:** `data/shopify-reports/`

---

## Executive Summary

RUDIS.com performance varies significantly across page types. Product and collection pages generally perform well, meeting Core Web Vitals thresholds. However, the homepage fails LCP requirements, and search pages have significant CLS issues. Mobile performance for product detail pages requires immediate attention.

**Overall Assessment:**
- **Product Pages:** ✅ Passing (56.6% of traffic)
- **Collection Pages:** ⚠️ Near limit (31.2% of traffic)
- **Homepage:** ❌ Failing LCP (6.9% of traffic)
- **Search Pages:** ❌ Failing CLS (2.5% of traffic)

---

## Core Web Vitals by Page Type

### Homepage (Index)

**Field Data (75th Percentile):**
- **LCP:** 3.57s ❌ **FAILING** (Target: < 2.5s)
- **CLS:** 0.01 ✅ **PASSING** (Target: < 0.10)
- **INP:** 152ms ✅ **PASSING** (Target: < 200ms)
- **FCP:** 1.58s ✅ **PASSING** (Target: < 1.8s)
- **TTFB:** 544ms ✅ **PASSING** (Target: < 800ms)

**Synthetic Data:**
- **LCP:** 3.6s ❌
- **CLS:** 0.01 ✅
- **INP:** 152ms ✅ (matches field data)

**Page Loads:** 199,154 (6.9% of total traffic)

**Analysis:**
The homepage LCP of 3.57s exceeds Google's threshold by 43%. Real-user data confirms synthetic test results. The primary bottleneck is hero image rendering. All other metrics are within acceptable ranges, indicating the issue is specific to image optimization rather than overall page performance.

**User Impact (Distribution):**
- **Good:** 62,336 users (31.3%)
- **Needs Improvement:** 34,843 users (17.5%)
- **Poor:** 15,189 users (7.6%)

**Trend:** LCP values fluctuated between 3.8s → 3.6s (July–October) with slight improvement.

**Root Cause:**
- Hero banners not optimized (> 2 MB each)
- Images served at ~2800px width
- No WebP/AVIF conversion
- Missing responsive image sources
- LCP image not preloaded

---

### Product Pages (PDP)

**Field Data (75th Percentile):**
- **LCP:** 1.66s ✅ **PASSING** (Target: < 2.5s)
- **CLS:** 0.04 ✅ **PASSING** (Target: < 0.10)
- **INP:** 192ms ✅ **PASSING** (Target: < 200ms)

**Synthetic Data (Mobile):**
- **LCP:** 8.71s ❌ **FAILING** (Target: < 2.5s)
- **CLS:** 0.334 ❌ **FAILING** (Target: < 0.10)
- **TBT:** 1.18s ❌ **HEAVY** (Target: < 0.30s)
- **FCP:** 3.1s

**Synthetic Data (Desktop):**
- **LCP:** 2.43s ✅ **PASSING**
- **CLS:** 0.078 ✅ **PASSING**
- **TBT:** 0.63s ⚠️ **ELEVATED**

**Page Loads:** 1,626,559 (56.6% of total traffic)

**Analysis:**
Field data shows product pages perform well for real users (LCP 1.66s). However, synthetic mobile testing reveals severe performance issues (LCP 8.71s), suggesting mobile-specific optimization problems. The discrepancy indicates that:
1. Real users may benefit from cached resources
2. Mobile first-load experience is poor
3. Desktop performance is acceptable but script-heavy

**User Impact (Distribution):**
- **LCP:** Good: 449,025 (27.6%), Needs Improvement: 402,835 (24.8%), Poor: 31,124 (1.9%)
- **CLS:** Good: 511,302 (31.4%), Needs Improvement: 419,355 (25.8%), Poor: 25,026 (1.5%)
- **INP:** Good: 325,477 (20.0%), Needs Improvement: 251,344 (15.5%), Poor: 12,069 (0.7%)

**Mobile Issues:**
- LCP > 8s suggests hero imagery and variant/zoom scripts delay rendering
- CLS > 0.3 indicates layout shifts from late-loading product media
- TBT 1.18s shows heavy main-thread blocking

**Root Causes:**
- Product gallery images > 3 MB
- Heavy JS bundles for variant selectors & reviews
- Late-loading reviews and sticky CTA bars causing layout shifts
- Large inline CSS in theme.css

---

### Collection Pages (PLP)

**Field Data (75th Percentile):**
- **LCP:** 2.07s ✅ **PASSING** (Target: < 2.5s) - *Near limit*
- **CLS:** 0.11 ❌ **FAILING** (Target: < 0.10)
- **INP:** 160ms ✅ **PASSING** (Target: < 200ms)
- **FCP:** 1.28s ✅ **PASSING** (Target: < 1.8s)
- **TTFB:** 256ms ✅ **PASSING** (Target: < 800ms)

**Synthetic Data:**
- **LCP:** 2.1s ✅
- **CLS:** 0.03 ✅
- **INP:** 185ms ✅

**Page Loads:** 897,082 (31.2% of total traffic)

**Analysis:**
Collection pages perform well overall, with LCP narrowly meeting the threshold. However, field data shows CLS at 0.11, slightly exceeding the threshold. The discrepancy between field (0.11) and synthetic (0.03) data suggests real-user conditions experience more layout shifts, possibly due to:
- Dynamic content loading
- Third-party widget injection
- User interaction patterns

**User Impact (Distribution):**
- **Good:** 326,813 users (36.5%)
- **Needs Improvement:** 270,296 users (30.2%)
- **Poor:** 34,675 users (3.9%)

**Trend:** Stable across July → October (± 0.1s variance in LCP).

**Root Causes:**
- Product thumbnails unoptimized (1.2 MB avg)
- Filter/sort interactions causing layout reflows
- Analytics scripts loading in head blocking main thread

---

### Search Pages

**Field Data (75th Percentile):**
- **LCP:** 1.99s ✅ **PASSING** (Target: < 2.5s)
- **CLS:** 0.40 ❌ **FAILING** (Target: < 0.10)
- **INP:** 176ms ✅ **PASSING** (Target: < 200ms)

**Synthetic Data:**
- **LCP:** 1.99s ✅
- **CLS:** 0.40 ❌
- **INP:** 176ms ✅

**Page Loads:** 71,997 (2.5% of total traffic)

**Analysis:**
Search pages have severe CLS issues (0.40–0.41), four times the acceptable threshold. LCP and INP are within acceptable ranges, indicating the issue is specific to layout stability during search results rendering.

**User Impact (Distribution):**
- **Good:** 27,610 users (38.3%)
- **Needs Improvement:** 14,079 users (19.5%)
- **Poor:** 10,428 users (14.5%)

**Root Causes:**
- Search results layout not reserved before content loads
- Dynamic result injection causing layout shifts
- SearchSpring integration causing layout instability

---

### Other Page Types

**Regular Pages:**
- **LCP:** 2.80s ⚠️ (Near limit)
- **CLS:** 0.02 ✅
- **INP:** 128ms ✅
- **Page Loads:** 66,006 (2.3% of traffic)

**Cart Pages:**
- **LCP:** 2.48s ✅
- **CLS:** 0.03 ✅
- **INP:** 128ms ✅
- **Page Loads:** 1,806 (0.1% of traffic)

**404 Pages:**
- **LCP:** 1.72s ✅
- **CLS:** 0.01 ✅
- **INP:** 136ms ✅
- **Page Loads:** 6,471 (0.2% of traffic)

---

## URL-Level Performance Insights

### High CLS Collections (Requiring Attention)

Specific collection pages show CLS values significantly above the 0.10 threshold:

**Critical (CLS > 0.15):**
- `/collections/sale` - **CLS 0.18** (26,779 page loads, 0.9% of traffic)
- `/collections/womens-wrestling-shoes` - **CLS 0.15** (19,339 page loads, 0.7% of traffic)
- `/collections/wrestling-gear` - **CLS 0.16** (13,429 page loads, 0.5% of traffic)
- `/collections/men-singlets` - **CLS 0.16** (9,524 page loads, 0.3% of traffic)
- `/collections/hoodies-pullovers-youth` - **CLS 0.24** (4,369 page loads, 0.2% of traffic)
- `/collections/coming-soon` - **CLS 0.42** (3,096 page loads, 0.1% of traffic)
- `/collections/collegiate` - **CLS 0.41** (1,897 page loads, 0.1% of traffic)

**High-Traffic Collections:**
- `/collections/wrestling-shoes` - **CLS 0.14** (150,764 page loads, 5.3% of traffic) - *Largest collection by traffic*
- `/collections/youth-wrestling-shoes` - **CLS 0.08** ✅ (56,988 page loads, 2.0% of traffic)

**Analysis:**
The `/collections/wrestling-shoes` page (largest collection by volume) has CLS 0.14, exceeding the threshold. Sale pages and coming-soon collections show the highest CLS values, likely due to dynamic pricing displays and promotional banner injection. These pages should be prioritized for layout stability fixes.

### Product Pages with CLS Issues

- `/products/rudis-mens-elite-singlet-custom1` - **CLS 0.18** (5,245 page loads)
- `/products/jb1-adult-wrestling-shoes-ice-blue` - **CLS 0.11** (14,122 page loads)
- `/products/jb1-adult-wrestling-shoes-gum-doubles` - **CLS 0.10** (9,854 page loads)

**Note:** Most product pages have acceptable CLS values (0.02–0.04), indicating the issue is specific to certain product templates or configurations.

---

## Performance Optimization Roadmap

### Priority 1: Do Now (Critical)

#### 1. Optimize Homepage Hero Images

**Goal:** Reduce homepage LCP from 3.57s to < 2.5s

**Actions:**
- Convert hero and banner images to WebP/AVIF formats (~70% size reduction)
- Implement responsive `<picture>` elements with multiple sources:
  - 1200px for desktop
  - 800px for tablet
  - 400px for mobile
- Preload LCP image in `<head>`:
  ```html
  <link rel="preload" as="image" href="[hero-image-url]" fetchpriority="high">
  ```
- Resize images to device-appropriate dimensions (current: ~2800px wide)
- Implement `loading="eager"` for LCP image, `loading="lazy"` for below-fold images

**Expected Impact:** LCP reduction from 3.57s to ~2.0s

**Files to Modify:**
- `sections/animated-hero.liquid`
- `sections/image-banner.liquid`
- `sections/banner-grid.liquid`
- `layout/theme.liquid` (for preload)

---

#### 2. Fix Collection Page CLS

**Goal:** Reduce collection page CLS from 0.11 to < 0.10

**Actions:**
- Reserve layout space for product grid containers (fixed height or aspect ratio)
- Implement skeleton loaders for product cards
- Debounce filter/sort click events to reduce DOM reflows
- Remove forced synchronous layout reflows
- Preload product thumbnail images
- **Priority fix for `/collections/wrestling-shoes`** (CLS 0.14, 5.3% of traffic)
- **Fix high-CLS collections:** sale (0.18), womens-wrestling-shoes (0.15), wrestling-gear (0.16), men-singlets (0.16)

**Expected Impact:** CLS reduction from 0.11 to ~0.05

**Files to Modify:**
- `sections/main-collection-product-grid.liquid`
- `sections/main-collection-product-grid-native.liquid`
- `sections/main-collection-product-grid-ss.liquid`
- `snippets/product-card.liquid`

---

#### 3. Optimize Search Results Layout

**Goal:** Reduce search page CLS from 0.40 to < 0.10

**Actions:**
- Reserve layout space for search results container
- Implement fixed-height containers for result cards
- Optimize SearchSpring integration to reduce layout shifts
- Add skeleton loaders during search execution

**Expected Impact:** CLS reduction from 0.40 to ~0.08

**Files to Modify:**
- `sections/main-search.liquid`
- `sections/main-search-native.liquid`
- `sections/searchspring-recommendations.liquid`

---

### Priority 2: Do Next (High)

#### 4. Optimize Product PDP Mobile Performance

**Goal:** Reduce mobile PDP LCP from 8.71s to < 2.5s

**Actions:**
- Optimize product gallery assets:
  - Convert all 1100px images to WebP/AVIF
  - Implement responsive `<picture>` tags
  - Lazy-load non-primary images after interaction
- Fix layout shift sources:
  - Add static height placeholders for review blocks
  - Reserve space for sticky CTA bars
  - Preload fonts and main product image
- Reduce main-thread blocking:
  - Split large JS bundles (`theme.js`, review widgets, analytics)
  - Defer scripts until interaction
  - Code-split variant selection logic

**Expected Impact:** Mobile LCP reduction from 8.71s to ~2.5s

**Files to Modify:**
- `sections/main-product.liquid`
- `sections/main-product-shoe.liquid`
- `sections/main-shoe-product.liquid`
- `snippets/product-media-gallery.liquid`
- `assets/theme.js` (bundle splitting)

---

#### 5. Optimize Product Thumbnails

**Goal:** Reduce collection page product thumbnail size from 1.2 MB avg

**Actions:**
- Convert product thumbnails to WebP/AVIF formats
- Implement `srcset` for responsive images
- Reduce default thumbnail size to 400px width
- Lazy-load thumbnails below the fold

**Expected Impact:** Faster collection page load times, reduced bandwidth

**Files to Modify:**
- `snippets/product-card.liquid`
- `snippets/product-thumbnail.liquid`

---

#### 6. Defer Non-Critical JavaScript

**Goal:** Reduce Total Blocking Time (TBT)

**Actions:**
- Audit `theme.js` bundle and split into critical/non-critical chunks
- Defer analytics scripts (GA4, Elevar, CQL)
- Defer wishlist scripts until interaction
- Defer third-party widgets (Yotpo, SearchSpring, etc.) until after initial render
- Use `async` or `defer` attributes appropriately

**Expected Impact:** TBT reduction from 1.18s to < 0.30s

**Files to Modify:**
- `layout/theme.liquid`
- `assets/theme.js`
- `snippets/elevar-head.liquid`
- `snippets/cql-head-content.liquid`

---

### Priority 3: Do Later (Medium)

#### 7. Optimize Font Loading

**Goal:** Reduce First Contentful Paint (FCP) and eliminate FOIT

**Actions:**
- Preload critical fonts (Barlow, Barlow Condensed)
- Implement `font-display: swap` for all fonts
- Reduce number of font weights loaded
- Use `preconnect` for font CDNs (already implemented)

**Expected Impact:** FCP improvement, reduced FOIT

**Files to Modify:**
- `layout/theme.liquid`
- CSS font declarations

---

#### 8. Optimize CSS Delivery

**Goal:** Reduce render-blocking CSS

**Actions:**
- Extract critical above-the-fold CSS (≤ 14 kB)
- Inline critical CSS in `<head>`
- Async-load remaining CSS
- Review and optimize `base.css` and component CSS files

**Expected Impact:** Faster FCP, reduced render-blocking time

**Files to Modify:**
- `layout/theme.liquid`
- `assets/base.css`
- Component CSS files

---

#### 9. Review Third-Party Widget Loading

**Goal:** Reduce impact of third-party widgets on performance

**Actions:**
- Audit third-party widgets (Affirm, Trustpilot, Loop Returns, Yotpo)
- Implement async loading strategies
- Consider lazy-loading below-the-fold widgets
- Review widget bundle sizes and optimization opportunities

**Expected Impact:** Reduced main-thread blocking, faster page loads

**Files to Review:**
- `snippets/yotpo-*.liquid`
- Third-party widget integrations
- `layout/theme.liquid` (widget loading)

---

## Performance Monitoring

### Tools & Metrics

**Primary Monitoring:**
- **Calibre CRUX Dashboard** - Real user monitoring (field data)
- **Google PageSpeed Insights** - Synthetic testing
- **Lighthouse** - Performance audits

**Key Metrics to Track:**
- LCP by page type (target: < 2.5s)
- CLS by page type (target: < 0.10)
- INP by page type (target: < 200ms)
- TBT (target: < 0.30s)
- FCP (target: < 1.8s)

### Monitoring Schedule

**Weekly:**
- Review Core Web Vitals trends
- Check for performance regressions
- Monitor field data vs synthetic data discrepancies

**Monthly:**
- Comprehensive performance audit
- Review optimization roadmap progress
- Update performance baselines

**Quarterly:**
- Full performance review
- Strategy updates based on trends
- New optimization opportunities

---

## Success Metrics

### Target Metrics

**Homepage:**
- LCP: < 2.5s (currently 3.57s)
- CLS: < 0.10 (currently 0.01) ✅
- INP: < 200ms (currently 152ms) ✅

**Product Pages:**
- LCP: < 2.5s (field: 1.66s ✅, mobile synthetic: 8.71s ❌)
- CLS: < 0.10 (field: 0.04 ✅, mobile synthetic: 0.334 ❌)
- INP: < 200ms (field: 192ms ✅)

**Collection Pages:**
- LCP: < 2.5s (currently 2.07s ✅)
- CLS: < 0.10 (currently 0.11 ❌)
- INP: < 200ms (currently 160ms ✅)

**Search Pages:**
- LCP: < 2.5s (currently 1.99s ✅)
- CLS: < 0.10 (currently 0.40 ❌)
- INP: < 200ms (currently 176ms ✅)

---

## References

- **Performance Reports:** `data/shopify-reports/`
- **Homepage Audit:** `prework/rudis-homepage-audit.md`
- **PLP Audit:** `prework/rudis-plp-audit.md`
- **PDP Audit:** `prework/rudis-pdp-audit.md`
- **Issues & Recommendations:** `prework/RUDIS Website Audit – Issues & Recommendations.md`

---

_This documentation is based on Shopify CRUX field data (August 2 - October 31, 2025, 75th percentile) and synthetic Lighthouse/PageSpeed Insights data from October 2025. Field data includes 2,877,161 total page loads across all page types._

