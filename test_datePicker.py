from playwright.sync_api import Page, expect, Playwright
import pytest

def test_datePicker(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://www.globalsqa.com/demo-site/datepicker/#google_vignette")

    page.wait_for_timeout(3000)

    #clicking on the date picker input field
    top_frame=page.frame_locator("(//iframe[@class='demo-frame'])[1]")
    top_frame.locator("(//input[@id='datepicker'])[1]").nth(0).click()
    date_title=top_frame.locator("//div[@class='ui-datepicker-title']").text_content()
    print("Date title is: ",date_title)