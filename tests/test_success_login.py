
import pytest
from selenium.webdriver.common.by import By
from utils import login, is_element_present

@pytest.mark.success
def test_successful_login(login_page):
    driver = login_page
    login(driver, "standard_user", "secret_sauce")
    driver.implicitly_wait(3)
    assert is_element_present(driver, By.CLASS_NAME, "app_logo"), "App logo not found"
