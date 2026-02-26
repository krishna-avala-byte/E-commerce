from selenium import webdriver
from selenium.webdriver.common.by import By

class registration:
   chk_gender_id="gender-male"
   txt_frstname_name="FirstName"
   txt_lastname_name="LastName"
   txt_email_xpath="//input[@id='Email']"
   txt_pwd_name="Password"
   txt_cnfpwd_name="ConfirmPassword"
   btn_register_id="register-button"
   txt_cnfrmsg_xpath="//div[@class='result']"

   def __init__(self,driver):
       self.driver=driver

   def gender(self):
       self.driver.find_element(By.ID,self.chk_gender_id).click()

   def firstname(self,firstname):
       self.driver.find_element(By.NAME,self.txt_frstname_name).send_keys(firstname)
   def lastname(self,lastname):
       self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lastname)
   def email(self,email):
       self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
   def password(self,password):
       self.driver.find_element(By.NAME,self.txt_pwd_name).send_keys(password)
   def cnf_password(self,cnfmpassword):
       self.driver.find_element(By.NAME,self.txt_cnfpwd_name).send_keys(cnfmpassword)
   def regbutton(self):
       self.driver.find_element(By.ID,self.btn_register_id).click()

   def cnfmmessage(self):
       try:
           self.driver.find_element(By.XPATH,self.txt_cnfrmsg_xpath).text
       except:
           None
