from .youtube import Youtube


class YtRelated(Youtube):

    def __init__(self, key):
        super().__init__(key)

    def build_request(self, vid, page=""):
        url = self.init_url+"/search?"
        d = {}
        d['key'] = self.key
        d['maxResults'] = "50"
        d['type'] = "video"
        d['part'] = "snippet"
        d['regionCode'] = "MA"
        d['relatedToVideoId'] = vid
        if page != "":
            d['pageToken'] = page
        return url+"&".join( [ k+"="+d[k] for k in d.keys() ] )

    def parse(self,
              data,
              plus={}):
        v = {}
        v['id'] = data['id']['videoId']

        if 'snippet' in data:
            snippet = data['snippet']
            v['channel'] = snippet['channelTitle']
            v['channelId']  = snippet['channelId']
            v['title'] = snippet['title']
            v['description'] = snippet['description']
            v['date'] = snippet['publishedAt']
        return {**v, **plus}

    def run(self,
            vid,  # video id
            page="",  # page token
            all_pages=False  # exhaust all pages
            ):
        data = []
        req = self.build_request(vid, page)
        res = self.get_response(req)
        data += list(map( self.parse, res['items']))

        if not all_pages:
            return data

        if 'nextPageToken' in res:
            next_page = res['nextPageToken']
            data += self.run(vid, page=next_page)

        return data


