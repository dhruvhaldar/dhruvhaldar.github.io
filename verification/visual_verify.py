from playwright.sync_api import sync_playwright

def verify_visuals():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the locally generated HTML
        # Using absolute path for safety
        import os
        cwd = os.getcwd()
        file_path = f"file://{cwd}/verification/sitemap_output.html"

        page.goto(file_path)

        # Wait for the table to be visible
        page.wait_for_selector("table")

        # Take a screenshot
        page.screenshot(path="verification/sitemap_visual.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_visuals()
