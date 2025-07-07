from playwright.sync_api import sync_playwright

def log_page_activity():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # # Log console messages
        # page.on("console", lambda msg: print(f"Console: {msg.type()} - {msg.text()}"))
        # # Log network requests
        # page.on("request", lambda req: print(f"Request: {req.method()} {req.url}"))
        # # Log network responses
        # page.on("response", lambda res: print(f"Response: {res.status} {res.url}"))

        # Navigate to a page
        page.goto("https://staging.rocketrecall.io")
        page.wait_for_timeout(5000)  # Wait for the page to load completely

        # Perform login action
        page.click("text=Login")  # Use the correct button text as on the page

        # Wait for 5 seconds to observe activity
        page.wait_for_timeout(5000)

        browser.close()

log_page_activity()