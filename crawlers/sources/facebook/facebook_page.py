# importing libraries
import pandas as pd
from time import sleep
from lxml import html
from .facebook import Facebook
import warnings
warnings.filterwarnings('ignore')

        
class FacebookPage(Facebook):
    
    def __init__(self, driver_path):
        super().__init__(driver_path)
        
    def build_url(self,
                       username):
        return "https://web.facebook.com/{username}/about/?ref=page_internal".format(username = username)
    
    def get_info(self, username):
        link_page = self.build_url(username)
        self.driver.get(link_page)
        sleep(3)
        d = {}
        page_source = self.driver.page_source
        tree = html.fromstring(page_source)

        root = tree.xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div[1]')[0]
        adress              = root.xpath('/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div/div/span/a/@href')
        people_like_this    = root.xpath('/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/text()')
        people_follow_this  = root.xpath('/div[2]/div/div[3]/div/div/div/div[2]/div/div/span/span/text()')
        category            = root.xpath('/div[2]/div/div[5]/div[1]/div/div/div/div[2]/div/div/span/span[1]/a/span/text()')
        instagram           = root.xpath('/div[5]/div/div[2]/div[1]/div/div/div/div[2]/div/div/span/span/a/text()')
        phone               = root.xpath('/div[5]/div/div[3]/div[1]/div/div/div/div[2]/div/div/span/span/text()')
        email               = root.xpath('/div[5]/div/div[4]/div[1]/div/div/div/div[2]/div/div/span/span/a/text()')
        about               = root.xpath('/div[6]/div/div[2]/div[1]/div/div/div/div[2]/div/div/span/div/div[2]/span/div/div/text()')
    
        d['adress'] = ' '.join(adress)
        d['people_like_this'] = ' '.join(people_like_this)
        d['people_follow_this'] = ' '.join(people_follow_this)
        d['category'] = ' '.join(category)
        d['instagram'] = ' '.join(instagram)
        d['phone'] = ' '.join(phone)
        d['email'] = ' '.join(email)
        d['about'] = ' '.join(about)
        return d

