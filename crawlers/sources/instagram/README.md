# Instagram

## Examples
A crawler for collecting data from instagram.


### initialize

```python 
from crawlers.sources.instagram import *

username = ""
password = ""
driver_path = ""

instagram = Instagram(username, password)
instagram_search = InstagramSearch( username, 
                                    password, 
                                    driver_path=driver_path)
                                    
```

### run
```python
instagram_search.login()

user_posts_links = instagram_search.get_user_links(user="hailey_bieber._", number_of_posts=100)
htag_posts_links = instagram_search.get_htag_links(hashtag="stop490", number_of_posts=1300)


instagram.login()
htag_posts = instagram.get_htag_posts(   hashtag, 
                            posts_number,
                            how='top')
user_posts = instagram.get_user_posts( username,
                          number_of_posts=12)
post_comments = instagram.get_comments(post_url)
user_info = instagram.get_user_info(user, by_username=False)
```