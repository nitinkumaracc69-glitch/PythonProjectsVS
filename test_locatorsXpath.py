from playwright.sync_api import Page, expect

def test_relativeXptah(page: Page):
    page.goto("https://www.hyrtutorials.com/p/add-padding-to-containers.html#google_vignette")
    locator=page.locator("//a[contains(text(),'Sign in into account')]")
    print("Locator  is "+ str(locator))
    expect(locator).to_contain_text("Sign in into account")

def test_relativeXptah_contains(page: Page):
    page.goto("https://www.way2automation.com/practice.html")
    locators=page.locator("//article[@class='course-card practice-card']/a//span[contains(text(),'Web App')]")
    print(locators.count())
    expect(locators).to_have_count(locators.count())

    print(locators.first.text_content())
    print(locators.last.text_content())
    print(locators.nth(5).text_content())

def test_relativeXptah_startWith(page: Page):
    page.goto("https://www.way2automation.com/practice.html")
    locators=page.locator("//article[@class='course-card practice-card']/a//span[starts-with(text(),'Web App')]")
    print(locators.count())
    expect(locators).to_have_count(locators.count())

    print(locators.first.text_content())
    print(locators.last.text_content())
    print(locators.nth(5).text_content())

    product_locators=locators.all_text_contents()
    for product in product_locators:
        print(product)

def test_locators_names(page: Page):
    page.goto("https://www.way2automation.com/practice.html")
    locators=page.locator("//div[@id='webapp']//a[@class='practice-thumb']")
    for locator in locators.all():
        print(locator.text_content())

def test_findingLast_locator(page: Page):
    page.goto("https://www.way2automation.com/")
    locators=page.locator("//div[@class='footer-col'][1]//a[last()]")
    print(locators.text_content())
    expect(locators).to_contain_text("AI Testing")

def test_relativeXptah_contains1(page: Page):
    page.goto("https://demowebshop.tricentis.com/desktops")
    locators=page.locator("//h2//a[contains(@href,'computer')]")
    print(locators.count())
    print(locators.all_text_contents())
    expect(locators).to_have_count(locators.count())

# last() and position() functions
    google_plus=page.locator("//div[@class='column follow-us']//li[last()]")
    print(google_plus.text_content())
    expect(google_plus).to_contain_text("Google+")

    second_locator=page.locator("//div[@class='column follow-us']//li[position()=2]")
    print(second_locator.text_content())
    expect(second_locator).to_contain_text("Twitter")

    


