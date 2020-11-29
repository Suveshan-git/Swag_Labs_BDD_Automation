from behave import *
from selenium import webdriver


@given(u'I launched the Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")


@when(u'I open the SwagLabs page')
def open_page(context):
    context.driver.get("https://www.saucedemo.com/")


@when(u'enter the "{username}" and "{password}"')
def enter_credentials(context, username, password):
    context.driver.find_element_by_xpath('//*[@id="user-name"]').send_keys(username)
    context.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)


@when(u'click the Login button')
def click_login(context):
    context.driver.find_element_by_xpath('//*[@id="login-button"]').click()


@then(u'I should land on the Products page')
def verify_product_page(context):
    page = context.driver.title
    if page == "Swag Labs":
        assert True
        context.driver.close()
    else:
        assert False
        context.driver.close()
