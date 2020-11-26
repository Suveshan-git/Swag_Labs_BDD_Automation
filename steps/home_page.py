from behave import *
from selenium import webdriver


@given(u'I have my browser open')
def open_browser(context):
    context.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")


@when(u'I enter the PHP URL and press enter')
def open_php(context):
    context.driver.get("https://phptravels.com/")


@then(u'I should land on the PHP Home Page')
def verify_home_page(context):
    title = context.driver.title
    if title == "PHPTRAVELS booking script and system for hotels airline flights tours cars online application - PHPTRAVELS":
        assert True
    else:
        assert False


@then(u'on the menu, I should see the Demo tab')
def verify_demo_tab(context):
    demo_tab = context.driver.find_element_by_xpath('/html/body/header/div/nav/a[1]').is_displayed()
    assert demo_tab is True


@then(u'I should see the Pricing tab')
def verify_pricing_tab(context):
    pricing_tab = context.driver.find_element_by_xpath('/html/body/header/div/nav/a[2]').is_displayed()
    assert pricing_tab is True


@then(u'I should see the Features tab')
def verify_features_tab(context):
    features_tab = context.driver.find_element_by_xpath('/html/body/header/div/nav/div[1]').is_displayed()
    assert features_tab is True


@then(u'I should see the Product tab')
def verify_product_tab(context):
    product_tab = context.driver.find_element_by_xpath('/html/body/header/div/nav/div[2]').is_displayed()
    assert product_tab is True


@then(u'I should see the Integrations tab')
def verify_integrations_tab(context):
    integrations_tab = context.driver.find_element_by_xpath('/html/body/header/div/nav/a[3]').is_displayed()
    assert integrations_tab is True


@then(u'I should see the Docs tab')
def verify_docs_tab(context):
    docs_tab = context.driver.find_element_by_xpath('/html/body/header/div/nav/a[4]').is_displayed()
    assert docs_tab is True


@then(u'I should see the Blog tab')
def verify_blog_tab(context):
    blog_tab = context.driver.find_element_by_xpath('/html/body/header/div/nav/a[5]').is_displayed()
    assert blog_tab is True


@then(u'I should see the Company tab')
def verify_company_tab(context):
    company_tab = context.driver.find_element_by_xpath('/html/body/header/div/nav/div[3]').is_displayed()
    assert company_tab is True


@then(u'I should see the Login button')
def verify_login_button(context):
    login_button = context.driver.find_element_by_xpath('/html/body/header/div/nav/a[6]').is_displayed()
    assert login_button is True
