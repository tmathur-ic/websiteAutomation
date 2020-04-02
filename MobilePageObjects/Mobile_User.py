from Utilities.PageBase import PageBase
import appium.webdriver.webelement
import MobileLocators.MobileOrderPageLocators as loc
from MobilePageObjects.MobileCatalog import MobileCatalog
import Static.Constants as const
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)
from datetime import date
import time

class MobileUser(PageBase):
    '''
    Class for methods of User Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
