from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('the user is on the Google homepage')
def step_open_google(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com")
    time.sleep(5000)

@when('the user searches for "{term}"')
def step_search(context, term):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5000)

@then('the results page should show results')
def step_verify_results(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0
    context.driver.quit()
    

