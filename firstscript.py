from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://quotes.toscrape.com/scroll')
        page.wait_for_timeout(5000)
        heading_selector = '//h1/a'
        heading = page.query_selector(heading_selector)
        print(heading.inner_text())
        login = page.query_selector('[href="/login"]')
        login.click()
        page.wait_for_timeout(5000)
        page.screenshot(path='img.png')
        print(page.title())
        browser.close()


if __name__ == '__main__':
    main()
