from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.steps.Locators.locators import Locators

@given('I navigate to the WallTouchBD login page')
def step_navigate_to_login(context):
    chrome_driver_path = r"C:\Program Files\ChromeDriver\chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get("https://www.walltouchbd.com/")
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Locators.LOGIN_ICON))
    ).click()
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Locators.SIGN_IN_LINK))
    ).click()

@when("I enter valid credentials")
def step_enter_credentials(context):
    context.driver.find_element(By.XPATH, Locators.PHONE_NUMBER_INPUT).send_keys("01684300844")
    context.driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys("Jubear@#78")

@when("I click the login button")
def step_click_login(context):
    context.driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

@then('I should be logged in successfully')
def step_verify_login(context):
    welcome_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.WELCOME_MESSAGE))
    )
    assert welcome_message.is_displayed(), "Login not successful"

@when('I search for "toys"')
def step_search_toys(context):
    context.driver.find_element(By.XPATH, Locators.SEARCH_INPUT).send_keys("toys")
    context.driver.find_element(By.XPATH, Locators.SEARCH_BUTTON).click()

@then("I should see search results")
def step_verify_search_results(context):
    search_header = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.SEARCH_PAGE_HEADER))
    )
    assert search_header.is_displayed(), "Search not successful"

@when("I access the first item in the search results")
def step_access_first_item(context):
    first_item = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Locators.FIRST_ITEM))
    )
    first_item.click()

@then("I should be on the item's detail page")
def step_verify_item_detail_page(context):
    add_to_cart_button = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.ADD_TO_CART_BUTTON))
    )
    assert add_to_cart_button.is_displayed(), "Details page not found"
