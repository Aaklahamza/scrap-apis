
import facebook_scraper


class FacebookPagePosts:
    def __init__(self):
        pass

    def get_posts( self,
                   username,
                   pages=5 ):
        data = []
        my_keys = [ 'post_id',
                    'post_url',
                    'text',
                    'post_text',
                    'time' ,
                    'comments' ,
                    'shares' ,
                    'username',
                    'user_url']

        for post in facebook_scraper.get_posts( account=username, pages=pages ):
            data.append( { x: post[x] for x in my_keys } )
        return data