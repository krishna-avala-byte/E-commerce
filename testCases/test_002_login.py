import time

import pytest
import os
from pageobjects.Homepage import Homepage
from pageobjects.Loginpage import Loginpage
from utilities.readproperties import readconfig
from utilities.customLogger import LogGen

class Test_login():
    baseurl= readconfig.Applicationbaseurl()
    logger=LogGen.loggen()

    username=readconfig.get_email()
    password=readconfig.get_password()

    def test_login(self,setup):
        self.logger.info("*** testcase_002---started------***")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        #accessing the homepage
        self.hp=Homepage(self.driver)
        self.hp.click_loginpage()

        self.lp=Loginpage(self.driver)
        self.lp.set_email(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login_button()
        self.target_page= self.lp.Is_cnfm_page()
        if self.target_page == True:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"loginpage.png")
            self.driver.close()
            assert False
        self.logger.info("*** testcase_002_login ended ***")

