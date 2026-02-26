from selenium import webdriver
from selenium.webdriver.common.by import By


class Homepage():
   lnk_reg_linktxt= "Register"
   lnk_login_linktxt= "Log in"
   lnk_logout_xpath="//a[@class='ico-logout']"

   def __init__(self,driver):
       self.driver=driver

   def register(self):
       self.driver.find_element(By.LINK_TEXT,self.lnk_reg_linktxt).click

   def click_loginpage(self):
       self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktxt).click()

   def click_logout(self):
       self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()

