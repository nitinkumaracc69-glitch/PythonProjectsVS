from playwright.sync_api import Page, expect, Playwright
import pytest

def test_alert_handling_lambda(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Approach 2 to handle alert box
    page.goto("https://demo.automationtesting.in/Alerts.html#google_vignette")
    page.locator("//button[@onclick='alertbox()']").click()
    page.wait_for_timeout(5000)
    page.screenshot(path="dialogbox.png")
    print("dialog message:", page.on("dialog", lambda dialog: print(dialog.message)))
        
    page.on("dialog", lambda dialog: dialog.accept())