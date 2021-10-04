
# Mongodb
a wrapper for Mongodb to insert data in bulk.


### initialize
```python 
from crawlers.providers.mongodb import MongoDb

mongodb = MongoDb(database="unfpa", collection="test")
```
### run
```python


rows = [{'videoId': 1, 'value': 'hello'}, 
        {'videoId': 2, 'value': 'hello'},
        {'videoId': 1, 'value': 'hello'}]

# insert data
mongodb.insert_data( [{'videoId': 3, 'value': 'hello'}, {'videoId': 2, 'value': 'hello'}])

# keep only data that doesn't exist in database
unique_data = mongodb.get_unique_rows( rows, unique_attributes=['videoId'] )


# you can even work norammly with the collection
data = list(mongodb.db.find({}))
```