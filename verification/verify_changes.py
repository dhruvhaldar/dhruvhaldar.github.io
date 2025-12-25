from playwright.sync_api import sync_playwright
import os
import re

def verify_redirect_page(page, filepath, destination):
    # We need to temporarily remove the meta refresh and comment out the script
    # to inspect the page content without actually redirecting.
    # However, we want to verify the script is correct in the source.

    print(f"Verifying {filepath}...")

    # 1. Verify source code correctness (static check)
    with open(filepath, 'r') as f:
        content = f.read()

    if 'window.top.location.replace' not in content:
        raise Exception(f"Failed: {filepath} does not contain window.top.location.replace")

    # Check CSP hash matches script
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if not script_match:
        raise Exception(f"Failed: No script found in {filepath}")

    script_content = script_match.group(1)

    import hashlib
    import base64
    calculated_hash = base64.b64encode(hashlib.sha256(script_content.encode('utf-8')).digest()).decode('utf-8')

    if f"script-src 'sha256-{calculated_hash}'" not in content:
         # It might be using a different quote style or something, but our update script used exactly this format.
         # Let's check looser match
         if calculated_hash not in content:
             raise Exception(f"Failed: CSP hash for script not found in {filepath}")

    print(f"  Static checks passed for {filepath}")

    # 2. Visual verification (render the page)
    # To render the page without redirecting immediately, we can modify it temporarily
    # OR we can intercept the navigation request in Playwright.
    # Since it's a file:// URL, request interception is tricky.
    # Best way: modify the file to comment out the redirect, load it, screenshot, revert.

    temp_filepath = filepath + ".temp.html"

    # Create a version that doesn't redirect
    safe_content = content.replace('<meta http-equiv="refresh"', '<!-- <meta http-equiv="refresh"')
    safe_content = safe_content.replace('<script>window.top.location.replace', '<script>// window.top.location.replace')

    with open(temp_filepath, 'w') as f:
        f.write(safe_content)

    try:
        abs_path = os.path.abspath(temp_filepath)
        page.goto(f"file://{abs_path}")

        # Take screenshot
        page.screenshot(path=f"verification/screenshot_{os.path.basename(filepath)}.png")
        print(f"  Screenshot saved to verification/screenshot_{os.path.basename(filepath)}.png")

    finally:
        if os.path.exists(temp_filepath):
            os.remove(temp_filepath)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # Verify index.html
            verify_redirect_page(page, "index.html", "https://dhruvhaldar.vercel.app/")

            # Verify about/index.html
            verify_redirect_page(page, "about/index.html", "https://dhruvhaldar.vercel.app/about")

        finally:
            browser.close()
