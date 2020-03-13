from Utilities.PageBase import PageBase
import MobileLocators.MobileOrderPageLocators as loc
import Static.Constants as const
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
            return True
        except Exception as e:
            raise Exception("Unable to check if Delivery button is present")

    def select_date_from_datepicker(self):
        '''
        
        '''

    def enter_address(self):
        '''
        Method to enter the address
        '''
        try:
            log.info("Enter the address 140 North 16th St, phila pa")
            self.send_keys(loc.address,const.order_address)
            log.info("Clicking on Delivery button")
            self.click(loc.delivery_btn)
            log.info("Clicking on Continue button")
            self.click(loc.confirm_address_continue_btn)
