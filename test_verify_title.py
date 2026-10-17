from playwright.sync_api import Page, expect


def test_verify_title(page: Page):
    # Launch and navigate to the target URL
    page.goto ("https://www.google.com")

    # Verify that the title exactly matches the expected text
    #expect(page).to_have_title("Google")
    my_title=page.title()
    expect(page).to_have_title("Google")
    print("The tile of the page is",my_title)
    page.close()

    