from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl

log = cl.customLogger(logging.INFO)

class MobileShipCookies(PageBase):
    '''
    Class for methods of Ship Cookies Page of mobile view
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
            return
        except Exception as e:
            raise Exception ("Unable to select the product due to "+str(e))

