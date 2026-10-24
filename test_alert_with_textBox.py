from playwright.sync_api import Page, expect, Playwright
import pytest

def test_dialogWithTextBox(playwright: Playwright):
    message_to_pass="Tom Holand"
    browser=playwright.firefox.launch(headless=False)

    context=browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    page=context.new_page()

    page.goto("https://demo.automationtesting.in/Alerts.html#google_vignette")
    page.locator("//a[@href='#Textbox']").click()

    page.wait_for_timeout(5000)
    page.on("dialog", lambda dialog: dialog.accept(message_to_pass))
    page.locator("//button[@onclick='promptbox()']").click()
    page.wait_for_timeout(3000)

    dialog_message_after=page.locator("//p[@id='demo1']")
    expect(dialog_message_after).to_contain_text(message_to_pass)

    context.tracing.stop(path="traces/dialogWithTextBox.zip")

    context.close()
    browser.close()