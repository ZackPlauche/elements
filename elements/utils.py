from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def remove_duplicates(items: list):
    return list(dict.fromkeys(items).keys())

def wait_for_element_text(
    driver: WebDriver,
    selector: tuple[str, str],
    expected_text: str,
    timeout: int = 10
) -> bool:
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(selector, expected_text)
    )