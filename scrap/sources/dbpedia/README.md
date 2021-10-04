# Dbpedia

## Examples
A crawler for collecting related vocabulary from Dbpedia.


### initialize

```python 
from crawlers.sources.dbpedia import Dbpedia
dbpedia = Dbpedia()
```

### run
```python
data = dbpedia.get_related(term='Data Science', 
                           limit=20,
                           lang="en")
```