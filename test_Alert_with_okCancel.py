from playwright.sync_api import Page, expect, Playwright
import pytest

def test_alert_okCancel(playwright: Playwright):
    dialog_status="accept"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demo.automationtesting.in/Alerts.html#google_vignette")
    page.locator("//a[@href='#CancelTab']").click()
    page.wait_for_timeout(2000)
    
        
    
    page.wait_for_timeout(2000)
    if dialog_status=="accept":
            page.on("dialog", lambda dialog: dialog.accept())
            

    else:
            page.on("dialog", lambda dialog: dialog.dismiss())

    page.locator("//button[@onclick='confirmbox()']").click()
    dialog_message_after=page.locator("//p[@id='demo']").text_content()
    browser.close()
            