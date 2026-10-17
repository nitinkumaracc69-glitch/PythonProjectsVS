from playwright.sync_api import Page,expect
import pytest

def test_dynamic_table(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")
    table_rows=page.locator("//table[@class='table table-striped']//tbody//tr")
    cpu_load = ""
    for row in table_rows.all():
        process_name=row.locator("td").nth(0).inner_text()
        if process_name=="Chrome":
            cpu_load=row.locator("td:has-text('%')").inner_text()
            print(cpu_load)
            break
    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)

    page.wait_for_timeout(5000)