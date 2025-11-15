
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def login(driver, username, password):
    user_el = driver.find_element(By.ID, "user-name")
    pass_el = driver.find_element(By.ID, "password")
    btn = driver.find_element(By.ID, "login-button")

    user_el.clear()
    user_el.send_keys(username)
    pass_el.clear()
    pass_el.send_keys(password)
    btn.click()

def is_element_present(driver, by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False
