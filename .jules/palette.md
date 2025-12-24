## 2025-05-23 - CSP Hash Calculation Sensitivity
**Learning:** CSP SHA-256 hash calculation is extremely sensitive to whitespace. When calculating a hash for inline styles or scripts, the content must match *exactly* what is served in the HTML, including all leading/trailing newlines and indentation.
**Action:** Always calculate the hash from the *final string* that will be injected into the HTML template, rather than a cleaned-up version of the code. Using a script to generate both the file content and the hash simultaneously ensures consistency.
