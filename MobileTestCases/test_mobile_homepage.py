from MobilePageObjects.Mobile_HomePage import MobileHomePage
from MobilePageObjects.Mobile_HamburgerMenu import MobileHamburgeMenu
import pytest
import Utilities.CustomLogger as cl
import logging
from Utilities.Mobile_Webdriver import GetWebdriver
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

    def test_click_tracker(self):
        '''
        Test if the user is able to click on Tracker from Hamburger menu
        :return:
        '''
        log.info("Clicking on The Hamburger menu")
        hamburger_obj=self.home_obj.click_hamburger_menu()
        log.info("Clicking the Tracker option from menu")
        hamburger_obj.click_tracker()



