from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
from Static import Constants as const
import Locators.AdminHomeLocators as loc
from PageObjectsAdmin.AdminLoginPage import AdminLoginPage

log = cl.customLogger(logging.INFO)

class AdminHomePage(PageBase):
    '''
    Class for methods of Admin Home Page
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login(self):
        '''
        Method to click on login button
        :return:
        '''
        try:
            log.info("Clicking on login button")
            self.click(loc.login_btn)
            return AdminLoginPage(driver=self.driver)
        except Exception as e:
            raise e

    def enter_credentials(self):
        '''
        Enter the Username
        :return:
        '''
        try:
            log.info("Entering the username")
            self.send_keys(loc.username,const.admin_user)
            log.info("Ëntering the password")
            self.send_keys(loc.password,const.admin_pass)
            login_obj =self.click_login()
            return login_obj
        except Exception as e:
            raise Exception("Unable to enter credentials")



