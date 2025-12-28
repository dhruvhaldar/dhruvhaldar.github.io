## 2025-12-27 - Consistent Accessibility Attributes
**Learning:** In a static site with many similar redirect pages, accessibility attributes like `title` on links or `aria-label` must be consistently applied across all files, not just the root. Inconsistencies can be flagged by automated tests and confuse users relying on assistive technology.
**Action:** When modifying a recurring pattern (like a redirect template), use a script to ensure the change is propagated to all instances of that pattern, and verify consistency programmatically.

## 2025-12-27 - Respecting Reduced Motion
**Learning:** Loading spinners and animations can trigger vestibular disorders. Always include a `@media (prefers-reduced-motion: reduce)` query to disable or simplify animations for users who have requested reduced motion in their system settings.
**Action:** Implement `animation: none` or a gentle fade/pulse alternative inside a `prefers-reduced-motion` media query for all animated elements.
