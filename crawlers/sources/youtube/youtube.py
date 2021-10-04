
import requests



class QuotaExceededError(Exception):
    pass

class EmptyResponseError(Exception):
    pass




class Youtube:

    def __init__(self, key):
        self.key = key
        self.init_url = "https://www.googleapis.com/youtube/v3"

    def build_request(self, **kwargs):
        pass

    def parse(self,
              data,
              plus={}):
        return {**data, **plus}


    def get_response(self, url):
        res = requests.get(url)

        if res.status_code != 200:
            if "quotaExceeded" in str(res.json()):
                raise QuotaExceededError('quota exceeded, change the API key or wait')

        res = res.json()
        if not (('items' in res) and (len(res['items']) > 0)):
            print(res)
            raise EmptyResponseError('no data in response')
        return res

    def run(self, **kwargs):
        pass
