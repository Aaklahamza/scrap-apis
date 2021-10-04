from time import sleep
from .helpers import string_to_soup
import requests
from .crawler import Crawler


class StaticCrawler(Crawler):

    def __init__(self):
        super().__init__()

    def get_html(self, url):
        try:
            r = requests.get(url,
                             headers=self.headers,
                             cookies=self.cookies,
                             proxies=self.proxies
                             )
            return string_to_soup(r.content)
        except KeyboardInterrupt:
            raise
