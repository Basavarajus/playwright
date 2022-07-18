from playwright.sync_api import Playwright, sync_playwright, expect

import asyncio
from playwright.async_api import async_playwright


with sync_playwright() as p:
   # browser =p.webkit.launch()
    browser = p.webkit.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://lms.simplilearn.com")
    page.screenshot(path="example.png")
    browser.close()
 