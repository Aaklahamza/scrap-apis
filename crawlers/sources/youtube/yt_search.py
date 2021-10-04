from .youtube import Youtube


class YtSearch(Youtube):

    def __init__(self, key):
        super().__init__(key)

    def build_request(self,
                      query,
                      start_date="",
                      end_date="",
                      channel="",
                      page=""):

        url = self.init_url + "/search?"
        d = {}
        d['key'] = self.key
        d['order'] = "relevance"
        d['maxResults'] = "50"
        d['type'] = "video"
        d['part'] = "snippet"
        d['regionCode'] = "MA"

        d['q'] = query
        if channel != "":
            d['channelId'] = channel
        if end_date != "":
            d['publishedBefore'] = end_date + "T00:00:00Z"
        if start_date != "":
            d['publishedAfter'] = start_date + "T00:00:00Z"
        if page != "":
            d['pageToken'] = page
        return url + "&".join([k + "=" + d[k] for k in d.keys()])

    def parse(self,
              data,
              plus={}):
        v = {}
        v['videoId'] = data['id']['videoId']
        snippet = data['snippet']
        v['channel'] = snippet['channelTitle']
        v['channelId'] = snippet['channelId']
        v['title'] = snippet['title']
        v['description'] = snippet['description']
        v['date'] = snippet['publishedAt']
        return {**v, **plus}

    def run(self,
            query,  # string query
            start_date="",  # start date ( eg. "2020-01-10" )
            end_date="",  # same format as start_date
            channel="",  # channel id
            page="",  # page token to consider
            max_rounds=-1):

        if max_rounds == 0:
            return []

        print('round ', max_rounds)
        data = []
        req = self.build_request(query,
                                 start_date,
                                 end_date,
                                 channel,
                                 page)
        res = self.get_response(req)
        data += list(map(self.parse, res['items']))

        if max_rounds == 1:
            return data

        if 'nextPageToken' in res:
            next_page = res['nextPageToken']
            data += self.run(query,
                             start_date,
                             end_date,
                             channel,
                             page=next_page,
                             max_rounds=max_rounds-1)

        return data
