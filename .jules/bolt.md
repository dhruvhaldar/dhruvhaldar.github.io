## 2024-05-23 - [Static Redirect Optimization]
**Learning:** The codebase consists of static HTML files performing client-side redirects to `https://dhruvhaldar.vercel.app/`.
**Insight:** While root and top-level pages use `preconnect` and `window.location.replace`, deeper pages (e.g., in `blog/`) lack these optimizations, relying solely on `meta refresh`.
**Action:** Standardize all redirect pages to include `preconnect` resource hints and `window.location.replace` scripts for faster navigation.

## 2024-05-23 - [DNS Prefetch Standardization]
**Learning:** Browser connectivity optimizations like `dns-prefetch` were inconsistently applied.
**Insight:** While root pages had both `preconnect` and `dns-prefetch`, deep pages in `blog/` only had `preconnect`. Adding `dns-prefetch` provides a fallback and ensures earlier DNS resolution.
**Action:** Always include both `preconnect` and `dns-prefetch` for external redirect targets to maximize connection speed across all browsers.
