
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

REPORTS_DIR = os.path.join(os.getcwd(), "reports")
SCREENSHOT_DIR = os.path.join(REPORTS_DIR, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture(scope="function")
def driver(request):
    chrome_options = Options()
    if os.environ.get("HEADLESS", "false").lower() in ("1", "true", "yes"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    yield driver

    try:
        driver.quit()
    except Exception:
        pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver_fixture = item.funcargs.get('driver') if 'driver' in item.funcargs else None
        if driver_fixture:
            timestamp = int(time.time() * 1000)
            name = item.name
            screenshot_file = os.path.join(SCREENSHOT_DIR, f"{name}_{timestamp}.png")
            try:
                driver_fixture.save_screenshot(screenshot_file)
            except Exception as e:
                print(f"Failed to save screenshot: {e}")

@pytest.fixture
def login_page(driver, base_url):
    driver.get(base_url)
    return driver
