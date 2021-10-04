# requests
from bs4 import BeautifulSoup
from more_itertools import unique_everseen
import re

# imports used in Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# time
from time import sleep
import time


class InstagramSearch():
    """
    Class that allows you to scrape the links of Instagram pages, either
    a profile or a hashtag.

    Initialised with the location of your Chromedriver location

    """

    def __init__(self, username, password, driver_path):
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(self.driver_path)
        self._password = password
        self._username = username

    def login(self):

        # intiate driver
        print("Launching driver...")

        # base url
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(2)

        username_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        username_field.send_keys(self._username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        password_field.send_keys(self._password)

        sleep(3)

        # find log in button
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        sleep(3)

        # handle alerts
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

        return self.driver

    def get_htag_links(self, hashtag, number_of_posts, SCROLL_PAUSE_TIME=5):
        tag_url = 'https://www.instagram.com/explore/tags/'  # set base url
        url = tag_url + hashtag  # set url to scrape from
        return self.scrapeLinks(url, number_of_posts, SCROLL_PAUSE_TIME)

    def get_user_links(self, user, number_of_posts, SCROLL_PAUSE_TIME=5):
        user_url = 'https://www.instagram.com/'  # set base url
        url = user_url + user  # set url to scrape from
        return self.scrapeLinks(url, number_of_posts, SCROLL_PAUSE_TIME)  # return url to scrape from


    def scrapeLinks(self, url, target, SCROLL_PAUSE_TIME):

        """
        Function that scrapes the links needed
        Args:
            target_url, number_of_posts
        Returns:
            list of links
        """

        def page_is_loading(driver):
            return len(driver.find_elements_by_css_selector('._9qQ0O')) == 1


        def get_page_links(driver):
            data = BeautifulSoup(driver.page_source, 'html.parser')
            body = data.find('body')
            links = []
            for link in body.find_all('a'):
                if link.get('href').startswith('/p/'):
                    links.append('https://www.instagram.com' + link.get('href'))
            return links

        # pass url as argument to Selenium webDriver, loads url
        self.driver.get(url)

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        # initiate empty list for unique Instagram links
        links = []

        # this loops round until n links achieved or page has ended
        while page_is_loading(self.driver):

            links += get_page_links(self.driver)

            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # update on successful links scraped
            print("Scraped ", len(links), " links, ", len(set(links)), ' are unique')

            # if n target met then while loop breaks
            if len(set(links)) > int(target):
                break

        # links are saved as an attribute for the class instance
        links += get_page_links(self.driver)
        links = list(unique_everseen(links))

        print(f"{len(links)} Unique links obtained. Closing driver")

        # close driver
        self.driver.quit()

        return links
