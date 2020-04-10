from MobilePageObjects.Mobile_HomePage import MobileHomePage
from Utilities.PageBase import PageBase
from MobilePageObjects.Mobile_HamburgerMenu import MobileHamburgeMenu
import pytest
import Utilities.CustomLogger as cl
import Static.Constants as const
import logging
from Utilities.Mobile_Webdriver import GetWebdriver
from appium.webdriver.common.mobileby import MobileBy
import softest
import time
# import allure_pytest
import allure


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
            allure.attach(driver.get_screenshot_as_png())
            home_obj.teardown_browser()
        if not teardown_flag:
            home_obj.teardown_browser()

    @allure.story('Order Scenario')
    @allure.description("""
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
        16. Order confirmation page should appear displaying Order summary. """)
    # @allure.step('Clicking Hamburger and order option from menu')
    # def click_hamburger_and_order(self):
    #     log.info("Clicking on The Hamburger menu")
    #     hamburger_obj = self.home_obj.click_hamburlog.info("Clicking on The Hamburger menu")
    #     hamburger_obj=self.home_obj.click_hamburger_menu()
    #     log.info("Clicking the Order option from menu")
    #     order_obj = hamburger_obj.click_order()
    #     return order_obj
    #
    # @allure.step('Entering Address')
    # def enter_address(self):
    #     order_obj.enter_address()
    #

    def test_order_sixpack_(self):
        log.info("Clicking on The Hamburger menu")
        hamburger_obj=self.home_obj.click_hamburger_menu()
        log.info("Clicking the Order option from menu")
        allure.story("Clicking Order")
        order_obj = hamburger_obj.click_order()
        allure.step("Enter the Address to order")
        order_obj.enter_address()
        flag=order_obj.is_delivery_btn_present()
        time.sleep(3)
        #self.soft_assert(self.assertEqual(order_obj.is_pickup_btn_present(),True,"Pickup button not present"))
        self.soft_assert(self.assertEqual, flag, False, "Unable to click Tracker on  ")
        order_obj.click_delivery_btn()
        #self.softest(self.assertTrue(flag,"Delivery button not present"))
        order_obj.confirm_address_continue()
        order_obj.select_date_from_datepicker()
        order_obj.select_time_from_dropdown("1:30 PM")
        catalog_obj=order_obj.click_continue_redirect_catalog()
        catalog_obj.click_product(const.product_sixpack)
        catalog_obj.click_pick_for_me_btn()
        time.sleep(4)
        cart_obj=catalog_obj.click_add_to_cart_btn()
        checkout_obj=cart_obj.click_checkout_btn()
        #checkout_obj.click_add_to_order()
        checkout_obj.enter_recipient_name(const.receiver_name)

        checkout_obj.enter_recipient_phone_number(const.receiver_number)
        time.sleep(5)
        #checkout_obj.click_form(locator="xpath@@//h5[contains(text(),'Recipient Delivery')]")
        checkout_obj.scroll_down(locator="xpath@@//input[@id='recipient-name']")
        time.sleep(3)
        #checkout_obj.click_meet_me_outside()
        checkout_obj.scroll_down(locator="xpath@@//input[@id='no-contact-delivery-option3']")
        checkout_obj.click_same_as_above_chkbx()
        checkout_obj.enter_customer_name(const.customer_name)
        checkout_obj.enter_customer_phone_number(const.customer_number)
        time.sleep(3)
        checkout_obj.enter_customer_email_id(const.customer_email)
        checkout_obj.scroll_down(locator="xpath@@//input[@id='customer-email']")
        checkout_obj.click_credit_card()
        checkout_obj.enter_name_credit_card(const.credit_card_name)
        checkout_obj.enter_credit_card_number(const.credit_card_number)
        checkout_obj.enter_credit_card_expiry(const.expiry)
        checkout_obj.enter_credit_card_cvc(const.cvc)
        checkout_obj.scroll_down(locator="xpath@@//input[@id='cc-security-code']")
        thanks_obj=checkout_obj.click_place_order()
        time.sleep(6)
        is_thanks = thanks_obj.is_thanks_present()
        self.soft_assert(self.assertEqual,is_thanks,True,"Thanks message not received")


    @allure.description("""
    1. Go to the Website.
    2. Click on Order Tab.
    3. Enter Address 1130 Universiy Blvd, Tuscaloosa, AL 
    4. Click on Delivery button against a Store.
    5. Select Date and Time from Calendar.
    6. Click on Continue.
    7. On Menu Page, Click The Sugar Rush
    8. Click on Pick for me.  Cookies should be added to cart.
    9. Go to Cart.
    10. Click on Checkout.
    11. Enter Valid Details under Delivery Info & your Info.
    12. Enter Delivery Message
    13. Select locaton as On Campus and then select Dorm from dorm dropdown.
    14. Select Payment Method as Cash
    15. Click on Place Order.
    16. Order confirmation page should appear displaying Order summary.""")
    def test_second_order(self):
        log.info("Clicking on The Hamburger menu")
        hamburger_obj = self.home_obj.click_hamburger_menu()
        log.info("Clicking the Order option from menu")
        allure.story("Clicking Order")
        order_obj = hamburger_obj.click_order()
        allure.step("Enter the Address to order")
        order_obj.enter_address(const.address2)






