from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.chrome.options import Options as _chrome_options
from selenium.webdriver.firefox.options import Options

def __browser__(user_browser, headless):
    global driver
    chrome_options = _chrome_options()
    chrome_options.add_argument("--headless")
    fireFoxOptions = Options()
    fireFoxOptions.headless = True
    if user_browser == 'Chrome':
        if headless == True:
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Chrome()
    if user_browser == 'Firefox':
        if headless == True:
            driver = webdriver.Firefox(options=fireFoxOptions)
        else:
            driver = webdriver.Firefox()
    if user_browser == 'Edge':
        if headless == True:
            raise Exception('Selenium driver cannot be headless and Edge.')
        else:
            driver = webdriver.Edge()
    return driver