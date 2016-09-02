# -*- encoding: utf-8 -*-

from modules import *
from ShodanClass import ShodanObject
from MongodbClass import ConnectionMongodb
from MongodbClass import ConnectionMlap

data_file = "data/mongodb_list.json"

if __name__ == "__main__":
    archive = open_shodan_file(data_file)
    for line in archive:
        s = ShodanObject()
        # Convert the JSON into a native Python object
        banner = simplejson.loads(line)
        # --------------------------------------------
        s.banner_extractor(banner)
        c = ConnectionMongodb(s.ip_str, s.port)
        test = False
        data_system = {}
        test, data_system = c.test_connection()
        s.data_system = data_system
        if test:
            s.collections = c.get_collections()
            mlab = ConnectionMlap()
            mlab.insert_doc(s.create_dict())
            del mlab
        del c, s
    archive.close()
