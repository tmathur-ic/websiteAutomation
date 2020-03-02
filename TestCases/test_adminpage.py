from selenium import webdriver
import os,sys
import json
import requests
from PageObjectsAdmin.AdminHomePage import AdminHomePage
from PageObjectsAdmin.AdminLoginPage import AdminLoginPage
import unittest
from datetime import date
import pytest
import time
from datetime import date
import Utilities.CustomLogger as cl
import logging
from Utilities.WebDriver import GetWebdriver
import allure
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
        page = f"https://{self.server}.insomniacookies.com/admin/login?"
        self.home_obj.open(page)
        log.info("Enter credentials")
        login_page_obj= self.home_obj.enter_credentials()

        self.soft_assert(self.assertEqual,login_page_obj.click_call_center(),True,"Unable to check store"+page)
        try:
            self.assert_all()
        except Exception as e:
            raise AssertionError(self.val)
