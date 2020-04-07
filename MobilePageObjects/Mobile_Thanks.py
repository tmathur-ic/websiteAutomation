from Utilities.PageBase import PageBase
import appium.webdriver.webelement
import MobileLocators.MobileThanksLocators as loc
from MobilePageObjects.Mobile_Tracker import MobileTracker
import Static.Constants as const
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)
from datetime import date
import time

class MobileThanks(PageBase):
    '''
    Class for methods of Thanks Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_thanks_present(self):
        '''
        Method to check if Thanks message is displayed
        '''
        try:
            log.info("Checking if Thanks message is displayed")
            self.wait_till_element_is_present(loc.thanks_message)
            if self.find_element(loc.thanks_message):
                return True
        except Exception as e:
            raise Exception ("Unable to check if thanks message is present due to "+str(e))

    def click_track_order_btn(self):
        '''
        Method to click the track order button
        '''
        try:
            log.info("Clicking the Track order button ")
            self.wait_till_element_is_present(loc.track_order_btn)
            self.click(loc.track_order_btn)
            return MobileTracker(self.driver)
        except Exception as e:
            raise Exception("Unable to click on Track order button due to "+str(e))

    def get_order_id(self):
        '''
        Method to get the order id
        '''
        try:
            log.info("Capturing the order id")
            order_id=self.get_attribute(loc.order_id_link,attribute='value')
            return order_id
        except Exception as e:
            raise Exception("Unable to get the order id due to "+str(e))