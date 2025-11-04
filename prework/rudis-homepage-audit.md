# RUDIS Website Audit – Homepage (with Calibre CRUX Integration)

**Client:** RUDIS  
**Environment:** Live  
**Auditor:** Arcadia Digital (ChatGPT Atlas)  
**Date:** October 22, 2025  

This audit merges:
- **Lighthouse / PageSpeed synthetic results**
- **Accessibility findings (WCAG 2.2 AA)**
- **Calibre CRUX field data for Homepage (3-month window, 75th percentile)**

---

## ⚙️ 1. Core Web Vitals (Merged Field + Synthetic)

| Metric | Field (CRUX 75th %) | Synthetic (Lighthouse/PSI) | Target | Assessment | Status |
|:--|:--:|:--:|:--:|:--:|:--:|
| **LCP (Largest Contentful Paint)** | **3.77 s** | 3.6 s | < 2.5 s | Slow – needs improvement | ❌ |
| **CLS (Cumulative Layout Shift)** | **0.00** | 0.00 | < 0.10 | Excellent – stable layout | ✅ |
| **INP (Interaction to Next Paint)** | **178 ms** | 179 ms | < 200 ms | Responsive interactions | ✅ |
| **FCP (First Contentful Paint)** | **1.58 s** | 1.6 s | < 1.8 s | Good | ✅ |
| **TTFB (Time to First Byte)** | **544 ms** | 600 ms | < 800 ms | Acceptable | ✅ |
| **RTT (Round Trip Time)** | **120 ms** | – | < 150 ms | Strong network performance | ✅ |

**Interpretation:**  
Real-user data confirms that the **homepage LCP is slow (3.77 s)**, failing Google’s Core Web Vitals threshold. All other metrics fall comfortably within “good” ranges, indicating that the bottleneck is image rendering on first paint rather than interactivity or network latency.

---

## 🧩 2. Field Data Summary (Calibre CRUX)
- **Time window:** Last 3 months  
- **Form Factor:** Mobile (Phone)  
- **Overall Assessment:** **Failing – LCP beyond 2.5 s threshold**  
- **Trend:** LCP values fluctuated between 3.8 s → 3.7 s (Jul–Oct) with no material improvement.  
- **CLS, INP, FCP, TTFB** remained consistently in the green bands.  

---

## 🧮 3. Key Accessibility Observations (WCAG 2.2 AA)
| Principle | Violations | Target | Notes |
|:--|:--:|:--:|:--|
| **Perceivable** | 4 | ≤ 2 | Missing alt text on hero and product images |
| **Operable** | 1 | ≤ 1 | Cookie banner focus traps |
| **Understandable** | 1 | ≤ 1 | Redundant labels in mega-menu |
| **Robust** | 1 | ≤ 1 | Inconsistent ARIA roles in navigation |

**Accessibility Score:** ≈ 89 % (axe) **Target:** ≥ 95 %

---

## 📊 4. Thematic Breakdown
| Category | Finding | Impact | Recommendation | Priority |
|:--|:--|:--|:--|:--:|
| **Images** | Hero banners not optimized (> 2 MB each) | High | Convert to AVIF/WebP and preload LCP image | 🔴 |
| **Scripts** | Non-critical JS blocking render | High | Defer/async non-critical scripts | 🟠 |
| **Fonts** | FOIT visible on first paint | Medium | Preload critical fonts + `font-display:swap` | 🟡 |
| **Accessibility** | Empty `alt` attributes | High | Add descriptive alts to hero + product images | 🔴 |
| **SEO** | Incomplete meta descriptions | Medium | Add descriptive meta summaries per page | 🟡 |

---

## 🔍 5. Action Plan (Developer Handoff)

### **A. Do Now**
1. **Compress hero and banner images**  
   - Convert to WebP/AVIF (~70 % size reduction).  
   - Implement responsive `<picture>` sources (1200 px / 800 px / 400 px).  
   - Preload the LCP image in `<head>`.  
2. **Add meaningful alt attributes**  
   - Tie alt text to product metadata via Liquid/Shopify template variables.  
3. **Defer non-critical JS**  
   - Audit `theme.js` bundle; defer analytics and wishlist scripts.  
4. **Audit cookie banner for keyboard focus**  
   - Ensure `aria-modal="true"` + focus trap with Esc dismissal.

### **B. Do Next**
1. **Improve navigation accessibility**  
   - Add `role="menu"`/`menuitem` + visible focus styles.  
2. **Optimize critical CSS delivery**  
   - Inline above-the-fold CSS (~14 kB max).  
3. **Monitor Calibre Pulse for LCP trend reduction below 2.5 s.**

### **C. Do Later**
1. **Semantic headings review** (`h1 → h3` hierarchy).  
2. **Refine accordion ARIA states** on PDP panels.

### **D. Don’t Do**
- Avoid changing collection and PDP asset pipelines that already achieve < 2.1 s LCP.

---

## 🧩 6. Summary & Recommendations
**Overall Grade:** **B (Performance) / B+ (Accessibility)**  
**Key Insights:**
1. Field data confirms real users experience slow LCP on homepage.  
2. All other Web Vitals are excellent.  
3. Accessibility gaps remain minor but systemic (alt text, cookie modal).  

**Next Audit:** Q1 2026 (after hero image optimization).

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

**© 2025 Arcadia Digital** | *Audit generated via ChatGPT Atlas + Calibre CRUX Dashboard*
