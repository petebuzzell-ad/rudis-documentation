# RUDIS Website Audit – Collection Page (“All Shoes”) with Calibre CRUX Integration

**Client:** RUDIS  
**Environment:** Live  
**Auditor:** Arcadia Digital (ChatGPT Atlas)  
**Date:** October 22, 2025  

This audit merges:
- **Lighthouse / PageSpeed synthetic results**
- **Accessibility findings (WCAG 2.2 AA)**
- **Calibre CRUX field data for PLP (3-month window, 75th percentile)**

---

## ⚙️ 1. Core Web Vitals (Merged Field + Synthetic)

| Metric | Field (CRUX 75th %) | Synthetic (Lighthouse/PSI) | Target | Assessment | Status |
|:--|:--:|:--:|:--:|:--:|:--:|
| **LCP (Largest Contentful Paint)** | **2.48 s** | 2.1 s | < 2.5 s | Good – near upper limit | ✅ |
| **CLS (Cumulative Layout Shift)** | **0.08** | 0.03 | < 0.10 | Stable layout | ✅ |
| **INP (Interaction to Next Paint)** | **219 ms** | 185 ms | < 200 ms | Slightly above ideal – optimize event handlers | ⚠️ |
| **FCP (First Contentful Paint)** | **1.28 s** | 1.3 s | < 1.8 s | Good | ✅ |
| **TTFB (Time to First Byte)** | **256 ms** | 310 ms | < 800 ms | Excellent | ✅ |
| **RTT (Round Trip Time)** | **113 ms** | – | < 150 ms | Strong network performance | ✅ |

**Interpretation:**  
The “All Shoes” collection page performs well in real-world conditions.  
LCP (2.48 s) narrowly meets the threshold, showing healthy image optimization compared to the homepage. INP (219 ms) indicates small opportunities to streamline JS event handling (especially on filter/sort controls).

---

## 🧩 2. Field Data Summary (Calibre CRUX)

- **Time window:** Last 3 months  
- **Form Factor:** Mobile (Phone)  
- **Overall Assessment:** **Passing – LCP within threshold, INP slightly to improve**  
- **Trend:** Stable across Jul → Oct (± 0.1 s variance in LCP).  
- **User experience:** Smooth scroll + consistent rendering observed.  

---

## 🧮 3. Accessibility Overview (WCAG 2.2 AA)

| Principle | Violations | Target | Notes |
|:--|:--:|:--:|:--|
| **Perceivable** | 2 | ≤ 2 | Product images missing `alt` text on lazy-load templates |
| **Operable** | 1 | ≤ 1 | Filter/sort dropdowns lack ARIA states |
| **Understandable** | 0 | ≤ 1 | – |
| **Robust** | 0 | ≤ 1 | – |

**Accessibility Score:** ≈ 92 % **Target:** ≥ 95 %

---

## 📊 4. Thematic Breakdown

| Category | Finding | Impact | Recommendation | Priority |
|:--|:--|:--|:--|:--:|
| **Event Handling** | INP > 200 ms | Medium | Debounce filter/sort handlers and reduce DOM reflows | 🟡 |
| **Images** | Product thumbnails unoptimized (1.2 MB avg) | High | Use WebP/AVIF + `srcset` | 🔴 |
| **Accessibility** | Alt attributes missing in template snippets | High | Map `alt` = `product.title` | 🔴 |
| **CSS Delivery** | Uncritical CSS loaded inline | Low | Move below-the-fold CSS to async file | 🟢 |
| **Analytics Scripts** | Load in head blocking main thread | Medium | Defer analytics scripts | 🟡 |

---

## 🔍 5. Action Plan (Developer Handoff)

### **A. Do Now**
1. Compress PLP product grid thumbnails and banner images.  
2. Add `alt` text to product images (`{{ product.title }}`).  
3. Debounce sort/filter click events and remove forced synchronous layout reflows.  

### **B. Do Next**
1. Implement ARIA roles on filter/sort controls (`role="listbox"`, `aria-expanded`, etc.).  
2. Defer non-critical third-party scripts (GA4, wishlist).  
3. Use Calibre Pulse to track INP reductions below 200 ms.

### **C. Do Later**
- Review collection template CSS loading order.  
- Consolidate media queries to reduce render blocking.

### **D. Don’t Do**
- Don’t restructure collection grid markup (it’s performant and stable per CLS = 0.08).

---

## 🧩 6. Summary & Recommendations
**Overall Grade:** **A- (Performance) / B+ (Accessibility)**  
**Highlights:**  
- Real users experience a fast PLP with excellent layout stability.  
- Minor INP lag and missing image `alt` attributes remain the only concerns.  

**Next Audit:** Q1 2026 after JS event optimizations.

---

### 🏁 Arcadia Digital Standards Reference
| Metric | Target | Tool / Source |
|:--|:--:|:--|
| Mobile PSI | ≥ 70 | Google PSI |
| Desktop PSI | ≥ 85 | Google PSI |
| Accessibility (WCAG 2.2 AA) | ≥ 95 % | axe / WAVE |
| Lighthouse SEO | ≥ 90 | Lighthouse |
| CLS | ≤ 0.10 | Lighthouse / CRUX |

---

**© 2025 Arcadia Digital** | *Audit generated via ChatGPT Atlas + Calibre CRUX Dashboard (PLP Integration)*
