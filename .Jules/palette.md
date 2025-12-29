## 2025-12-27 - Reduced Motion in Loading States
**Learning:** Animations like spinning loaders can trigger vestibular disorders. Always wrap continuous animations in `@media (prefers-reduced-motion: reduce)` to respect user preferences.
**Action:** When adding animations, simultaneously add the reduced motion media query to disable or simplify them.
