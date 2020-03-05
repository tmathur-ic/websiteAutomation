from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
from Static import Constants as const
import Locators.AdminLoginLocators as loc
from PageObjectsAdmin.CallCenterTab import  CallCenterTab

log = cl.customLogger(logging.INFO)

class AdminLoginPage(PageBase):
    '''
    Class for methods of AdminLogin Page
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_call_center(self):
        '''
        Method to click on Call center tab
        :return:
        '''
        try:
            log.info("Clicking on Call center tab")
            self.click(loc.call_center_tab)
            return CallCenterTab(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Call center tab")


