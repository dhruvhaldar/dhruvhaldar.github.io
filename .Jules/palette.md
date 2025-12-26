## 2024-05-23 - Focus Styles on Redirect Pages
**Learning:** Redirect pages, while transient, can sometimes stall or fail, leaving keyboard users stranded without visible focus indicators on the only interactive element (the fallback link).
**Action:** Always include explicit `:focus` styles for fallback links on redirect pages, even if they are meant to be temporary. Use `outline` and `outline-offset` for high visibility.
