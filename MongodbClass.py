# -*- encoding: utf-8 -*-

import pymongo


class ConnectionMongodb(object):
    def __init__(self, server, port):
        self.MONGODB_URI = "mongodb://" + server + ":" + str(port)
        self.mongol_URI = ''
        self.client = pymongo.MongoClient(self.MONGODB_URI, serverSelectionTimeoutMS=1000, maxPoolSize=50)

    def __del__(self):
        pass

    def test_connection(self):
        data_system = {}
        try:
            data_system = self.client.server_info()
            print self.MONGODB_URI + "\t" + "Connection OK"
            return True, data_system
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print self.MONGODB_URI + "\t" + str(err)
            return False, data_system

    def get_collections(self):
        d = {}
        try:
            d = dict((db, [collection for collection in self.client[db].collection_names()])
                     for db in self.client.database_names())
            return d
        except pymongo.errors.OperationFailure as err:
            print self.MONGODB_URI + "\t" + str(err)
            return d
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print self.MONGODB_URI + "\t" + str(err)
            return d


class ConnectionMlap(object):
    def __init__(self):
        self.mongol_URI = ''  # write here your MongoDB URI from mLab
        self.client = ""
        self.db = ""

    def __del__(self):
        pass

    def __open_conexion__(self):
        try:
            self.client = pymongo.MongoClient(self.mongol_URI)
            self.db = self.client.get_default_database()
        except:
            print "Connection error"

    def __close_conexion__(self):
        self.client.close()

    def insert_doc(self, doc, coleccion='mongol'):
        self.__open_conexion__()
        try:
            colecc = self.db[coleccion]
            colecc.insert(doc)
            print(" **********  Document Saved  *************")
            self.__close_conexion__()
        except:
            print(" **********  Document not Saved  *************")
            self.__close_conexion__()
