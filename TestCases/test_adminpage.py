from selenium import webdriver
import os,sys
import json
from PageObjectsAdmin.AdminHomePage import AdminHomePage
from PageObjectsAdmin.AdminLoginPage import AdminLoginPage
from Static import Constants as const
import unittest
from datetime import date
import pytest
import time
from datetime import date
import Utilities.CustomLogger as cl
import logging
from Utilities.WebDriver import GetWebdriver
# import allure
import softest

log = cl.customLogger(logging.INFO)

val=''

@pytest.mark.usefixtures('create_resource')
class TestAdminLoginPage(softest.TestCase):
    '''
    Test Class for AdminHome PAge
    '''

    @pytest.fixture(scope='function')
    def create_resource(self, request, browser,bstk_server):
        global val
        teardown_flag = False
        driver = GetWebdriver.get_webdriver(browser)
        driver.maximize_window()
        home_obj = AdminHomePage(driver)
        login_obj = AdminLoginPage(driver)
        request.cls.home_obj = home_obj
        request.cls.login_obj = login_obj

        request.cls.server = bstk_server
        request.cls.page = f"https://{bstk_server}.insomniacookies.com/admin/login?"
        self.home_obj.open(request.cls.page)
        failed_before = request.session.testsfailed
        yield
        if request.session.testsfailed != failed_before:
            teardown_flag = True
            home_obj.teardown_browser()
        if not teardown_flag:
            home_obj.teardown_browser()

    def test_check_store(self):
        '''
        Test if the user directs to call center page
        :return:
        '''
        log.info("Enter credentials")
        login_page_obj= self.home_obj.enter_credentials()
        log.info("Clicking on Call center tab")
        call_center_obj=login_page_obj.click_call_center()
        time.sleep(3)
        log.info("Clicking on Store Menu button")
        call_center_obj.click_store_menu()
        time.sleep(7)
        log.info("Select the store from list")
        call_center_obj.select_store_from_menu()
        log.info("Click the load menu button")
        call_center_obj.click_load_menu()
        time.sleep(7)
        log.info("Verifying the title")
        title = call_center_obj.get_store_title()
        print(title)
        flag=False
        if const.store_name in title:
            flag =True
        self.soft_assert(self.assertTrue(flag,"Store name not update"))
        try:
            self.assert_all()
        except Exception as e:
            raise AssertionError(self.val)
