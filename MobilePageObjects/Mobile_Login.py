from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
import MobileLocators.MobileLoginLocators as loc
from MobilePageObjects.Mobile_User import MobileUser
import Static.Constants as const
import time
log = cl.customLogger(logging.INFO)

class MobileLogin(PageBase):
    '''
    Class for methods of Login PAge of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_customer_email(self,email):
        '''
        Method to enter the customer email
        '''
        try:
            log.info("Entering the Customer Email id "+str(email))
            self.switch_control_to_app()
            self.driver.find_element_by_id('android:id/button2').click()
            time.sleep(3)
            self.switch_control_to_webview()
            self.send_keys(loc.current_user_email,email)
        except Exception as e:
            raise Exception ("Unable to enter the customer email due to "+str(e))

    def enter_customer_password(self,password):
        '''
        Method to enter the Customer's password
        '''
        try:
            log.info("Entering the Customer password "+str(password))
            self.send_keys(loc.current_password,password)
        except Exception as e:
            raise Exception("Unable to enter the customer password due to "+str(e))

    def click_remember_me_checkbox(self):
        '''
        Method to click the remember me checkbox
        '''
        try:
            log.info("Clicking the Remember me checkbox")
            self.click(loc.remember_me_chkbx)
        except Exception as e:
            raise  Exception ("Unable to click on remember me checkbox due to "+str(e))

    def click_login_btn(self):
        '''
        Method to click on Login Button
        '''
        try:
            log.info("Clicking on Login Button")

            self.wait_till_element_is_present(loc.login_btn)
            self.click(loc.login_btn)
            return MobileUser(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on login button due to "+str(e))

    def click_forgot_password(self):
        '''
        Method to click on Forgot password
        '''
        try:
            log.info("Clicking on Forgot your password")
            self.click(loc.forgot_pwd)
        except Exception as e:
            raise Exception ("Unable to click on Forgot Your Password link due to "+str(e))

    def enter_new_customer_email(self,email):
        '''
        Method to enter the new Customer email
        '''
        try:
            log.info("Entering the new Customer Email")
            self.send_keys(loc.register_email)
        except Exception as e:
            raise Exception("Unable to enter the new customer email id due to "+ str(e))

    def enter_new_customer_password(self,pwd):
        '''
        Method to enter the new Customer password
        '''
        try:
            log.info("Entering the new customer password")
            self.send_keys(loc.register_password,pwd)
        except Exception as e:
            raise Exception ("Unable to enter the register password due to "+str(e))

    def confirm_new_customer_password(self,pwd):
        '''
        Method to confirm password
        '''
        try:
            log.info("Confirming the password by entering password again")
            self.send_keys(loc.confirm_password,pwd)
        except Exception as e:
            raise Exception ("Unable to confirm the password due to "+str(e))

    def click_captcha(self):
        '''
        Method to click Captcha
        '''
        try:
            log.info("Clicking checkbox for captcha")
            self.click(loc.captcha_chkbx)
        except Exception as e:
            raise Exception("Unable to click checkbox for captcha due to "+str(e))

    def click_create_account_btn(self):
        '''
        Method to click on Create account button
        '''
        try:
            log.info("Clicking on Create Account button")
            self.click(loc.create_account_btn)
        except Exception as e:
            raise Exception("Unable to click on Create account button due to "+str(e))

    def click_no_loyalty_chkbx(self):
        '''
        Method to click on No loyalty checkbox
        '''
        try:
            log.info("Clicking on No loyalty checkbox")
            self.click(loc.no_loyalty_program)
        except Exception as e:
            raise Exception("Unable to click on no loyalty checkbox due to "+str(e))

    def click_subscribe_email(self):
        '''
        Method to subscribe email from insomnia
        '''
        try:
            log.info("Clicking checkbox to subscribe emails from insomnia")
            self.click(loc.like_emails)
        except Exception as e:
            raise Exception("Unable to click on subscribe email checkbox due to "+str(e))