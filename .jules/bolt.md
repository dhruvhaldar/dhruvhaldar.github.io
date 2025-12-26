## 2024-05-23 - [Static Redirect Optimization]
**Learning:** The codebase consists of static HTML files performing client-side redirects to `https://dhruvhaldar.vercel.app/`.
**Insight:** While root and top-level pages use `preconnect` and `window.location.replace`, deeper pages (e.g., in `blog/`) lack these optimizations, relying solely on `meta refresh`.
**Action:** Standardize all redirect pages to include `preconnect` resource hints and `window.location.replace` scripts for faster navigation.

## 2024-05-23 - [DNS Prefetch Standardization]
**Learning:** Browser connectivity optimizations like `dns-prefetch` were inconsistently applied.
**Insight:** While root pages had both `preconnect` and `dns-prefetch`, deep pages in `blog/` only had `preconnect`. Adding `dns-prefetch` provides a fallback and ensures earlier DNS resolution.
**Action:** Always include both `preconnect` and `dns-prefetch` for external redirect targets to maximize connection speed across all browsers.

## 2025-05-21 - [Invalid Header Cleanup]
**Learning:** The `Permissions-Policy` header cannot be set via a `<meta>` tag.
**Insight:** The presence of `<meta http-equiv="Permissions-Policy" ...>` is invalid and adds unnecessary bytes to the payload. Removing it reduces the size of all redirect pages.
**Action:** Ensure `Permissions-Policy` is only set via HTTP headers if needed, and never in static HTML meta tags.