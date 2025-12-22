## 2024-05-23 - [Static Redirect Optimization]
**Learning:** The codebase consists of static HTML files performing client-side redirects to `https://dhruvhaldar.vercel.app/`.
**Insight:** While root and top-level pages use `preconnect` and `window.location.replace`, deeper pages (e.g., in `blog/`) lack these optimizations, relying solely on `meta refresh`.
**Action:** Standardize all redirect pages to include `preconnect` resource hints and `window.location.replace` scripts for faster navigation.
