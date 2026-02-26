
import os
import pytest
from selenium import webdriver
from datetime import datetime

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver

# @pytest.fixture()
# def setup():
#     driver = webdriver.Edge()
#     yield driver
#     driver.quit()

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver= webdriver.Edge()
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        # driver = webdriver.Firefox(GeckoDriverManager().install())
        driver=webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver= webdriver.Chrome()
        print("Launching chrome browser.........")
    return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    if hasattr(config, '_metadata'):
      config._metadata['Project Name'] = 'nopCommerce'

      config._metadata['Module Name'] = 'AccountRegistration'
      config._metadata['Tester'] = 'Krishna'
      # config.option.htmlpath = "C:\\Users\\avalkris\\PycharmProjects\\nop_e_commerce_project\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
      config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"


# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
#Specifying report folder location and save report with timestamp
    # @pytest.hookimpl(tryfirst=True)
    # def pytest_configure(config):
    #     # config.option.htmlpath = "C:\\Users\\avalkris\\PycharmProjects\\nop_e_commerce_project\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
    #     config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"

    @pytest.hookimpl(tryfirst=True)
    def pytest_configure(config):
        # Define the reports directory inside the project
        report_dir = os.path.join(os.getcwd(), "report")
        os.makedirs(report_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Create a timestamped report filename
        report_filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
        report_path = os.path.join(report_dir, report_filename)

        # Set the htmlpath for pytest-html
        config.option.htmlpath = report_path
