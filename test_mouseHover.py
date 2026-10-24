from playwright.sync_api import Playwright, expect, Page
import pytest

def test_mouse_hover(playwright: Playwright):
    page=playwright.firefox.launch(headless=False).new_context().new_page()

    page.goto("https://practice-automation.com/hover/")
    mousehover_line=page.locator("//h3[@id='mouse_over']")

    mousehover_line.hover()
    page.wait_for_timeout(2000)

    text_after_mousehover=mousehover_line.text_content()
    print(text_after_mousehover)