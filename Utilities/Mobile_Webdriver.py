from appium import webdriver

class GetWebdriver():

    @staticmethod
    def get_webdriver(browser):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['browserName'] = browser
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)