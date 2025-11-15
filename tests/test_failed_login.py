
import pytest
from selenium.webdriver.common.by import By
from utils import login

@pytest.mark.failed
def test_failed_login_locked_out(login_page):
    driver = login_page
    login(driver, "locked_out_user", "secret_sauce")
    driver.implicitly_wait(3)
    error_el = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    text = error_el.text
    assert ("locked out" in text.lower()) or ("banned" in text.lower())
