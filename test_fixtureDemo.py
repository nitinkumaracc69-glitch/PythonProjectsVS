from playwright.sync_api import Page, expect
import pytest

@pytest.fixture
def setup():
    print("Initializing test environemt.....")
    yield
    print("Test environment cleanup.....")

def test_1(setup):
    print("Test 1 is running.....")

def test_2(setup):
    print("Test 2 is running.....")