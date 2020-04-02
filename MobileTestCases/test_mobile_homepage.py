from MobilePageObjects.Mobile_HomePage import MobileHomePage
from MobilePageObjects.Mobile_HamburgerMenu import MobileHamburgeMenu
import pytest
import Utilities.CustomLogger as cl
import Static.Constants as const
import logging
from Utilities.Mobile_Webdriver import GetWebdriver
from appium.webdriver.common.mobileby import MobileBy
import softest

log = cl.customLogger(logging.INFO)

val=''

@pytest.mark.usefixtures('create_resource')
class TestMobileHomePage(softest.TestCase):
    '''
    Test Class for HomePage
    '''

    @pytest.fixture(scope='function')
    def create_resource(self, request, browser,bstk_server):
        global val
        teardown_flag = False
        driver = GetWebdriver.get_webdriver(browser)
        home_obj = MobileHomePage(driver)
        request.cls.home_obj = home_obj
        request.cls.server = bstk_server
        page = f"https://{request.cls.server}.insomniacookies.com/"
        driver.get(page)
        failed_before = request.session.testsfailed
        yield
        if request.session.testsfailed != failed_before:
            teardown_flag = True
            home_obj.teardown_browser()
        if not teardown_flag:
            home_obj.teardown_browser()

    def test_order_guest(self):
        '''
        Test Scenario
        1. Go to the Website.
        2. Click on Order Tab.
        3. Enter 140 16th St, phila pa
        4. Verify that Pickup and Delivery buttons can be seen with out scrolling.  Make screen smaller to see if it adjusts.
        5. Click on Delivery button against a Store verify that the continue button can be see without scrolling
        6. Select Date and Time from Calendar.
        7. Click on Continue.
        8. On Menu Page, Click on a Six Pack and order 5
        9. Click on add product. Cookies should be added to cart Message should be show that items were added to cart.Only be present 1 second.
        10. Go to Cart.
        11. Click on Checkout.
        12. Enter Valid Details under Delivery Info & your Info.
        13. Enter Delivery Message
        14. Select Payment Method as Credit Card and enter its details.
        15. Click on Place Order.
        16. Order confirmation page should appear displaying Order summary.+
        :return:
        '''
        log.info("Clicking on The Hamburger menu")
        hamburger_obj=self.home_obj.click_hamburger_menu()
        log.info("Clicking the Order option from menu")
        order_obj = hamburger_obj.click_order()
        order_obj.enter_address()



