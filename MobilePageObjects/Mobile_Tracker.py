from Utilities.PageBase import PageBase
import logging
import MobileLocators.MobileTrackerLocators as loc

import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)

class MobileTracker(PageBase):
    '''
    Class for methods of Tracker Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_track_order_btn(self):
        '''
        Method to click on Track order button
        '''
        try:
            log.info("Clicking the Track order button ")
            self.wait_till_element_is_present(loc.track_order_btn)
            self.click(loc.track_order_btn)
        except Exception as e:
            raise Exception("Unable to click on track order button")

    def enter_order_id(self,order_id):
        '''
        Mehtod to enter the order id
        '''
        try:
            log.info("Entering the order id")
            self.wait_till_element_is_present(loc.input_order_id)
            self.send_keys(loc.input_order_id,order_id)
        except Exception as e:
            raise Exception("Unable to enter the order id due to "+str(e))