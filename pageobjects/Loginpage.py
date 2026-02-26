from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpage():
    txt_email_id="Email"
    txt_password_id="Password"
    btn_login_xpath="//button[normalize-space()='Log in']"
    txt_cnfm_page_xpath="//h2[normalize-space()='Welcome to our store']"

    def __init__(self,driver):
       self.driver=driver

    def set_email(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)

    def set_password(self,pwd):
        self.driver.find_element(By.ID,self.txt_password_id).send_keys(pwd)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()


    def Is_cnfm_page(self):
        try:
          return self.driver.find_element(By.XPATH,self.txt_cnfm_page_xpath).is_displayed()
        except:
            False




