
from .youtube import Youtube


class YtMetadata(Youtube):

    def __init__(self, key):
        super().__init__(key)

    def build_request(self, vids):
        url = self.init_url + "/videos?"
        d = {}
        d['key'] = self.key
        d['part'] = 'statistics'
        d['id'] = ",".join(vids)
        return url +"&".join( [ k+ "=" + d[k] for k in d.keys()])

    def parse(self,
              data,
              plus={}):
        v = data['statistics']
        for k in v.keys():
            if v[k] != '':
                v[k] = int(v[k])
        v['id'] = data['id']
        return {**v, **plus}

    def run(self,
            vids  # list of videos to collect their stats, takes between 1 and 50 ids.
            ):
        data = []
        req = self.build_request(vids)
        res = self.get_response(req)
        data += list(map( self.parse, res['items']))
        return data
