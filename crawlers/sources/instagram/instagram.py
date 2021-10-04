from instagrapi import Client

class Instagram:

    """
    Class that allows you to scrape the content of Instagram
    """

    def __init__(self, username, password):
        self._password = password
        self._username = username
        self.client = Client()
    
    def login(self):
        if self.client.login(self._username, self._password) :
            print('Successfully logged in..')
        else :
            print("Couldn't login")
    
    def logout(self):
        if self.client.logout():
            print('Successfully logged out..')
        else :
            print( "Couldn't logout")
    
    def get_htag_posts(self, 
                       hashtag, 
                       posts_number=20,
                       how='top'):

        """
        Function that scrapes the medias for the given target (hashtag/user)
        if hashtag 
        Args:
            hashtag
            posts_number
            how: most recent posts or top posts (top/recent)
        Returns:
            a list of posts(medias)
        """
        posts = []
        if how == 'recent':
            posts = self.client.hashtag_medias_recent(hashtag, amount=posts_number)
            
        elif how == 'top':
            posts = self.client.hashtag_medias_top(hashtag, amount=posts_number)
        else:
            print(' wrong how')
            
        return posts
    
    
    def get_user_posts(self,
                       username,
                       number_of_posts=12):
        
        user_id = self.client.user_id_from_username(username)
        posts = self.client.user_medias(user_id, number_of_posts)
        return posts
    



    def get_comments(self, url):
        """
        Function that scrapes the comments from the given post
        Args:
            target_url
        Returns:
            a list of comments
        """
        
        comments = []
                
        post_id = self.client.media_id(self.client.media_pk_from_url(url))
        comments = self.client.media_comments(post_id)
        return comments
    
    def get_user_info(self, user, by_username=False):
        
        """
        Function that get info by username or user_id
        Args:
            username
        returns:
            User object
        """
        if by_username==True:
            return self.client.user_info_by_username(user)
        else:
            return self.client.user_info(user)