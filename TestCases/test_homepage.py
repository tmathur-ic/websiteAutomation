from selenium import webdriver
import os,sys
import json
import requests
from PageObjects.HomePage import HomePage
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
class TestHomePage(softest.TestCase):
    '''
    Test Class for HomePage
    '''

    @pytest.fixture(scope='function')
    def create_resource(self, request, browser,bstk_server):
        global val
        teardown_flag = False
        driver = GetWebdriver.get_webdriver(browser)
        driver.maximize_window()
        home_obj = HomePage(driver)
        request.cls.home_obj = home_obj
        request.cls.server = bstk_server
        failed_before = request.session.testsfailed
        yield
        if request.session.testsfailed != failed_before:
            teardown_flag = True
            home_obj.teardown_browser()
        if not teardown_flag:
            home_obj.teardown_browser()

    def test_click_icon(self):
        '''
        Test if the user stays on HomePage after clicking the icon
        :return:
        '''
        global val
        page = "https://insomniacookies.com/"
        self.home_obj.open(page)
        log.info("Clicking on home page icon")
        self.soft_assert(self.assertEqual,self.home_obj.click_home_icon(),True,"Unable to click Tracker on  "+page)
        try:
            self.assert_all()
        except Exception as e:
            raise AssertionError(self.val)

    def test_click_cookies_on_menu(self):
        '''
        Test if the user is able to click on cookies on manu
        :return:
        '''
        page = "https://insomniacookies.com/"
        self.home_obj.open(page)
        log.info("Clicking on Menu icon")
        menu_obj=self.home_obj.click_menu()
        self.soft_assert(self.assertEqual,menu_obj.click_cookies_link(),True,"Unable to click Tracker on  "+page)
        try:
            self.assert_all()
        except Exception as e:
            raise AssertionError(self.val)

    def test_admin(self):
        '''
        Tests for admin
        :return:
        '''
        page = f"https://{self.server}.insomniacookies.com/admin/login?"
        self.home_obj.open(page)


