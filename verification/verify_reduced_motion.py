from playwright.sync_api import sync_playwright
import os

def verify_reduced_motion():
    os.makedirs("verification", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(reduced_motion='reduce')
        page = context.new_page()

        with open('index.html', 'r') as f:
            content = f.read()

        # Strip redirect to keep page stable
        content = content.replace('<script>window.location.replace("https://dhruvhaldar.vercel.app/");</script>', '')
        content = content.replace('<meta content="0; URL=https://dhruvhaldar.vercel.app/" http-equiv="refresh"/>', '')

        page.set_content(content)

        spinner = page.locator('.spinner')
        spinner.wait_for(state="attached")

        # specific check for animation-name
        anim_name = spinner.evaluate("el => getComputedStyle(el).animationName")
        print(f"Animation Name: {anim_name}")

        if anim_name == 'none':
             print("SUCCESS: Animation name is none.")
        else:
             print(f"FAILURE: Animation name is {anim_name}")

        page.screenshot(path="verification/reduced_motion.png")
        browser.close()

if __name__ == "__main__":
    verify_reduced_motion()
