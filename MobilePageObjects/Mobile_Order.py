from Utilities.PageBase import PageBase
import appium.webdriver.webelement
import MobileLocators.MobileOrderPageLocators as loc
from MobilePageObjects.MobileCatalog import MobileCatalog
import Static.Constants as const
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)
from datetime import date
import time

class MobileOrder(PageBase):
    '''
    Class for methods of Order Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def is_pickup_btn_present(self):
        '''
        Method to check if the pickup button is present
        '''
        try:
            log.info("Checking if the pickup button is present")
            self.wait_till_element_is_present(loc.pickup_btn)
            return True
        except Exception as e:
            raise Exception("Unable to check if pickup button is present")

    def is_delivery_btn_present(self):
        '''
        Method to check if the deliver button is present
        '''
        try:
            log.info("Checking if the pickup button is present")
            self.wait_till_element_is_present(loc.delivery_btn)
            self.find_element(loc.delivery_btn)
            return True
        except Exception as e:
            raise Exception("Unable to check if Delivery button is present")

    def select_date_from_datepicker(self):
        '''
        Method to select date from datepicker
        '''

        try:
            log.info("clicking the datepicker widget")
            time.sleep(4)
            self.click(loc.date_selector)
            time.sleep(3)
            #self.click(loc.date_picker_selector)
            today = date.today().strftime("%d")
            if int(today) < 10:
                today = today.strip('0')
            elem=self.find_element(f"xpath@@//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='{today}']")
            elem.click()
            #self.click(loc.after_12_date)
            # if int(today) >= 12:
            #     self.click(loc.after_12_date)
            # else:
            #     self.click(loc.before_12_date)
        except Exception as e:
            raise Exception("Unable to select the date from datepicker")



    def select_time_from_dropdown(self, value):
        '''
        Method to select time from dropdown
        '''
        try:
            log.info("Selecting the time from dropdown")
            self.select_dropdown_option(loc.time_selector_dropdown, value)
        except Exception as e:
            raise Exception("Unable to select time from dropdown due to " + str(e))

    def enter_address(self):
        '''
        Method to enter the address
        '''
        try:
            time.sleep(20)
            self.switch_control_to_app()
            self.driver.find_element_by_id('android:id/button2').click()
            time.sleep(20)
            self.switch_control_to_webview()
            log.info("Enter the address 140 North 16th St, phila pa")
            time.sleep(5)
            self.find_element(loc.address)
            self.send_keys(loc.address,const.order_address)
            time.sleep(3)
            self.press_down_key(loc.address)
            #self.click(loc.address)
        except Exception as e:
            raise Exception ("Unable to enter the address due to " +str(e))
    #
    # def select_address(self):
    #     '''
    #     Method to select address from suggestion bar
    #     '''
    #     try:
    #         time.sleep(1)
    #         self.enter_address()
    #
    #     except Exception as e:
    #         raise Exception ("Unable to select address due to "+str(e))


    def click_delivery_btn(self):
        '''
        Method to click on delivery button
        '''
        try:
            log.info("Clicking on Delivery button")
            self.wait_till_element_is_present(loc.delivery_btn)
            self.click(loc.delivery_btn)
        except Exception as e:
            raise Exception("Unable to click on Delivery button due to "+str(e))

    def click_pickup_btn(self):
        '''
        Method to click on pickup button
        '''
        try:
            log.info("Clicking on Delivery button")
            self.click(loc.pickup_btn)
        except Exception as e:
            raise Exception("Unable to click on Pickup button due to "+str(e))

    def click_continue_redirect_catalog(self):
        '''
        Method to click on Continue button to redirect to catalog
        '''
        try:
            log.info("Clicking on Continue button")
            self.wait_till_element_is_present(loc.continue_to_catalog)
            self.click(loc.continue_to_catalog)
            log.info("Redirecting to Catalog page")
            return MobileCatalog(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on continue button due to "+str(e))

    def confirm_address_continue(self):
        '''
        Mehtod to click on Continue button for confirming address
        '''
        try:
            log.info("Clicking on Continue button")
            self.wait_till_element_is_present(loc.confirm_address_continue_btn)
            self.click(loc.confirm_address_continue_btn)
        except Exception as e:
            raise Exception ("Unable to click on continue button after confirming address due to "+str(e))
