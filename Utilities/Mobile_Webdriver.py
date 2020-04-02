from appium import webdriver

class GetWebdriver():

    @staticmethod
    def get_webdriver(browser):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['browserName'] = browser
        desired_caps['autoAcceptAlerts']= True
        desired_caps['autoGrantPermissions'] = True
        #desired_caps['udid'] = '65a44185'
        #desired_caps['chromedriverExecutable'] ='C:\\Users\\mathu\\AppData\\Local\\appium-desktop\\app-1.5.0\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\\win\\chromedriver.exe'
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)