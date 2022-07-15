import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utilities.readProperties import ReadConfig

allure.dynamic.title("Tutorial Point Login_Page")

logging.basicConfig(filename='.\\Logs\\autoDemo.log', format='%(asctime)s %(message)s', level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S %p')

allure.step("Launch_Browser")


@given(u'Launch Browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.get(ReadConfig.getApplicationURL())
    context.driver.maximize_window()
    logging.info('**** Browser Launched ****')


@when(u'User Enter Valid Credentials')
def validCredentials(context):
    textbox_username = "user_email"
    textbox_password = "user_password"
    logging.info('**** Successfully Logged In ****')
    time.sleep(2)
    context.driver.find_element(by=By.ID, value=textbox_username).clear()
    time.sleep(2)
    context.driver.find_element(by=By.ID, value=textbox_username).send_keys(ReadConfig.getUsername())
    time.sleep(2)
    context.driver.find_element(by=By.ID, value=textbox_password).clear()
    time.sleep(2)
    context.driver.find_element(by=By.ID, value=textbox_password).send_keys(ReadConfig.getPassword())
    context.driver.save_screenshot(".\\Screenshots\\Login_Creds.png")


@then(u'User Click on Login Button')
def loginButton(context):
    button_login = "user_login"
    time.sleep(2)
    context.driver.find_element(by=By.ID, value=button_login).click()
    logging.info('**** User On Dashboard Page ****')
    time.sleep(5)
    context.driver.save_screenshot(".\\Screenshots\\Dashboard.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot1", attachment_type=AttachmentType.PNG)


@then(u'User Check Tutorial-point Logo')
def tutorialPointLogo(context):
    time.sleep(5)
    context.driver.find_element(by=By.XPATH,
                                value="//body/div[@id='']/div[@id='sidedrawer']/div[@id='sidedrawer-brand']/a[1]/span[1]/img[1]").screenshot(
        ".\\Screenshots\\Logo.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot2", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    context.driver.close()
