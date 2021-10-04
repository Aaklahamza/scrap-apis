# DuckDuckGo

## Examples
A crawler for collecting website description from Duckduckgo.


### initialize

```python 
from crawlers.sources.duckduck import DuckSearch
dsearch = DuckSearch()
```

### run
```python
desc_data = dsearch.run(list_websites=['webteb.com','doctissimo.fr'])
```