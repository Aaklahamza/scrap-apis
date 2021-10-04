# Facebook

## Examples

### Posts

```python 

fb_posts = FacebookPosts()
posts = fb_posts.get_posts(username="almuhandissarcasm", pages=5)

```

### Comments
```python
fb_page_comments = FacebookPageComments(driver_path = "chromedriver.exe")
fb_page_comments.login( email, password )

post_id = "206555864554844"
page_id = "1465622106863621"

comments = fb_page_comments.get_post_comments(post_id, page_id, 3)
```

### Page & Profile Infos

```python

# pages
fb_page = FacebookPage( driver_path = "chromedriver.exe" )
fb_page.login(email, password)
fb_page.get_info('maghrebvoices')

# profiles
fb_profile = FacebookProfile( driver_path = "chromedriver.exe" )
fb_profile.login(email, password)
fb_profile.get_info('MouhcineTo1')


```
