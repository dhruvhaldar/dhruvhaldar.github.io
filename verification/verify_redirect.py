from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Disable JS to stop immediate redirect so we can see the spinner/fallback
        # Actually, redirect happens via <script> and <meta>.
        # If I disable JS, I can see the fallback content?
        # The content is always there, JS just redirects.
        # But <meta refresh> might also trigger.
        # I'll try to capture it quickly or use a file url.

        # Note: Playwright file:// access might be restricted or behave differently with CSP.
        # I'll use a local http server.

        page = browser.new_page()

        # Navigate to index.html served via python http.server (I need to start it first)
        # Alternatively, I can load the content directly.
        # Let's try file URI first.
        import os
        cwd = os.getcwd()
        filepath = f"file://{cwd}/index.html"

        print(f"Navigating to {filepath}")

        # Block the redirect to seeing the page content
        # We can route the destination URL to abort.
        page.route("https://dhruvhaldar.vercel.app/**", lambda route: route.abort())

        try:
            page.goto(filepath)
        except Exception as e:
            print(f"Navigation error (expected due to abort): {e}")

        # Wait for spinner or text
        # The spinner is .spinner
        page.wait_for_selector(".spinner", state="visible", timeout=5000)

        # Check if styles are applied (e.g. spinner has border)
        spinner = page.locator(".spinner")
        border_top_color = spinner.evaluate("el => getComputedStyle(el).borderTopColor")
        print(f"Spinner Border Top Color: {border_top_color}")

        # If CSS is broken (hash mismatch), the spinner won't be styled or visible properly.
        # Default border color without CSS would be nothing (div has no size).
        # So if we see it, CSS works.

        page.screenshot(path="verification/index_screenshot.png")
        print("Screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
