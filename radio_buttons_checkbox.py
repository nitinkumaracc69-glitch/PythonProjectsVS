from playwright.sync_api import Page,expect
import pytest   

def test_1(page:Page):
    page.goto("https://testkru.com/Elements/RadioButtons")
    radiobuttons=page.locator("//input[@name='select']")
    print(radiobuttons.count())
    page.wait_for_timeout(3000)
    for radiobutton in radiobuttons.all():
        page.wait_for_timeout(2000)
        expect(radiobutton).to_be_visible()
        expect(radiobutton).to_be_enabled()
        radiobutton.click()

#Selecting multiple radio buttons in a group is not possible, 
# but we can select multiple radio buttons from different groups.
# (//div[@class='col-6'])[2]//input
# (//div[@class='col-6'])[2] -- this represents second group and //input -- this represents all radio 
# buttons in that group.
def test_2_multiselect_radiobuttons(page: Page):
        page.goto("https://testkru.com/Elements/RadioButtons")
        multiselect_radiobuttons=page.locator("(//div[@class='col-6'])[2]//input")
        print(multiselect_radiobuttons.count())
        page.wait_for_timeout(3000)
        for radiobutton in multiselect_radiobuttons.all():
             page.wait_for_timeout(2000)
             expect(radiobutton).to_be_visible()
             expect(radiobutton).to_be_enabled()
             radiobutton.click()

def test_3_disabled_radiobuttons(page: Page):
        page.goto("https://testkru.com/Elements/RadioButtons")
        multiselect_radiobuttons=page.locator("(//div[@class='col-6'])[3]//input[contains(@name,'disabled')]")
        print(multiselect_radiobuttons.count())
        page.wait_for_timeout(3000)
        for radiobutton in multiselect_radiobuttons.all():
            page.wait_for_timeout(2000)
            expect(radiobutton).to_be_disabled()
            