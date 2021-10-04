

from crawlers.core import DynamicCrawler


class Facebook(DynamicCrawler):
    def __init__(self, driver_path):
        super().__init__(driver_path)

    def login(self,
               email,
               password):
        # sign in
        self.driver.get("https://mbasic.facebook.com/login")
        email_ = self.driver.find_element_by_xpath('//*[@id="m_login_email"]')
        email_.send_keys(email)
        password_ = self.driver.find_element_by_xpath('//*[@id="password_input_with_placeholder"]/input')
        password_.send_keys(password)
        button = self.driver.find_element_by_xpath('//*[@id="login_form"]/ul/li[3]/input')
        button.click()