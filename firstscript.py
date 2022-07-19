from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://quotes.toscrape.com/scroll')
        page.wait_for_timeout(5000)
        heading_selector = '//h1/a'
        heading = page.query_selector(heading_selector)
        print(heading.inner_text())
        login = page.query_selector('[href="/login"]')
        login.click()

        user_input  = page.query_selector('[id="username"]')
        user_input.type("user")

        page.wait_for_timeout(3000)
        user_input_pass = page.query_selector('[id="password"]')
        user_input_pass.type("pass")

        page.query_selector('[type="submit"]').click()

        page.wait_for_timeout(5000)
        selector='//*[@href="/logout"]'
        try:
            logout = page.wait_for_selector(selector,timeout=5000)
        except:
            print('The login failed')
            exit()

        quotes = page.query_selector_all('[class="quote"]')
        for quote in quotes:
            print(quote.query_selector('.text').inner_text())


        page.screenshot(path='img.png')
        print(page.title())
        browser.close()


if __name__ == '__main__':
    main()
