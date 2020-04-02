from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
import MobileLocators.MenuLocators as loc
from MobilePageObjects.Mobile_Locations import MobileLocation
from MobilePageObjects.Mobile_Login import MobileLogin
from MobilePageObjects.Mobile_Loyalty import MobileLoyalty
from MobilePageObjects.Mobile_Ship_cookies import MobileShipCookies
from MobilePageObjects.Mobile_About_us import MobileAboutUs
from MobilePageObjects.Mobile_Contact import MobileContact
from MobilePageObjects.Mobile_Cater import MobileCatering
from MobilePageObjects.Mobile_Events import MobileEvents
from MobilePageObjects.Mobile_Menu import MobileMenu
from MobilePageObjects.Mobile_Gifts import MobileGiftCard
from MobilePageObjects.Mobile_Order import MobileOrder
from MobilePageObjects.Mobile_Tracker import MobileTracker
from MobilePageObjects.Mobile_Gear import MobileGear
from MobilePageObjects.MobileCatalog import MobileCatalog

log = cl.customLogger(logging.INFO)

class MobileHamburgeMenu(PageBase):
    '''
    Class for methods of HomePage
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def click_order(self):
        '''
        Method to click order
        '''
        try:
            self.wait_till_element_is_present(loc.order_link)
            self.click(loc.order_link)
            return MobileOrder(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Order link due to " +str(e))

    def click_tracker(self):
        '''
        Method to lcick on Tracker
        '''
        try:
            self.click(loc.tracker_link)
            return MobileTracker(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Tracker link due to "+str(e))

    def click_ship_cookies(self):
        '''
        Method to click on Ship cookies
        '''
        try:
            self.click(loc.ship_cookies_link)
            return MobileCatalog(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Ship cookies due to "+str(e))

    def click_gift_cards(self):
        '''
        Method to click on Gift cards link
        '''
        try:
            self.click(loc.gift_card_link)
            return MobileGiftCard(self.driver)
        except Exception as e:
            raise Exception("Unable to click on Gift cards due to "+str(e))


    def click_gear(self):
        '''
        Method to click gear
        '''
        try:
            self.click(loc.gear_link)
            return MobileGear(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Gear link due to " +str(e))

    def click_menu(self):
        '''
        Method to click on menu
        '''
        try:
            self.click(loc.menu_link)
            return MobileMenu(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Menu link due to "+str(e))


    def click_catering(self):
        '''
        Method to click on catering
        '''
        try:
            self.click(loc.catering_link)
            return MobileCatering(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on catering due to "+str(e))


    def click_events(self):
        '''
        Method to click on events link
        '''
        try:
            self.click(loc.events_link)
            return MobileEvents(self.driver)
        except Exception as e:
            raise Exception("Unable to click on events due to "+str(e))

    def click_locations(self):
        '''
        Method to click locations
        '''
        try:
            self.click(loc.locations_link)
            return MobileLocation(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Locations due to " +str(e))

    def click_about_us(self):
        '''
        Method to click on about us
        '''
        try:
            self.click(loc.about_us_link)
            return MobileAboutUs(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on About Us link due to "+str(e))

    def click_loyalty(self):
        '''
        Method to click on loyalty
        '''
        try:
            self.click(loc.loyalty_link)
            return MobileLoyalty(self.driver)
        except Exception as e:
            raise Exception ("Unable to click on Loyalty due to "+str(e))

    def click_contact(self):
        '''
        Method to click on Contact link
        '''
        try:
            self.click(loc.contact_link)
            return MobileContact(self.driver)
        except Exception as e:
            raise Exception("Unable to click on Contact link due to "+str(e))

    def click_login(self):
        '''
        Method to click on login link
        '''
        try:
            self.click(loc.login_link)
            return MobileLogin(self.driver)
        except Exception as e:
            raise Exception("Unable to click on Login due to "+str(e))

