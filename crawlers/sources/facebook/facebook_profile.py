# importing libraries
import pandas as pd
from time import sleep
from lxml import html
from .facebook import Facebook
import warnings
warnings.filterwarnings('ignore')


class FacebookProfile(Facebook):

    def __init__(self, driver_path):
        super().__init__(driver_path)

    def build_url(self,
                       username):
        return 'https://web.facebook.com/{username}/about_contact_and_basic_info'.format(username=username)


    def get_info(self, username):
        link_profile = self.build_url(username)
        self.driver.get(link_profile)
        sleep(3)
        d_ = {}
        page_source = self.driver.page_source
        tree = html.fromstring(page_source)
        root = tree.xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]')[0]
        gender          = root.xpath('/div[2]/div/div/div[2]/div/div/div/div/div[1]/span/text()')
        birth_date      = root.xpath('/div[3]/div/div/div[2]/div[1]/div/div/div/div[1]/span/text()')
        birth_year      = root.xpath('/div[3]/div/div/div[2]/div[2]/div/div/div/div[1]/span/text()')
        religious_views = root.xpath('/div[4]/div/div/div[2]/ul/li/div/div/div[1]/span/text()')
        d_['username'] = username
        d_['gender'] = gender
        d_['birth_date'] = birth_date
        d_['birth_year'] = birth_year
        d_['religious_views'] = religious_views
        return d_

