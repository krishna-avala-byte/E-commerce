import configparser
import os

config= configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")

class readconfig:
    @staticmethod
    def Applicationbaseurl():
        url=config.get('commonInformation','baseurl')
        return url

    @staticmethod
    def get_email():
        email=config.get('commonInformation','email')
        return email

    @staticmethod
    def get_password():
        password=config.get('commonInformation','password')
        return password
