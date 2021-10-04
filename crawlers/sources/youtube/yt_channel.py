from .youtube import Youtube
import fuckit

class YtChannel(Youtube):

    def __init__(self, key):
        super().__init__(key)

    def build_request(self, cids):
        url = self.init_url + "/channels?"
        d = {}
        d['key'] = self.key
        d['part'] = 'snippet,statistics'
        d['id'] = ",".join(cids)
        d['maxResults'] = "50"
        return url + "&".join([k + "=" + d[k] for k in d.keys()])

    def parse(self, data):
        @fuckit
        def parse_one(item):
            d = {}
            d['id'] = item['id']
            snippet = item['snippet']
            d['country'] = snippet['country']
            d['description'] = snippet['description']
            d['publishedAt'] = snippet['publishedAt']
            d['title'] = snippet['title']
            stats = item['statistics']
            for k in stats:
                d[k] = stats[k]
            return d

        items = data['items']
        return list(map(parse_one, items))

    def run(self, cids):
        req = self.build_request(cids)
        res = self.get_response(req)
        p_res = self.parse (res)
        return p_res
