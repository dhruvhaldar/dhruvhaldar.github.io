## 2024-05-23 - Resource Hint Ordering
**Learning:** Browsers process HTML sequentially. For redirect pages using `meta refresh`, placing `preconnect` and `dns-prefetch` tags *before* the `meta refresh` tag ensures that the DNS resolution and connection handshake start immediately, before the browser parses and executes the refresh directive. This is critical for minimizing the latency of client-side redirects.
**Action:** Always ensure resource hints like `preconnect` and `dns-prefetch` appear before any blocking meta tags or scripts that trigger navigation.
