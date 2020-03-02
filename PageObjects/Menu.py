from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
import Locators.MenuPageLocators as loc

log = cl.customLogger(logging.INFO)

class MenuPage(PageBase):
    '''
    Class for methods of HomePage
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def click_cookies_link(self):
        '''
        Method to click on cookies
        :return:
        '''
        try:
            log.info("Clicking on Cookies link")
            self.click(loc.cookies_link)
            return True
        except Exception as e:
            raise Exception("Unable to click on cookies link")