from playwright.sync_api import Page, expect, Playwright
import pytest

def test_dialogbox_demo(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)

    context=browser.new_context()
    page=context.new_page()

    page.goto("https://demo.automationtesting.in/Alerts.html#google_vignette")
    page.locator("//button[@onclick='alertbox()']").click()
    


    #Approach 1 to handle alert box
    def handle_dialog(dialog):
        print(f"Dialog message: {dialog.message}")
        dialog.accept()
    page.on("dialog", handle_dialog)

    page.wait_for_timeout(5000)

