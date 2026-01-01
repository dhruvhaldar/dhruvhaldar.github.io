# Sentinel Journal

## 2025-02-19 - Content Security Policy for Static Redirects
**Vulnerability:** Missing Content Security Policy (CSP) headers on static redirect pages.
**Learning:** Even simple static redirect pages can benefit from CSP to prevent execution of unauthorized scripts if the HTML is compromised or if there are unexpected injection vectors in the future.
**Prevention:** Added a strict CSP meta tag to the main entry point to restrict script execution to inline scripts only (required for the redirect logic) and deny other resources by default.
## 2024-05-23 - Strict Referrer Policy and Invalid Meta Cleanup
**Vulnerability:** Inconsistent Referrer-Policy across subpages and invalid usage of Permissions-Policy in meta tags.
**Learning:** The `Permissions-Policy` header is not supported in HTML `<meta>` tags (unlike CSP), making its presence invalid and useless. Conversely, `Referrer-Policy` IS supported in meta tags and is critical for privacy in redirect scenarios.
**Prevention:** Ensure `<meta name="referrer" content="strict-origin-when-cross-origin">` is present on all pages. Remove any `<meta http-equiv="Permissions-Policy">`. Use automated checks (BeautifulSoup) to enforce this consistency.
## 2025-02-21 - CSP Hardening: base-uri and form-action
**Vulnerability:** Use of `base-uri 'self'` and `form-action 'self'` in purely static redirect pages.
**Learning:** Static redirect pages do not use `<base>` tags or forms. Allowing `'self'` unnecessarily expands the attack surface.
**Prevention:** Explicitly set `base-uri` and `form-action` to `'none'` in the Content Security Policy for all static pages to adhere to the principle of least privilege.
