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

from TestData.HomePageData import HomePageData
from pageObject.LoginPage import LoginPage
from pageObject.ProductPage import ProductPage
from tests.Baseclass import BaseClass


# @pytest.mark.usefixtures("init_driver")
# class BaseClass():
#     pass


class TestOne(BaseClass):

    def test_e2e1(self):
        log = self.getLogger()
        Login = LoginPage(self.driver)
        log.info("Login page Opened successsfull")
        Login.Login_Email_type("prajapatirajat94@gmail.com")
        log.info("Email entered successfull")

        # Email= self.driver.find_element(By.XPATH,"//input[@id='input-email']")
        # Email.send_keys("Prajapatirajat94@gmail.com")
        time.sleep(2)
        # Password = self.driver.find_element(By.XPATH, "//input[@id='input-password']")
        Login.Login_Password_type("Ksting@1234")
        log.info("password entered successfull")
        time.sleep(2)
        Login.LoginButton_Click()

        # Tablet=self.driver.find_element(By.XPATH,"//a[text()='Tablets']")
        # Tablet.click()
        time.sleep(2)
        # this return product page object
        productpage = Login.TabletButton_Click()

        tabname = productpage.TabletProduct_Text()
        time.sleep(2)
        assert tabname == "Samsung Galaxy Tab 10.1"

        time.sleep(2)

    def test_e2e2(self):
        productpage = ProductPage(self.driver)
        productpage.TabletProduct_Click()
        time.sleep(2)

        tabletprice = productpage.TabletPrice_Text()
        assert tabletprice == "$241.99"
        time.sleep(2)

    # below method, you need to add in TestClass to for parametrize and pass it into test_e2e.py file method
    # (self,getData)
    # here params support tupples and dictionary data type
    # below we have store data in HomePageData file from TestData
    #pass this getData in method example:-> def test_e2e(self,getData):
    # @pytest.fixture(params=HomePageData.getTestData("TC1"))
    # def getData(self, request):
    #     return request.param

    # or you can use in params dictionary
    # @pytest.fixture(params=[{"firstname":"Rajat@gmail.com", "password":"Rsting123" },
    #                         { "firstname":"kjl@gmail.com","password":"Rsting123"}])
    # def getData(request):
    #     return request.param
