from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = "http://localhost:8000/index.html"
        print(f"Navigating to {url}")

        # Block the redirect to seeing the page content
        page.route("https://dhruvhaldar.vercel.app/**", lambda route: route.abort())

        try:
            page.goto(url)
        except Exception as e:
            print(f"Navigation error: {e}")

        # Check for CSP violation errors in console
        page.on("console", lambda msg: print(f"Console: {msg.text}") if "Security" in msg.text or "CSP" in msg.text else None)

        try:
            # Wait for spinner or text
            page.wait_for_selector(".spinner", state="visible", timeout=5000)

            # Check if styles are applied
            spinner = page.locator(".spinner")
            border_top_color = spinner.evaluate("el => getComputedStyle(el).borderTopColor")
            print(f"Spinner Border Top Color: {border_top_color}")

            page.screenshot(path="verification/index_screenshot.png")
            print("Screenshot taken.")
        except Exception as e:
            print(f"Verification failed: {e}")
            page.screenshot(path="verification/failure.png")

        browser.close()

if __name__ == "__main__":
    run()
