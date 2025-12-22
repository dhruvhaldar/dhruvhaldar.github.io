# Sentinel Journal

## 2025-02-19 - Content Security Policy for Static Redirects
**Vulnerability:** Missing Content Security Policy (CSP) headers on static redirect pages.
**Learning:** Even simple static redirect pages can benefit from CSP to prevent execution of unauthorized scripts if the HTML is compromised or if there are unexpected injection vectors in the future.
**Prevention:** Added a strict CSP meta tag to the main entry point to restrict script execution to inline scripts only (required for the redirect logic) and deny other resources by default.
