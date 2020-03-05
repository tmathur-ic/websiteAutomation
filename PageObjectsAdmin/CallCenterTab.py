from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
from Static import Constants as const
import Locators.CallCenterLocator as loc

log = cl.customLogger(logging.INFO)


class CallCenterTab(PageBase):
    '''
    Class for methods of Call Center Page
    '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def click_store_menu(self):
        '''
        Method to click on Store menu button
        '''
        try:
            self.click(self.wait_till_element_is_present(loc.store_menu_btn))
            return True
        except Exception as e:
            raise Exception("Unable to click on Store menu due to "+str(e))

    def select_store_from_menu(self):
        '''
        Method to select store from menu
        '''
        try:
            self.select_value_from_dropdown(loc.select_store,const.store_name)
            return True
        except Exception as e:
            raise Exception("Unable to select store from menu")

    def click_load_menu(self):
        '''
        Method to Click on Load Menu button
        '''
        try:
            self.click(self.wait_till_element_is_present(loc.load_menu_btn))
        except Exception as e:
            raise Exception ("Unable to click on load menu button")

    def get_store_title(self):
        '''
        Method to get the store title
        '''
        try:
            return self.get_text(loc.store_title)
        except Exception as e:
            raise Exception("Unable to get the store title due to "+str(e))
