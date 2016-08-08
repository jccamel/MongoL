# -*- encoding: utf-8 -*-

import pymongo


class ConectionMongodb(object):
    def __init__(self):
        self.MONGODB_URI = ""
        self.db = ""
        self.client = ""
        self.colection = ""

    def __del__(self):
        pass

    def open_conection(self):
        self.client = pymongo.MongoClient(self.MONGODB_URI)
        self.db = self.client.get_default_database()

    def close_conection(self):
        self.client.close()
