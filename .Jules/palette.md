## 2025-12-27 - Consistent Accessibility Attributes
**Learning:** In a static site with many similar redirect pages, accessibility attributes like `title` on links or `aria-label` must be consistently applied across all files, not just the root. Inconsistencies can be flagged by automated tests and confuse users relying on assistive technology.
**Action:** When modifying a recurring pattern (like a redirect template), use a script to ensure the change is propagated to all instances of that pattern, and verify consistency programmatically.

## 2025-12-27 - Reduced Motion in Static Sites
**Learning:** Even simple redirect pages with spinners need to respect `prefers-reduced-motion`. Users with vestibular disorders may experience discomfort even during a short redirect.
**Action:** Always include a `@media (prefers-reduced-motion: reduce)` block to disable or replace animations in loading states, even for static sites.
