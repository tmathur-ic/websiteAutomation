from Utilities.PageBase import PageBase
import appium.webdriver.webelement
import MobileLocators.MobileCatalogPageLocators as loc
from MobilePageObjects.MobileCart import MobileCart
import Static.Constants as const
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)
from datetime import date

class MobileCatalog(PageBase):
    '''
    Class for methods of Catalog Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_product(self,product):
        '''
        Method to click on the product on catalog page
        '''
        try:
            log.info("clicking on the product " + product)
            self.click(locator=f"xpath@@//div[@data-title='{product}']")
        except Exception as e:
            raise Exception ("Unable to select the product due to "+str(e))


    def click_pick_for_me_btn(self):
        '''
        Method to click on Pick for me button
        '''
        try:
            self.wait_till_element_is_present(loc.pick_for_me_btn)
            log.info("clicking on Pick for me button")
            self.click(loc.pick_for_me_btn)
        except Exception as e:
            raise Exception("Unable to click on Pick for me button due to "+ str(e))

    def click_add_to_cart_btn(self):
        '''
        Method to click on Add to cart button
        '''
        try:
            self.wait_till_element_is_present(loc.add_to_cart_btn)
            log.info("Clicking on Add to cart button")
            self.click(loc.add_to_cart_btn)
            return MobileCart(self.driver)
        except Exception as e:
            raise Exception("Unable to click on Add to cart button due to "+ str(e))

    def select_quantity_from_dropdown(self,quantity):
        '''
        Method to select quantity from dropdown
        '''
        try:
            log.info("Clicking on Dropdown to select quantity")
            self.click(loc.quantity_dropdown)
            log.info("Selecting the quantity " +str(quantity))
            self.click(locator=f"xpath@@//div[@class='modal-footer d-lg-none']//ul/li[@data-quantity='{quantity}']")
        except Exception as e:
            raise Exception("Unable to select quantity due to "+str(e))