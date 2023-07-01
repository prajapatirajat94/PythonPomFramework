from selenium.webdriver.common.by import By


class ProductPage():

    TabletText=(By.XPATH,"//a[text()='Samsung Galaxy Tab 10.1']")
    TabletPrice=(By.XPATH,"//div[@id='content']//div[@class='col-sm-4']//li/h2")

    def __init__(self,driver):
        self.driver=driver

    def TabletProduct_Text(self):
        return self.driver.find_element(*ProductPage.TabletText).text

    def TabletProduct_Click(self):
        return self.driver.find_element(*ProductPage.TabletText).click()

    def TabletPrice_Text(self):

        return self.driver.find_element(*ProductPage.TabletPrice).text
