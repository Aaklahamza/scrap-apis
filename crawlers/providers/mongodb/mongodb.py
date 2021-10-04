import pymongo
from pymongo.errors import BulkWriteError


class MongoDb:

    def __init__(self,
                 database,
                 collection,
                 uri="mongodb://localhost:27017/"):
        self.db = pymongo.MongoClient(uri)[database][collection]

    # keep only entries which don't exist in the data
    def get_unique_rows(self, rows, unique_attributes=[]):
        if len(unique_attributes) == 0:
            return rows
        return list(filter(lambda row: self.db.count_documents({k: row[k] for k in unique_attributes}) == 0, rows))

    # inserting a list of documents
    # all documents will be attempted ( even if an error occurs )
    def insert_data(self,
                    docs):

        if len(docs) > 0:
            try:
                self.db.insert_many(docs, ordered=False)
            except BulkWriteError as bwe:
                print(bwe.details)
        return len(docs)
