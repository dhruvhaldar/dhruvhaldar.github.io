# Bolt's Journal

## 2024-05-22 - Redirect Performance
**Learning:** For static redirect pages, placing `dns-prefetch` and `preconnect` immediately after `meta charset` (and before `meta refresh`) ensures the browser starts resolving the destination before the redirect logic tears down the page context.
**Action:** Standardize all redirect templates to include these hints at the top of the `<head>`.
