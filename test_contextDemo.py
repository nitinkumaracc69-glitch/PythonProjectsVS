from playwright.sync_api import Page, expect, Playwright
import pytest

def test_context_demo(playwright: Playwright):
    #creating the context and saving it in a variable
    browser=playwright.chromium.launch(headless=False)

    #creating a new page in the context
    page=browser.new_page()

    #navigating to a URL using above page variable
    page.goto("https://www.google.com")

    page.wait_for_timeout(3000)

    expect(page).to_have_title("Google")

