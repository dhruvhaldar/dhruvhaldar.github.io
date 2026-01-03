from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = "http://localhost:8000/verification/test.html"
        print(f"Navigating to {url}")

        try:
            page.goto(url)

            # Wait for spinner - this proves styles are applied (via size/border)
            page.wait_for_selector(".spinner", state="visible", timeout=3000)

            # Check computed style
            spinner = page.locator(".spinner")
            style = spinner.evaluate("el => getComputedStyle(el).borderTopColor")
            print(f"Spinner border-top-color: {style}")

            page.screenshot(path="verification/success.png")
            print("Verified successfully.")

        except Exception as e:
            print(f"Verification failed: {e}")
            page.screenshot(path="verification/failed_visuals.png")

        browser.close()

if __name__ == "__main__":
    run()
