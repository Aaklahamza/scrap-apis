
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .helpers import string_to_soup
from .crawler import Crawler

class DynamicCrawler(Crawler):

    def __init__(self, driver_path):
        super().__init__()
        self.driver_path = driver_path
        self.driver = None
        self.driver = self.get_driver()

    # get webdriver
    def get_driver(self):
        if self.driver != None:
            return self.driver
        options = Options()
        # no UI
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument("--mute-audio")
        options.add_argument('--disable-popup-blocking')
        options.add_argument("user-agent=APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)")
        chrome_prefs = {}
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        options.experimental_options['prefs'] = chrome_prefs
        driver = webdriver.Chrome(self.driver_path, options=options)
        driver.implicitly_wait(3)
        self.driver = driver
        return self.driver

    def get_html(self, url, middlewares=[]):
        driver = self.get_driver()
        driver.get(url)

        # TODO : chain of actions before getting the html
        for func in middlewares:
            print("middleware : ", func.__name__)
            func(driver)
        soup = self.get_html_now()
        return soup

    def get_html_now(self):
        return string_to_soup(self.get_driver().page_source)

    def destroy_driver(self):
        if self.driver != None:
            self.driver.quit()
        self.driver = None

    def __del__(self):
        self.destroy_driver()
