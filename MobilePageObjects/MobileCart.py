from Utilities.PageBase import PageBase
import appium.webdriver.webelement
import MobileLocators.MobileCartLocators as loc
from MobilePageObjects.MobileCheckout import MobileCheckout
import Static.Constants as const
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)
from datetime import date

class MobileCart(PageBase):
    '''
    Class for methods of Cart Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_apply_coupon(self):
        '''
        Method to Click on Apply Coupon
        '''
        try:
            log.info("Clicking on Apply coupon button")
            self.wait_till_element_is_present(loc.apply_btn)
            self.click(loc.apply_btn)
        except Exception as e:
            raise Exception ("Unable to click on Apply button due to "+str(e))

    def enter_coupon(self,coupon):
        '''
        Method to Enter the Coupon
        '''
        try:
            log.info("Entering the coupon "+str(coupon))
            self.send_keys(loc.input_apply_coupon,str(coupon))
        except Exception as e:
            raise Exception ("Unable to enter the coupon due to "+str(e))

    def click_delete_product(self):
        '''
        Method to click on Delete icon
        '''
        try:
            log.info("Clicking on Delete icon")
            self.wait_till_element_is_present(loc.delete_btn)
            self.click(loc.delete_btn)
        except Exception as e:
            raise  Exception ("Unable to click on Delete icon due to "+str(e))

    def click_edit_icon(self):
        '''
        Method to click on Edit icon
        '''
        try:
            log.info("Clicking on Edit icon")
            self.wait_till_element_is_present(loc.edit_icn)
            self.click(loc.edit_icn)
        except Exception as e:
            raise Exception ("Unable to click on Edit icon due to "+str(e))

    def click_checkout_btn(self):
        '''
        Clicking on Checkout button
        '''
        try:
            log.info("Clicking on Checkout Button")
            self.wait_till_element_is_present(loc.checkout_btn)
            self.click(loc.checkout_btn)
            return MobileCheckout(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Checkout button due to "+str(e))

    def click_edit_product(self):
        '''
        Clicking on edit product card
        '''
        try:
            log.info("Clicking on Edit product card")
            self.wait_till_element_is_present(loc.edit_product)
            self.click(loc.edit_product)
        except Exception as e:
            raise Exception ("Unable to click on edit product card "+str(e))


    def select_date_from_datepicker(self):
        '''
        Method to select date from datepicker
        '''
        try:
            log.info("clicking the datepicker widget")
            self.click(loc.date_picker_selector)
            today = date.today().strftime("%d")
            if int(today) >= 12:
                self.click(loc.after_12_date)
            else:
                self.click(loc.before_12_date)
        except Exception as e:
            raise Exception ("Unable to select the date from datepicker")


    def select_time_from_dropdown(self,value):
        '''
        Method to select time from dropdown
        '''
        try:
            log.info("Selecting the time from dropdown")
            self.select_dropdown_option(loc.time_selector_dropdown,value)
        except Exception as e:
            raise Exception ("Unable to select time from dropdown due to "+str(e))
