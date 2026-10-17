from playwright.sync_api import Page, expect

def test_locators(page: Page):
    page.goto("https://saucelabs.com/")
    # get_by_text method is used to locate elements by their text content. 
    # It is a powerful way to find elements that contain specific text, making it easier to interact with them in tests.
    page.wait_for_timeout(5000)
    text_on_homepage=page.get_by_text("Verify AI-generated code at the pace it's written.")
    expect(text_on_homepage).to_be_visible()

    #page.getByAltText()
   
    alt_text=page.get_by_alt_text("Brand Logo").first
    print(alt_text)
    expect(alt_text).to_be_visible()

    #get_by_role method is used to locate elements based on their ARIA roles.
    expect(page.get_by_role('button', name='Products')).to_be_visible()

def test_verify_titile(page: Page):
    page.goto("https://saucelabs.com/")
    #get_by_title method is used to locate elements based on their title attribute.

    expect(page).to_have_title(
        "Sauce Labs: AI-Unified Release Assurance Platform"
    )

def test_placeholder(page:Page):
    page.goto("https://miketaylr.com/code/placeholder.html")
    page.wait_for_timeout(5000)
    #get_by_placeholder method is used to locate input elements based on their placeholder text.
    expect(page.get_by_placeholder("username@thissite.com")).to_be_visible()

def test_label(page:Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.wait_for_timeout(5000)
    #get_by_placeholder method is used to locate input elements based on their placeholder text.
    expect(page.get_by_label("Username")).to_be_visible()
    page.get_by_label("Username").fill("NITIN")