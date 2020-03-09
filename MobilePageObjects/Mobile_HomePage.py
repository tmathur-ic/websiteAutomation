from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
import MobileLocators.MobileHomePageLocators as loc
from MobilePageObjects.Mobile_HamburgerMenu import MobileHamburgeMenu
import Static.Constants as const
log = cl.customLogger(logging.INFO)

class HomePage(PageBase):
    '''
    Class for methods of HomePage of mobile view
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
            self.click(loc.home_img)
            return True
        except Exception as e:
            raise Exception("Unable to click on Home icon")

    def click_hamburger_menu(self):
        '''
        Method to click on Menu
        :return:
        '''
        try:
            log.info("Clicking on Menu Icon")
            self.click(loc.hamburger_menu_btn)
            return MobileHamburgeMenu(self.driver)
        except Exception as e:
            raise Exception("Unable to click on Menu")

    def click_top_order_now(self):
        '''
        Method to click on Top Order Now button
        '''
        try:
            log.info("Clicking on Top order Now button")
            self.click(loc.top_order_btn)
        except Exception as e:
            raise Exception("Unable to click on Top order now button")

    def enter_address(self):
        '''
        Method to enter the address
        '''
        try:
            log.info("Entering the address for order")
            self.send_keys(loc.address_order,const.address)
            log.log("Selecting from Dropdown")
            self.click(loc.address_select)
        except Exception as e:
            raise Exception("Unable to enter the address")

    def click_middle_order_now(self):
        '''
        Method to click on middle Order Now button
        '''
        try:
            log.info("Clicking on Top order Now button")
            self.click(loc.order_now_middle)
        except Exception as e:
            raise Exception("Unable to click on Middle order now button")