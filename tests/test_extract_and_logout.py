



import pytest
from selenium.webdriver.common.by import By
from utils import login
import os, json

@pytest.mark.extract
def test_extract_inventory_and_logout(login_page):
    driver = login_page
    login(driver, "standard_user", "secret_sauce")
    driver.implicitly_wait(3)

    assert "inventory" in driver.current_url or driver.find_elements(By.CLASS_NAME, "inventory_list")

    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    extracted = []
    for it in items:
        title = it.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = it.find_element(By.CLASS_NAME, "inventory_item_price").text
        desc = it.find_element(By.CLASS_NAME, "inventory_item_desc").text if it.find_elements(By.CLASS_NAME, "inventory_item_desc") else ""
        extracted.append({"title": title, "price": price, "desc": desc})

    out_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "inventory_extract.json"), "w") as f:
        json.dump(extracted, f, indent=2)

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.implicitly_wait(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    driver.implicitly_wait(2)
    assert driver.find_element(By.ID, "user-name")
