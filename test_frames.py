from playwright.sync_api import Page, expect, Playwright
import pytest

def test_frames(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()

    page=context.new_page()

    page.goto("https://demo.automationtesting.in/Frames.html")


    # frame1=page.frame_locator("//iframe[@id='singleframe']")
    frame=page.frame(url='https://demo.automationtesting.in/SingleFrame.html')
    page.wait_for_timeout(2000)
    frame.locator("//input[@type='text']").fill("Hello frame")
    # frame1.locator("input[type='text']").fill("Hello frame")
    page.wait_for_timeout(2000)

    page.close()
    context.close()