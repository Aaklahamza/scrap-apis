
# Youtube

## Youtube base class
A base class defining the common behaviors of the wrappers (eg. YtComments... ).<br>
On the same file ( youtube.py ), we defined few exceptions (eg. QuotaExceeded ). <br>

### behaviors
- **init** : constructor, sets the API key
- **build_request** : takes query parameters and returns an url to be sent to the API
- **parse** : parse the response of the API, if the response contains multiple items ( videos, comments ), 
    this method only parses one item. Use map() or for to parse all the items.
- **get_response** : responsible of sending the url to the API and returning the response in JSON.

## Inheritors

- **YtComments** : collecting comments of a video
- **YtMetadata** : collecting videos stats ( likes, dislikes.. )
- **YtRelated** : collecting similar videos to one video
- **YtSearch** : collecting query results of a search query
- **YtChannel** : collecting stats about a specific channel
## Examples 

### initialize
```python 

import pandas as pd
from crawlers.sources.youtube import *

api_key = "API_KEY_HERE"

yt_search = YtSearch( key=api_key )
yt_related = YtRelated( key=api_key )
yt_metadata = YtMetadata( key=api_key )
yt_comments = YtComments( key=api_key )
yt_channel = YtChannel( key=api_key )

```
### run
```python
START_DATE = '2020-10-16'
END_DATE = '2020-11-01'

# search
data = yt_search.run(   query="hespress", 
                        start_date=START_DATE, 
                        end_date=END_DATE, 
                        max_rounds=2 ) # will return 2*50 results at most, ( -1 to get everything )
                              
# related
data = yt_related.run(vid="Y9vq7kVJi60" )

# metadata
data = yt_metadata.run(vids=["vJbvzkXiex8"] )

# comments
data = yt_comments.run(vid="vJbvzkXiex8")


# channel stats
data = yt_channel.run( cids=['UC_LKhBiSqiBLbFC3wFY2BRA'] )
```