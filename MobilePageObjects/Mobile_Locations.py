from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
import MobileLocators.MobileHomePageLocators as loc
log = cl.customLogger(logging.INFO)

class MobileLocation(PageBase):
    '''
    Class for methods of Locations PAge of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

