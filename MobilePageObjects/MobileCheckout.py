from Utilities.PageBase import PageBase
import appium.webdriver.webelement
import MobileLocators.MobileCheckoutLocators as loc
import Static.Constants as const
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)
from datetime import date

class MobileCheckout(PageBase):
    '''
    Class for methods of Checkout Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_more_items(self):
        '''
        Method to click on Add More Items button
        '''
        try:
            log.info("Clicking on Add More Items button")
            self.wait_till_element_is_present(loc.add_more_items)
            self.click(loc.add_more_items)
        except Exception as e:
            raise Exception("Unable to click on Add More Items due to "+str(e))

    def click_add_to_order(self):
        '''
        Method to click on Add to Order button
        '''
        try:
            log.info("Clicking on Add to order button ")
            self.wait_till_element_is_present(loc.add_to_order)
            self.click(loc.add_to_order)
        except Exception as e:
            raise Exception("Unable to click on Add to order button due to "+str(e))

    def select_flavours(self,flavour):
        '''
        Method to Select ice cream flavours
        '''
        try:
            log.info("Clicking on Select Ice Cream flavours dropdown")
            self.wait_till_element_is_present(loc.select_flavours)
            log.info("Selecting the flavour "+ flavour + " from the options")
            self.select_dropdown_option(loc.select_flavours,flavour)
        except Exception as e:
            raise  Exception ("Unable to Select the flavour due to "+str(e))