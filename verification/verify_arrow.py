from playwright.sync_api import sync_playwright
import re
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Read the file and strip redirect logic
        with open("index.html", "r") as f:
            content = f.read()

        # Remove meta refresh
        content = re.sub(r'<meta[^>]*http-equiv="refresh"[^>]*>', '', content)
        # Remove script redirect
        content = re.sub(r'<script>window.location.replace.*?</script>', '', content)

        page.set_content(content)

        # Check if the text contains the arrow
        link = page.locator(".fallback-link")
        print(f"Link text: {link.inner_text()}")

        # Screenshot
        page.screenshot(path="verification/index_arrow.png")

        browser.close()

if __name__ == "__main__":
    run()
