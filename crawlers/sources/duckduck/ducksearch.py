import urllib
from crawlers.core import DynamicCrawler

class DuckSearch(DynamicCrawler):

    def __init__(self, driver_path):
        super().__init__(driver_path)

    def build_url(self, query):  # setting url for the query

        qry = urllib.parse.quote_plus(query)
        url = "https://duckduckgo.com/?q=" + qry + "&t=h_&ia=web"
        return url

    def find_desc(self, query):  # using selenium to get the info shown in the description of first result

        l = []
        soup = self.get_html(self.build_url(query))
        website_info = soup.find_all("div", {"class": "result__snippet js-result-snippet"})[0].text

        element = {
            'website': query,
            'description': website_info
        }
        l.append(element)
        return l  # return element of website and its description

    def run(self, list_websites):  # runs for list of websites returns dict
        all_res = []
        for website in list_websites:
            res = self.find_desc(website)
            all_res += res
        return all_res
