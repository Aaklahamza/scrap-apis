import urllib
from crawlers.core import StaticCrawler
import fuckit
from crawlers.common import sanitize


class GSearch(StaticCrawler):

    def __init__(self):
        super().__init__()

    def build_url(self, query, num = 20):
        qry = urllib.parse.quote_plus(query)
        url = "https://www.google.co.uk/search?q=" + qry + "&num="+str(num)
        return url


    @sanitize
    @fuckit
    def parse_one(self, html, plus={}):
        d = {}
        d['link'] = html.find('a', href=True).get('href').replace('/url?q=', '')
        d['title'] = html.find("div", {"class": 'BNeawe vvjwJb AP7Wnd'}).text
        d['website'] = html.find("div", {"class": 'BNeawe UPmit AP7Wnd'}).text.split(' ')[0]
        return {**d, **plus}

    def parse(self, html, plus={}):
        res = list( map( lambda x: {'url': x.parent.get('href'), 'title': x.text}, html.find_all('h3') ) )
        data = list(filter( lambda x: x['url'] is not None, res ))

        for i in range(len(data)):
            data[i]['rank'] = i+1
            data[i]['url'] = data[i]['url'].replace('/url?q=', '')
            data[i]['website'] = urllib.parse.urlparse(data[i]['url']).netloc

        data = list(map( lambda x: {**x, **plus}, data))
        return data

    def run(self, query, num = 20):
        url = self.build_url(query,num)
        response = self.get_html(url)
        results = self.parse(response, {'query': query})
        return results
