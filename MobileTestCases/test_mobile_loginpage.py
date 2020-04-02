from MobilePageObjects.Mobile_Login import MobileLogin
from MobilePageObjects.Mobile_HomePage import MobileHomePage
from MobilePageObjects.Mobile_HamburgerMenu import MobileHamburgeMenu
import pytest
import Utilities.CustomLogger as cl
import Static.Constants as const
import logging
from Utilities.Mobile_Webdriver import GetWebdriver
from appium.webdriver.common.mobileby import MobileBy
import softest
import time

log = cl.customLogger(logging.INFO)

val=''

@pytest.mark.usefixtures('create_resource')
class TestMobileLoginPage(softest.TestCase):
    '''
    Test Class for LoginPage
    '''

    @pytest.fixture(scope='function')
    def create_resource(self, request, browser,bstk_server):
        global val
        teardown_flag = False
        driver = GetWebdriver.get_webdriver(browser)
        home_obj = MobileHomePage(driver)
        login_obj=MobileLogin
        request.cls.home_obj = home_obj
        request.cls.login_obj = login_obj
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


    def test_create_account(self):

        time.sleep(6)
        log.info("Clicking on The Hamburger menu")
        hamburger_obj = self.home_obj.click_hamburger_menu()
        log.info("Clicking the Order option from menu")
        login_object = hamburger_obj.click_login()
        login_object.enter_customer_email(const.customer_email)