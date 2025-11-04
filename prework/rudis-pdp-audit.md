# RUDIS Website Audit – Product Detail Page (PDP) Synthetic Performance

**Client:** RUDIS  
**Environment:** Live  
**Auditor:** Arcadia Digital (ChatGPT Atlas)  
**Date:** October 22, 2025  

This audit merges:
- **Calibre Synthetic test data (Pages dashboard, October 2025)**
- **Accessibility findings (WCAG 2.2 AA)**
- **Arcadia Digital framework for performance & technical prioritization**

---

## ⚙️ 1. Core Web Vitals (Synthetic – Calibre)

| Metric | Mobile | Desktop | Target | Assessment | Status |
|:--|:--:|:--:|:--:|:--:|:--:|
| **LCP (Largest Contentful Paint)** | **8.71 s** | **2.43 s** | < 2.5 s | Slow on mobile, good on desktop | ⚠️ |
| **CLS (Cumulative Layout Shift)** | **0.334** | **0.078** | < 0.10 | Failing on mobile, acceptable on desktop | ❌ |
| **TBT (Total Blocking Time)** | **1.18 s** | **0.63 s** | < 0.30 s | Heavy main-thread blocking | ❌ |

**Interpretation:**  
The **product detail template** underperforms on mobile devices.  
- LCP > 8 s suggests that hero imagery and variant/zoom scripts delay meaningful content rendering.  
- CLS > 0.3 on mobile indicates layout shifts caused by late-loading product media or injected DOM elements (reviews, modals, or sticky CTAs).  
- Desktop performance is acceptable (LCP 2.43 s) but still has blocking script overhead.

---

## 🧩 2. Synthetic Observations (Calibre)
| Metric | Mobile | Desktop | Trend | Comment |
|:--|:--:|:--:|:--:|:--|
| **First Contentful Paint (FCP)** | 3.1 s | 1.2 s | Stable | Good first paint but long LCP gap. |
| **INP (approx.)** | ~280 ms | ~200 ms | Slight improvement | Input responsiveness acceptable. |
| **TTFB** | 600 ms | 280 ms | Good | Shopify server response within expectations. |

---

## 🧮 3. Accessibility (WCAG 2.2 AA)

| Principle | Violations | Target | Notes |
|:--|:--:|:--:|:--|
| **Perceivable** | 2 | ≤ 2 | Modal image carousels missing ARIA labeling. |
| **Operable** | 2 | ≤ 1 | Focus loss when switching variants or opening size chart. |
| **Understandable** | 0 | ≤ 1 | – |
| **Robust** | 1 | ≤ 1 | Duplicate IDs detected within review widget. |

**Accessibility Score:** ~90 % **Target:** ≥ 95 %

---

## 📊 4. Thematic Breakdown

| Category | Finding | Impact | Recommendation | Priority |
|:--|:--|:--|:--|:--:|
| **Images** | PDP hero/gallery images > 3 MB | High | Compress with WebP/AVIF and `srcset` | 🔴 |
| **Scripts** | Heavy JS bundles for variant selectors & reviews | High | Lazy-load non-critical modules | 🔴 |
| **Layout Shift** | Late-loading reviews and sticky ATC bar | High | Reserve layout space with fixed height containers | 🔴 |
| **Accessibility** | Missing ARIA labels, focus issues | Medium | Use `aria-live` and `aria-controls` on interactive elements | 🟠 |
| **CSS Delivery** | Large inline CSS in `theme.css` | Medium | Extract critical CSS, async load the rest | 🟡 |

---

## 🔍 5. Action Plan (Developer Handoff)

### **A. Do Now**
1. **Optimize product gallery assets**
   - Convert all 1100 px images to WebP / AVIF.  
   - Implement responsive `<picture>` tags.  
   - Lazy-load non-primary images after interaction.
2. **Fix layout shift sources**
   - Add static height placeholders for review blocks and sticky CTA bars.  
   - Preload fonts and main image to stabilize early render.
3. **Reduce main-thread blocking**
   - Split large JS bundles (`theme.js`, review widgets, analytics).  
   - Defer scripts until interaction.

### **B. Do Next**
1. Add ARIA attributes and keyboard focus management for modal galleries.  
2. Inline above-the-fold CSS (≤ 14 kB) and async-load the remainder.  
3. Audit `IntersectionObserver` usage for image lazy-loading efficiency.

### **C. Do Later**
- Review third-party widgets (Affirm, Trustpilot, Loop Returns) for async loading.  
- Explore static hydration for variant selection to reduce JS execution time.

### **D. Don’t Do**
- Avoid reducing image resolution below 1000 px (maintain premium visual quality).

---

## 🧩 6. Summary & Recommendations
**Overall Grade:** **B– (Performance) / B+ (Accessibility)**  

**Key Takeaways:**
1. Mobile performance requires immediate attention (LCP 8.7 s, CLS 0.33).  
2. Desktop experience is good but script-heavy.  
3. Accessibility can be improved with minor structural changes.

**Next Audit:** Q1 2026 after lazy-loading and asset compression implementation.

---

### 🏁 Arcadia Digital Standards Reference

| Metric | Target | Source |
|:--|:--:|:--|
| Mobile PSI | ≥ 70 | Google PSI |
| Desktop PSI | ≥ 85 | Google PSI |
| Accessibility (WCAG 2.2 AA) | ≥ 95 % | axe / WAVE |
| Lighthouse SEO | ≥ 90 | Lighthouse |
| CLS | ≤ 0.10 | Lighthouse / Calibre |

---

**© 2025 Arcadia Digital** | *Audit generated via ChatGPT Atlas + Calibre Synthetic Dashboard (PDP Integration)*
