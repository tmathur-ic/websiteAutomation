from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)

class MobileOrder(PageBase):
    '''
    Class for methods of Order Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

