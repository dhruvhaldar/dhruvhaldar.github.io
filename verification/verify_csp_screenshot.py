from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            # Navigate to index.html (with redirect disabled if possible, but here we just want to load the page content and see if favicon works?)
            # Actually, to screenshot the spinner, we need to be fast or disable redirect.
            # But I cannot modify the file now as I'm in pre-commit verification.
            # I'll just load the page. The redirect takes 0 seconds in meta.
            # So I might end up on vercel.app.
            # I'll block the redirect using route abort.

            page.route("**/*", lambda route: route.abort() if "dhruvhaldar.vercel.app" in route.request.url else route.continue_())

            page.goto("http://localhost:8080/index.html")

            # Wait a bit
            page.wait_for_timeout(1000)

            # Take screenshot
            page.screenshot(path="verification/csp_fix.png")
            print("Screenshot taken.")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run()
