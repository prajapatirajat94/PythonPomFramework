import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pageObject.ProductPage import ProductPage


class LoginPage:

    email=(By.XPATH,"//input[@id='input-email']")
    password=(By.XPATH,"//input[@id='input-password']")
    LoginBtn=(By.XPATH,"//input[@type='submit']")
    TabletButton=(By.XPATH,"//a[text()='Tablets']")
    def __init__(self,driver):
        self.driver=driver

#here we have to call classlevel instance with Classname.variablename
    def Login_Email_type(self,Email):
        self.driver.find_element(*LoginPage.email).send_keys(Email)


    def Login_Password_type(self,TypePassword):
        self.driver.find_element(*LoginPage.password).send_keys(TypePassword)

    def LoginButton_Click(self):
        self.driver.find_element(*LoginPage.LoginBtn).click()


    def TabletButton_Click(self):
        self.driver.find_element(*LoginPage.TabletButton).click()
        productpage=ProductPage(self.driver)
        return productpage

