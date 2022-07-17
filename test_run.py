from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.gainsight.com/
    page.goto("https://www.gainsight.com/")
    page.set_default_timeout(3000)
    # Click button >> nth=1
    page.locator("button").nth(1).click(timeout=2000)
    # Click text=Accelerate Growth By Making Customers Wildly Successful With Your Products Drive >> a
    page.locator("text=Accelerate Growth By Making Customers Wildly Successful With Your Products Drive >> a").click()
    page.wait_for_url("https://info.gainsight.com/demo.html")
    # Click [placeholder="First name"]
    page.locator("[placeholder=\"First name\"]").click()
    # Fill [placeholder="First name"]
    page.locator("[placeholder=\"First name\"]").fill("Basavaaraj")
    # Press Tab
    page.locator("[placeholder=\"First name\"]").press("Tab")
    # Fill [placeholder="Last Name"]
    page.locator("[placeholder=\"Last Name\"]").fill("S")
    # Click [placeholder="Work email address"]
    page.locator("[placeholder=\"Work email address\"]").click()
    # Fill [placeholder="Work email address"]
    page.locator("[placeholder=\"Work email address\"]").fill("sbasavaraj")
    # Click [placeholder="Company"]
    page.locator("[placeholder=\"Company\"]").click()
    # Fill [placeholder="Company"]
    page.locator("[placeholder=\"Company\"]").fill("gainsight")
    # Click button:has-text("Submit")
    page.locator("button:has-text(\"Submit\")").click()
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
