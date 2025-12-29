from playwright.sync_api import sync_playwright

def verify_reduced_motion():
    with sync_playwright() as p:
        # Create a context with reduced motion enabled
        browser = p.chromium.launch()
        context = browser.new_context(reduced_motion='reduce')
        page = context.new_page()

        # Load content from index.html (mocking file loading)
        with open('index.html', 'r') as f:
            content = f.read()

        # Strip redirect logic to prevent navigation
        content = content.replace('<script>window.location.replace("https://dhruvhaldar.vercel.app/");</script>', '')
        content = content.replace('<meta content="0; URL=https://dhruvhaldar.vercel.app/" http-equiv="refresh"/>', '')

        page.set_content(content)

        # Check if the spinner has animation: none
        spinner = page.locator('.spinner')
        # Wait for the spinner to be attached
        spinner.wait_for(state="attached")

        animation = spinner.evaluate("el => getComputedStyle(el).animation")

        print(f"Animation value with reduced motion: {animation}")

        if animation == 'none' or animation == 'none 0s ease 0s 1 normal none running':
             print("SUCCESS: Animation is disabled.")
        else:
             print("FAILURE: Animation is NOT disabled.")

        browser.close()

if __name__ == "__main__":
    verify_reduced_motion()
