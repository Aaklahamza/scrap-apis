# Google

## Examples
A crawler for collecting search results from Google for a specific query.


### initialize

```python 
from crawlers.sources.google import GSearch
search = GSearch()
```

### run
```python
data = search.run(query='data science')
```