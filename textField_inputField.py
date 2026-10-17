from playwright.sync_api import Page,expect
import pytest

def test_simple_textfield(page:Page):
    # (//div[@class='col-6']//input[@name='firstName'])[1]
    page.goto("https://testkru.com/Elements/TextFields")
    page.wait_for_timeout(3000)
    text_field_without_Placeholder=page.locator("(//div[@class='col-6']//input[@name='firstName'])[1]")
    expect(text_field_without_Placeholder).to_be_visible()
    text_field_without_Placeholder.fill("TestKru")

def test_textfield_with_placeholder(page:Page):
    page.goto("https://testkru.com/Elements/TextFields")
    # lastNameWithPlaceholder  
    page.wait_for_timeout(3000)
    text_field_with_Placeholder=page.locator("")