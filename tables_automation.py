from playwright.sync_api import Page,expect
import pytest

def test_static_table(page: Page):
    page.goto("https://www.tutorialspoint.com/selenium/practice/webtables.php")
    table_data=page.locator("//table[@class='table table-striped mt-3']//tbody//tr")
    page.wait_for_timeout(5000)
    for data in table_data.all():
        print(data.locator("td").all_inner_texts())

# finding a specific text in the table and printing the row data
def test_specific_text_in_table(page: Page):
    page.goto("https://www.tutorialspoint.com/selenium/practice/webtables.php")
    table_data=page.locator("//table[@class='table table-striped mt-3']//tbody")
    page.wait_for_timeout(5000)
    print(table_data.locator("tr").nth(0).locator("td").nth(0).all_inner_texts())

# Column count verification
def test_column_count_verification(page: Page):
    page.goto("https://www.tutorialspoint.com/selenium/practice/webtables.php")
    table_column_counts=page.locator("//table[@class='table table-striped mt-3']//thead//th")
    actualcolumn_count=table_column_counts.count() 
    expect(table_column_counts).to_have_count(actualcolumn_count)

# Row count verification
def test_row_count_verification(page: Page):
    page.goto("https://www.tutorialspoint.com/selenium/practice/webtables.php")
    table_row_counts=page.locator("//table[@class='table table-striped mt-3']//tbody//tr")
    actualrow_count=table_row_counts.count()
    print(actualrow_count)
    expect(table_row_counts).to_have_count(actualrow_count)

# Table Header Names Validation
def test_table_header_names_validation(page: Page):
    page.goto("https://www.tutorialspoint.com/selenium/practice/webtables.php")
    header_elements=page.locator("//table[@class='table table-striped mt-3']//thead//tr//th")
    expected_headers = ["First Name" , "Last Name", "Age", "Email", "Salary", "Department", "Action"]
   
    for i, expected_header in enumerate(expected_headers):
        expect(header_elements.nth(i)).to_have_text(expected_header)

# Precise Cell Value Extraction
def test_precise_cell_value_extraction(page: Page):
    page.goto("https://www.tutorialspoint.com/selenium/practice/webtables.php")
    cell_value = page.locator("//table[@class='table table-striped mt-3']//tbody//tr[1]//td[3]")
    expect(cell_value).to_have_text("39")