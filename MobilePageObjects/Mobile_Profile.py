from Utilities.PageBase import PageBase
import appium.webdriver.webelement
import MobileLocators.MobileProfileLocators as loc
from MobilePageObjects.MobileCatalog import MobileCatalog
import Static.Constants as const
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)
from datetime import date
import time

class MobileProfile(PageBase):
    '''
    Class for methods of Profile Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_first_name(self,first_name):
        '''
        Method to enter the first name
        '''
        try:
            log.info("Entering the first name")
            self.send_keys(loc.input_first_name,first_name)
        except Exception as e:
            raise Exception("Unable to enter the first name due to "+str(e))

    def enter_last_name(self,last_name):
        '''
        Method to enter the last name
        '''
        try:
            log.info("Entering the last name")
            self.send_keys(loc.input_last_name,last_name)
        except Exception as e:
            raise Exception("Unable to enter the last name due to "+str(e))

    def enter_email_address(self,email):
        '''
        Method to enter the email address
        '''
        try:
            log.info("Entering the email address")
            self.send_keys(loc.input_email)
        except Exception as e:
            raise Exception ("Unable to enter the email due to "+str(e))

    def enter_phone_number(self,phone_number):
        '''
        Method to enter the phone number
        '''
        try:
            log.info("Entering the phone number")
            self.send_keys(loc.input_phone_number,phone_number)
        except Exception as e:
            raise  Exception ("Unable to enter the phone number due to "+str(e))

    def click_remember_credit_cards(self):
        '''
        Method to click checkbox for remembering cred cards
        '''
        try:
            log.info("Clicking the checkbox to remember credit card details")
            self.wait_till_element_is_present(loc.credit_card_chkbx)
            self.click(loc.credit_card_chkbx)
        except Exception as e:
            raise Exception ("Unable to click the checkbox due to "+str(e))

    def click_allow_push_notifications(self):
        '''
        Method to click checkbox for allowing push notifications
        '''
        try:
            log.info("Clicking the checkbox to allow push notifications")
            self.wait_till_element_is_present(loc.allow_notification_chkbx)
            self.click(loc.allow_notification_chkbx)
        except Exception as e:
            raise Exception ("Unable to click the checkbox due to "+str(e))

    def click_large_groups_chkbx(self):
        '''
        Methof to click the large group checkbox
        '''
        try:
            log.info("Clicking the large group checkbox")
            self.wait_till_element_is_present(loc.large_groups_chkbx)
            self.click(loc.large_groups_chkbx)
        except Exception as e:
            raise Exception("Unable to click the checkbox due to "+str(e))

    def click_event_offering_chkbx(self):
        '''
        Method to click the event offering checkbox
        '''
        try:
            log.info("Clicking the event offering checkbox")
            self.wait_till_element_is_present(loc.event_groups_chkbx)
            self.click(loc.event_groups_chkbx)
        except Exception as e:
            raise Exception("Unable to click on checkbox due to "+str(e))

    def click_newsletter_chkbx(self):
        '''
        Method to click the newsletter checkbox
        '''
        try:
            log.info("Clicking the newsletter checkbox")
            self.wait_till_element_is_present(loc.newsletter_chkbx)
            self.click(loc.newsletter_chkbx)
        except Exception as e:
            raise Exception ("Unable to click on checkbox due to "+str(e))

    def click_update_profile_btn(self):
        '''
        Method to click on Update Profile button
        '''
        try:
            log.info("Clicking on Update Profile button")
            self.wait_till_element_is_present(loc.update_profile_btn)
            self.click(loc.update_profile_btn)
        except Exception as e:
            raise Exception ("Unable to click on Update Profile button due to "+str(e))

    def enter_current_password(self,current_pwd):
        '''
        Method to Enter the current password
        '''
        try:
            log.info("Entering the current password")
            self.wait_till_element_is_present(loc.input_current_pwd)
            self.send_keys(loc.input_current_pwd,current_pwd)
        except Exception as e:
            raise Exception ("Unable to enter the current password due to "+str(e))

    def enter_new_password(self,new_pwd):
        '''
        Method to enter the new password
        '''
        try:
            log.info("Enter the new password")
            self.wait_till_element_is_present(loc.input_new_pwd)
            self.click(loc.input_new_pwd,new_pwd)
        except Exception as e:
            raise Exception ("Unable to enter the new password due to "+str(e))