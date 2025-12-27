from playwright.sync_api import sync_playwright
import os

def verify_favicon():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Create context with java_script_enabled=False to prevent redirect
        context = browser.new_context(java_script_enabled=False)
        page = context.new_page()

        # We can also rely on the meta refresh, which is 0 seconds.
        # But maybe disabling JS is enough to inspect the initial DOM for the link tag?
        # The meta refresh might still trigger.

        # Let's try to fetch the content using python request if playwright fails?
        # But Playwright sees the DOM.

        try:
            print("Navigating to index.html...")
            # We use the local server
            page.goto("http://localhost:8080/index.html")
            # Wait for element? No, it's static.
        except Exception as e:
            print(f"Navigation interrupted: {e}")

        # Check for the link tag
        icon_link = page.locator('link[rel="icon"]')
        count = icon_link.count()
        print(f"Found {count} icon links on index.html")

        if count > 0:
            href = icon_link.first.get_attribute("href")
            print(f"Icon href: {href}")
            if href == "data:;base64,iVBORw0KGgo=":
                print("SUCCESS: Favicon is present and correct.")
            else:
                print("FAILURE: Favicon href is incorrect.")
        else:
            print("FAILURE: Favicon link not found.")
            # Print page content to debug
            # print(page.content())

        page.screenshot(path="verification/index_favicon.png")

        browser.close()

if __name__ == "__main__":
    verify_favicon()
