from urllib.parse import unquote
import json
from enum import Enum
import time
import Utilities.CustomLogger as cl
import logging
import os
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from retry import retry
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver

class PageBase():

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def open(self, url, wait_time=2):
        """
        Visit the page base_url + url
        :param url: URL to be opened
        :param wait_time: time to wait till url opens
        :return:
        """
        # url = self.base_url + url
        if self.driver.current_url != url:
            self.driver.get(url)
        self.sleep_in_seconds(wait_time)

    def get_page_source(self):
        """
        Return the page source of current page
        :return:
        """
        return self.driver.page_source

    def get_currentdriver(self):
        """
        Return current driver
        :return: current driver instance
        """
        return self.driver

    def get_current_title(self):
        """
        Get the current title of the opened browser
        :return: current browser title
        """
        return self.driver.title

    def get_current_url(self):
        """
        Get the current URL
        :return: Return current URL
        """
        return self.driver.current_url

    def is_element_selected(self, locator):
        """
        Check whether provided element is selected
        :param locator: Element locator strategy
        :return: True or False about the element selection
        """
        element = self.find_element(locator)
        return element.is_selected()

    def is_element_enabled(self, locator):
        """
        Returns whether given element is enabled or not
        :param locator: Element locator strategy
        :return: True if given element is enabled else returns false
        """
        element = self.find_element(locator)
        return element.is_enabled()

    @retry(StaleElementReferenceException, tries=5, delay=2)
    def click(self, locator):
        """
        Clicks the given element
        :param locator: Element locator strategy
        :return: element
        """
        element = None
        if isinstance(locator, str):
            element = self.find_element(locator)
        elif isinstance(locator, WebElement):
            element = locator

        if element is not None:
            element.click()
        else:
            raise Exception("Could not click on locator " + element)

    def javascript_click(self, locator):
        element = None
        if isinstance(locator, str):
            element = self.find_element(locator)
        elif isinstance(locator, WebElement):
            element = locator

        if element is not None:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            raise Exception("Could not click on locator " + element)

    def set_field(self, locator, element_value):
        """
        Locates the element by specified locator and then sets its value
        :param locator: Element locator strategy
        :param element_value: value to be written
        :return: element
        """
        webelement = self.find_element(locator)
        try:
            webelement.send_keys(Keys.CONTROL, 'a')
            webelement.clear()
            time.sleep(1)
            webelement.send_keys(element_value)
        except Exception as e:
            raise Exception("Could not write on the the element {} due to {}".
                            format(webelement, e))

        return webelement

    def get_text(self, locator):
        """
        get  the inner text of given element
        :param locator: Element locator strategy
        :return: text
        """
        element = self.find_element(locator)
        return element.text

    def get_element_text(self, element):
        """
        get  the inner text of given element
        :param locator: Element locator strategy
        :return: text
        """
        # element = self.find_element(locator)
        return element.text

    def is_element_displayed(self, locator):
        """
        Returns whether given element is displayed or no
        :param locator: Element locator strategy
        :return: True if given element is displayed else returns false
        """
        element = self.find_element(locator)
        return element.is_displayed()

    def switch_to_frame(self, frame_id):
        """
        Switch to the given frame based on id
        :param frame_id: id of the frame (can be xpath also)
        :return:
        """
        self.driver.switch_to_frame(frame_id)

    def switch_to_main_window(self):
        """
        Switch to the main browser window
        :return:
        """
        self.driver.switch_to_default_content()

    def move_and_click(self, locator):
        """
        Move and click to the given element using
        selenium action class
        :param locator: Element locator strategy
        :return: element
        """
        element = self.find_element(locator)
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()
        except Exception as e:
            raise Exception("Could Not click locator {} due to {}".format(element, e))
        return element

    def click_and_move_by_offset(self, locator, offset):
        element = self.find_element(locator)
        drawing = ActionChains(self.driver) \
            .move_to_element(element) \
            .click_and_hold(element) \
            .move_by_offset(*offset) \
            .release()
        drawing.perform()

    @retry(NoSuchElementException, tries=2, delay=2)
    def find_element(self, locator):
        """
        Find and return element based on the given locator value
        E.g: draggableElement = ("xpath@@//div[@id='draggable']")
        :param locator: Element locator strategy
        :return: Element
        """
        return self.driver.find_element(*self.__get_by(locator_with_strategy=locator))

    def find_child_element(self, element, locator):
        by = self.__get_by(locator_with_strategy=locator)
        return element.find_element(*by)

    def find_child_elements(self, element, locator):
        by = self.__get_by(locator_with_strategy=locator)
        return element.find_elements(*by)

    def __get_by(self, locator_with_strategy):
        """
        Get and return By instance based on the locator strategy
        :param locator_with_strategy: Element locator strategy
        :return: By instance of the element
        """
        if "@@" not in locator_with_strategy:
            locator_with_strategy = Strategy.ID.value + "@@" + locator_with_strategy

        strategy_and_locator = str(locator_with_strategy).split("@@")
        strategy = strategy_and_locator[0]
        locator = strategy_and_locator[1]
        by = None
        if strategy == Strategy.XPATH.value:
            by = (By.XPATH, locator)
        elif strategy == Strategy.ID.value:
            by = (By.ID, locator)
        elif strategy == Strategy.CSS.value:
            by = (By.CSS_SELECTOR, locator)
        elif strategy == Strategy.TAGNAME.value:
            by = (By.TAG_NAME, locator)
        return by

    def find_elements(self, locator):
        """
        Find and return the list of webelements based on the given locator value
        :param locator: Element locator strategy
        :return: list of the elements
        """
        return self.driver.find_elements(*self.__get_by(locator_with_strategy=locator))

    @retry(StaleElementReferenceException, tries=5, delay=2)
    def get_attribute(self, locator, attribute):
        """
        Get the provided attribute value for the given element
        :param locator: Element locator strategy
        :param attribute: attribute
        :return: value of the attribute
        """
        if isinstance(locator, WebElement):
            return locator.get_attribute(attribute)
        else:
            element = self.find_element(locator)
            return element.get_attribute(attribute)

    def drag_and_drop(self, draggable, droppable):
        """
        Performs drag and drop action using selenium action class
        :param draggable: draggable element
        :param droppable: droppable element
        :return:
        """
        try:
            action = ActionChains(self.driver)
            action.drag_and_drop(draggable, droppable).perform()
        except Exception as e:
            raise e

    def sleep_in_seconds(self, seconds=1):
        """
        Method for hard wait as per given seconds
        :param seconds: time in seconds
        :return:
        """
        time.sleep(seconds)

    def select_value_from_dropdown(self, locator, value):
        """
        It will select value from dropdown based on visible text
        :param locator: dropdwon Element locator strategy
        :return:
        """
        element = self.find_element(locator)
        select = Select(element)
        time.sleep()
        select.select_by_visible_text(value)

    def select_value_from_dropdown_by_index(self, locator, index):
        """
        It will select first value from dropdown
        :param locator: dropdwon Element locator strategy
        :param index: index of the dropdown element
        :return:
        """
        element = self.find_element(locator)
        select = Select(element)
        time.sleep(3)
        select.select_by_index(index)
        time.sleep(3)

    def explicit_wait(self, locator):
        """
        Smart Wait in Selenium, wait till element is clickable
        :param locator: Element locator strategy
        :return: Found Element
        """
        element = self.find_element(locator)
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        except Exception as e:
            raise e
        return element

    def select_dropdown_option(self, locator, option_text):
        """
        Selects the option in the drop-down based on the tag text
        :param locator: element
        :param option_text: value to be selected
        :return:
        """
        dropdown = self.find_element(locator)
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

    def hit_enter(self, locator, wait_time=2):
        """
        Hit Enter
        :param locator: element
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.ENTER)
            self.sleep_in_seconds(wait_time)
        except Exception as e:
            raise e

    def send_keys(self, locator, *keys):
        """
        send keys to locator
        :param locator: element
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(*(keys))
        except Exception as e:
            raise e

    def scroll_down(self, locator, wait_time=2):
        """
        Scroll down WebPage
        :param locator: locator
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.PAGE_DOWN)
            self.sleep_in_seconds(wait_time)
        except Exception as e:
            raise e

    def hover(self, locator, wait_seconds=2):
        """
        Hover over the element
        :param locator: locator
        :param wait_seconds: time to wait
        :return:
        """
        element = self.find_element(locator)
        action_obj = ActionChains(self.driver)
        action_obj.move_to_element(element)
        action_obj.perform()
        self.sleep_in_seconds(wait_seconds)

    def read_browser_console_log(self, log_type='browser'):
        """
        Read Browser Console log
        :param log_type: driver.get_log('browser')
            driver.get_log('driver')
            driver.get_log('client')
            driver.get_log('server')
        :return: logs
        """
        return self.driver.get_log(log_type)

    def execute_javascript(self, js_script):
        """
        Execute javascipt
        :param js_script:
        :return:
        """
        try:
            self.driver.execute_script(js_script)
        except Exception as e:
            raise e

    def accept_alert(self):
        """
        Accepts Java Alert
        :return:
        """
        try:
            self.driver.switch_to_alert().accept()
        except NoAlertPresentException:
            raise NoAlertPresentException

    def dismiss_alert(self):
        """
        Dismiss Java Alert
        :return:
        """
        try:
            self.driver.switch_to_alert().dismiss()
        except NoAlertPresentException:
            raise NoAlertPresentException

    def wait_till_element_is_present(self, locator, timeout=10):
        """
        WebDriver Explicit wait till element is present
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout). \
                until(EC.presence_of_element_located(self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_element_is_visible(self, locator, timeout=10):
        """
        WebDriver Explicit wait till element is visible, once disappeared wait will over
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """
        web_element = self.find_element(locator)
        try:
            element = WebDriverWait(self.driver, timeout). \
                until_not(EC.visibility_of_element_located(web_element))
            return element
        except Exception as e:
            raise e

    def teardown_browser(self):
        """
        Close all browser instances
        :return:
        """
        self.driver.quit()

    def close_browser(self):
        """
        Close current browser instance
        :return:
        """
        self.driver.close()

    def disconnect_browser(self):
        """
        Disconnect browser
        :return:
        """
        # network_conditions = self.get_network_conditions()
        # self.driver.set_network_conditions(offline=True, latency=network_conditions["latency"],
        #                                     download_throughput=network_conditions["download_throughput"],
        #                                     upload_throughput=network_conditions["upload_throughput"])
        self.driver.set_network_conditions(
            offline=True,
            latency=1,  # additional latency (ms)
            download_throughput=500 * 1024,  # maximal throughput
            upload_throughput=500 * 1024)  # maximal throughput

    def connect_browser(self):
        """
        Connect browser
        :return:
        """
        # network_conditions = self.get_network_conditions()
        # self.driver.set_network_conditions(offline=False, latency=network_conditions["latency"],
        #                                     download_throughput=network_conditions["download_throughput"],
        #                                     upload_throughput=network_conditions["upload_throughput"])
        self.driver.set_network_conditions(
            offline=False,
            latency=1,  # additional latency (ms)
            download_throughput=500 * 1024,  # maximal throughput
            upload_throughput=500 * 1024)  # maximal throughput

    def get_network_conditions(self):
        """
        Gets Chrome network emulation settings
        :return: A dict. For example:
                {'latency': 4, 'download_throughput': 2, 'upload_throughput': 2,
                'offline': False}
        """
        return self.driver.get_network_conditions()

    def print_version(self):
        """
        Prints version
        :return:
        """
        print("print_version = 2.0")

    def maximize_browser(self):
        """
        Maximize the browser
        :return:
        """
        self.driver.maximize_window()

    def back(self):
        """
        browser back button
        :return:
        """
        self.driver.back()

    def is_element_present(self, locator):
        """
        Check the presence of element.
        :return: Boolean
        """
        try:
            self.sleep_in_seconds(2)
            self.find_element(locator)
        except:
            return False
        return True

    def get_css_value(self, locator, css_property):
        """"
        This method will get the CSS property of the element
        :return: CSS property Value

        Usage
        get_css_value(locator,"color")
        get_css_value(locator,"font-family")
        get_css_value(locator,"font-size")
        The above code will return value in RGB format such as “rgba(36, 93, 193, 1)”
        """
        element = self.find_element(locator)
        return element.value_of_css_property(css_property)

    def get_current_window_handle(self):
        """
        Returns the handle of the current window.
        :return: string containing current window handle
        """
        return self.driver.current_window_handle

    def get_window_handles(self):
        """
        Returns the list containing handles of all windows within the current session.
        :return: list containing all opened window handles in current session
        """
        return self.driver.window_handles

    def is_special_char_available(self, url):

        url = unquote(url)
        allowed_ascii = range(128)
        try:
            for literal in url:
                try:
                    if not ord(literal) in allowed_ascii:
                        return True
                except TypeError as e:
                    raise TypeError(str(e), url, literal)
            return False
        except Exception as e:
            raise Exception("Unable to check special character: "+ str(e))


    def switch_to_new_window(self, win_handle):
        """
        Switch to window corresponding to windows handle id
        :return:
        """
        self.driver.switch_to_window(win_handle)

    def refresh_browser(self):
        """
        Refreshes the page
        :return:
        """
        self.driver.refresh()


    def download_bluestacks(self,locator,page):
        """
        Click the download bluestacks button
        :return:
        """
        try:

            self.wait_till_element_is_present(locator)
            element = self.find_element(locator)
            display = self.get_css_value(locator, css_property="display")
            visibility = self.get_css_value(locator, css_property="visibility")
            opacity = self.get_css_value(locator, css_property="opacity")
            if display != "none" or visibility != "hidden" or opacity != 0:
                self.click(locator)
                self.driver.get("chrome://downloads")
                time.sleep(10)
                manager = self.driver.find_element_by_css_selector('body/deep/downloads-manager')
                shadow = self.driver.execute_script('return arguments[0].shadowRoot;', manager)
                item = shadow.find_element_by_css_selector('iron-list>downloads-item')
                shadow = self.driver.execute_script('return arguments[0].shadowRoot;', item)
                file_name = shadow.find_element_by_css_selector('div#details>#title-area>a')
                downloaded_file = str(file_name.text)
                time.sleep(20)
                file_size = self.get_size(downloaded_file)
                self.remove_file(downloaded_file)
                return file_size
            else:
                return False
        except Exception as e:
            raise Exception("Unable to click on download button on page "+page+" due to " + str(e))

    def get_size(self,file):
        """
        Function to check the size of the file
        :return:
        """
        try:
            file_size = os.path.getsize(f"C:\\Users\\{os.environ['USERNAME']}\\Downloads\\"+str(file))
            return file_size
        except Exception as e:
            raise Exception("Unable to get file size: "+ str(e))

    def remove_file(self,file):
        """
        Function to remove the file from location
        :param file:
        :return:
        """
        if file:
            os.remove(f"C:\\Users\\{os.environ['USERNAME']}\\Downloads\\"+str(file))


    # def get_element_screen_shot(self, locator, filename):
    #     element = self.find_element(locator)
    #     location = element.location
    #     size = element.size
    #     self.get_full_page_screen_shot(filename)
    #     im = Image.open(filename)  # uses PIL library to open image in memory
    #
    #     left = location['x']
    #     top = location['y']
    #     right = location['x'] + size['width']
    #     bottom = location['y'] + size['height']
    #
    #     im = im.crop((left, top, right, bottom))  # defines crop points
    #     im.save(filename)  # saves new cropped image

    def get_full_page_screen_shot(self, filename):
        self.driver.save_screenshot(filename)

    def get_page_cookies(self):
        return self.driver.get_cookies()

    def get_page_useragent(self):
        return self.driver.execute_script("return navigator.userAgent")

    def get_page_type(self, url):
        page_comps = url.split('/')
        locale_list = ['tw', 'vi', 'tr', 'th', 'ru', 'pt-br', 'pl', 'nl', 'ms', 'ko', 'ja', 'it', 'id', 'fr', 'es',
                       'de', 'cs', 'ar']
        locale = 'en'
        if page_comps[3] in locale_list:
            locale = page_comps[3]
        if page_comps[-1] == "index.html":
            return ('homepage', locale)
        if page_comps[-1] == "blog.html":
            return ('blog', locale)
        if page_comps[-1] == "affiliate-guides.html":
            return ('affiliate-guides', locale)
        if page_comps[-1] == "bluestacks-4.html":
            return ('bluestacks-4', locale)
        if page_comps[-1] == "affiliate.html":
            return ('affiliate.html', locale)
        if page_comps[-1] == "copyright-dispute-policy.html":
            return ('copyright-dispute-policy.html', locale)
        if page_comps[-1] == "terms-and-privacy.html":
            return ('terms-and-privacy.html', locale)
        if page_comps[-1] == "about-us.html":
            return ('about-us.html', locale)
        if page_comps[-1] == "apps.html":
            return ('apps.html', locale)
        if 'download.html' in page_comps[3]:
            return ('download.html', locale)
        if locale != 'en':
            index = 4
        else:
            index = 3
        if page_comps[index] == 'apps':
            return ('apps', locale)
        elif page_comps[index] == 'blog':
            return ('blog', locale)
        elif page_comps[index] == 'about-us':
            return ('about-us', locale)
        elif page_comps[index] == 'bluestacks-4':
            return ('bluestacks-4', locale)
        elif page_comps[index] == 'terms-and-privacy':
            return ('terms-and-privacy', locale)
        else:
            return ('unknown', locale)

    def get_page_locale(self,url):
        try:
            locale_list = ['tw', 'vi', 'tr', 'th', 'ru', 'pt-br', 'pl', 'nl', 'ms', 'ko', 'ja', 'it', 'id', 'fr', 'es',
                           'de', 'cs', 'ar']
            locale = url.split('/')[3]
            if locale in locale_list:
                return locale
            else:
                return 'en'
        except IndexError as e:
            locale = 'en'
            return locale

    def get_console_error_logs(self, driver_obj):
        return driver_obj.get_log('browser')








    # def take_screenshot(drv_obj):
    #     """
    #     Take screenshot
    #     :return:
    #     """
    #     logging.info("Taking screenshot:")
    #     #timestr = time.strftime("%Y%m%d-%H%M%S")
    #     timestr = round(time.time() * 1000)
    #     filename = str(timestr) + "-screenshot.png"
    #     image = get_full_path() + '/screenshot/' + filename
    #     drv_obj.get_full_page_screen_shot(image)
    #
    #     request = HttpRequest()
    #     response = request.upload_file(gui_cs.upload_logs_url, image)
    #     logger.debug("Response: " + str(response.content))
    #     logger.debug("Status Code: " + str(response.status_code))
    #
    #     with open(image, "rb") as fh:
    #         temp = fh.read()
    #     logger.info(
    #         "Screenshot URL: " + gui_cs.upload_logs_url + "/" +filename,
    #         attachment={
    #             "name": os.path.basename(image),
    #             "data": temp,
    #             "mime": "application/octet-stream",
    #         },
    #     )
    #     time.sleep(2)

class Strategy(Enum):
    """
    Locator Strategy Constants
    """
    XPATH = "xpath"
    ID = "id"
    CSS = "css"
    TAGNAME = "tag name"

class dbconfiguration:
    def __init__(self):
        with open(os.path.join(os.path.abspath(__file__ + "/../../"), "Static\\dbconfig.json"), 'r') as config:
            values = json.load(config)
            self.host = values.get('host','')
            self.database = values.get('database','')
            self.port = values.get('port', 0)
            self.user = values.get('user','')
            self.password = values.get('password','')

    def getdbconnection(self):
        try:
            self.mySQLConnection = mysql.connector.connect(
                host = self.host,
                database = self.database,
                port = self.port,
                user = self.user,
                password = self.password
                )
        except mysql.connector.Error as e:
            print("Error code:", e.errno)
            print ("SQLSTATE value:", e.sqlstate)
            print ("Error message:", e.msg)
            print ("Error:", e)
            s = str(e)
            print ("Error:", s)

    def select_query(self, select_query):
        connection = self.mySQLConnection
        cursor = connection.cursor()
        cursor.execute(select_query)
        records = cursor.fetchall()
        return records
