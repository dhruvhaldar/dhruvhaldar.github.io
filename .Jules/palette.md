## 2024-05-23 - [Enhanced Client-Side Redirects]
**Learning:** Static sites used as redirection layers often rely solely on meta-refresh, which can be slow or blocked. A JavaScript fallback (`window.location.replace`) significantly improves perceived performance. Visual feedback (spinner/message) reduces confusion during the transition.
**Action:** Always include a JS redirect alongside meta-refresh and ensure the intermediate page is styled and informative to prevent a "broken" feel.
