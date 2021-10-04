
from lxml import etree, html
import warnings
warnings.filterwarnings('ignore')

from .facebook import Facebook
        

    
class FacebookPageComments(Facebook):
    
    def __init__(self, driver_path):
        super().__init__(driver_path)
        
        
    def build_post_url(self, 
                       post_id, 
                       page_id, 
                       page=1):
        return "https://mbasic.facebook.com/story.php?story_fbid={post_id}&id={page_id}&p={page}".format(post_id=post_id, 
                                                                                               page_id=page_id,
                                                                                               page=str(page*10))
        
    
    # parses one comment
    def parse_comment(self, 
                      comment):
        href_author = comment.xpath("div/h3/a/@href")
        author      = comment.xpath("div/h3/a/text()")
        content     = comment.xpath("div/div[1]/text()")
        reactions   = comment.xpath("div/div[3]/span[1]/span/a[1]/text()")
        date        = comment.xpath("div/div[3]/abbr/text()")

        d = {}
        d['href_author'] = ' '.join(href_author)
        d['author'] = ' '.join(author)
        d['content'] = ' '.join(content)
        d['reactions'] = ' '.join(reactions)
        d['date'] = ' '.join(date)
        return d
    
    # extracts comments from a post
    def get_post_comments_one_page(self,
                          post_id,
                          page_id,
                          page=1):
        
        link_post = self.build_post_url(post_id, page_id, page)
        self.driver.get(link_post)
        
        
        data = []
        html_source = self.driver.page_source
        tree = html.fromstring(html_source)
        comments = tree.xpath("/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[5]/div")[1:]
        data = list(map(  lambda comment : {**self.parse_comment(comment), **{'post_url': link_post}}, 
                               comments ))
        
        return data
    
    
    def get_post_comments(self, 
                               post_id, 
                               page_id, 
                               pages=2):
        data = []
        for page in range(1, pages+1):
            data += self.get_post_comments_one_page(post_id, page_id, page )
        return data