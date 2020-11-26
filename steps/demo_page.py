from behave import *
from selenium import webdriver


@given(u'I am on the PHP Home page')
def navigate_to_home_page(context):
    context.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
    context.driver.get("https://phptravels.com/")


@when(u'I click the Demo tab on the menu')
def click_demo_tab(context):
    context.driver.find_element_by_xpath('/html/body/header/div/nav/a[1]').click()


@then(u'I should see the Demo page')
def step_impl(context):
    demo_page = context.driver.title
    if demo_page == "Demo Script Test drive - PHPTRAVELS":
        assert True
    else:
        assert False
