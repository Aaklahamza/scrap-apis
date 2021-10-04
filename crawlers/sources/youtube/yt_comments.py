from .youtube import Youtube

class YtComments(Youtube):
    def __init__(self, key):
        super().__init__(key)

    def build_request(self,
                      vid,
                      page=""):
        url = self.init_url + "/commentThreads?"

        d = {}
        d['key'] = self.key
        d['maxResults'] = "50"
        d['part'] = "snippet"
        d['videoId'] = vid
        if page != "":
            d['pageToken'] = page
        return url + "&".join([k + "=" + d[k] for k in d.keys()])

    def parse(self,
              data,
              plus={}):
        v = {}
        v['id'] = data['id']
        snippet = data['snippet']
        v['videoId'] = snippet['videoId']
        v['replies'] = snippet['totalReplyCount']
        t_snippet = snippet['topLevelComment']['snippet']
        v['authorName'] = t_snippet['authorDisplayName']
        v['authorId'] = t_snippet['authorChannelId']['value']
        v['text'] = t_snippet['textOriginal']
        v['likes'] = t_snippet['likeCount']
        v['publishedAt'] = t_snippet['updatedAt']
        return {**v, **plus}

    def run(self,
            vid,  # video id
            page="",  # page token
            all_pages=True # exhaust all pages
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

