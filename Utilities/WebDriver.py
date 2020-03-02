from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

class GetWebdriver():

    @staticmethod
    def get_webdriver(browser):
        if browser.lower() == 'firefox':
            return webdriver.Firefox(os.path.join(os.path.abspath(__file__ + "/../../"), "Webdrivers\\geckodriver.exe"))
        elif browser.lower() == 'chrome':
            chromeOptions = webdriver.ChromeOptions()
            prefs = {'safebrowsing.enabled': 'false'}
            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
            chromeOptions.add_experimental_option("prefs", prefs)
            return webdriver.Chrome(os.path.join(os.path.abspath(__file__ + "/../../"), "Webdrivers\\chromedriver.exe"), chrome_options=chromeOptions, desired_capabilities = desired_capabilities)