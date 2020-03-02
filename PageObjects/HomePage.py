from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
import Locators.HomePageLocators as loc
from PageObjects.Menu import MenuPage

log = cl.customLogger(logging.INFO)

class HomePage(PageBase):
    '''
    Class for methods of HomePage
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_home_icon(self):
        '''
        Method to click on home icon
        :return:
        '''
        try:
            log.info("Clicking on Home Icon")
            self.click(loc.home_image)
            return True
        except Exception as e:
            raise Exception("Unable to click on Home icon")

    def click_menu(self):
        '''
        Method to click on Menu
        :return:
        '''
        try:
            log.info("Clicking on Menu Icon")
            self.click(loc.menu)
            return MenuPage(self.driver)
        except Exception as e:
            raise Exception("Unable to click on Menu")

