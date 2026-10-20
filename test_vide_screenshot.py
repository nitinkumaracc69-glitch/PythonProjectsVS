from playwright.sync_api import Page, expect, Playwright
import pytest

def test_video_screen(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
   
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.wait_for_timeout(3000)
    page.screenshot(path="screenshot.png")