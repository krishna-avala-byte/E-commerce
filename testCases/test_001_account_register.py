import time
import os
from pageobjects.account_registration import registration
from pageobjects.Homepage import Homepage
from utilities import randomstring
from utilities.customLogger import LogGen
from utilities.readproperties import readconfig
import pytest

class Test_001_accountregister:
    # baseurl="https://demo.nopcommerce.com/register?returnUrl=%2F"
    baseurl = readconfig.Applicationbaseurl()
    logger = LogGen.loggen()

    def test_acc_setup(self,setup):
        self.driver=setup
        self.logger.info("***browser started***")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("*** Filling the account details ***")
        self.regpage=registration(self.driver)
        self.regpage.gender()
        self.regpage.firstname("kalyan")
        self.regpage.lastname("ka")
        self.Email = randomstring.random_string_generator()+"@gmail.com"
        # self.regpage.email(readconfig.get_email())
        self.regpage.email(self.Email)
        self.regpage.password(readconfig.get_password())
        self.regpage.cnf_password(readconfig.get_password())
        self.regpage.regbutton()
        self.message=self.regpage.cnfmmessage()
        time.sleep(5)
        self.logger.info("*** closing the browser***")
        self.driver.close()
        # if self.message=="Your registration completed":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_acc_setup.png")
        #     self.driver.close()
        #     assert False
