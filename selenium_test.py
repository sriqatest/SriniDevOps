import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module", autouse=True)
def browser():
    # Set below options for AWS optimized headless browser
    chrome_options = Options()
    all_arguments = ["--headless", "window-size=1400,1500", "--disable-gpu",
                     "--no-sandbox", "start-maximized", "enable-automation",
                     "--disable-infobars", "--disable-dev-shm-usage"]
    for argument in all_arguments:
        chrome_options.add_argument(argument)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    # Return the driver object at the end of setup
    yield driver
    # For cleanup, quit the driver
    driver.close()
    driver.quit()
    print("Test Complete")


# Test step 1 - Open URL
def test_open_url(browser):
    browser.get("http://35.154.147.222/")


# Test step 2 - Check Title
def test_check_title(browser):
    assert "Simple PHP Website" in browser.title


# Test step 2 - Check Home Link Present
def test_home_link(browser):
    assert browser.find_element_by_id("Homes")


# Test step 3 - Check About Us Link Present
def test_about_link(browser):
    assert browser.find_element_by_id("About Uss")


# Test step 4 - Check Product Link Present
def test_product_link(browser):
    assert browser.find_element_by_id("Products")


# Test step 5 - Check Contact Link Present
def test_contact_link(browser):
    assert browser.find_element_by_id("Contacts")