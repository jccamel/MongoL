# -*- encoding: utf-8 -*-

from modules import *
from ShodanClass import ShodanObject

data_file = "data/mongodb_list.json"

if __name__ == "__main__":
    archive = open_shodan_file(data_file)
    for line in archive:
        s = ShodanObject()
        # Convert the JSON into a native Python object
        banner = simplejson.loads(line)
        # --------------------------------------------
        s.banner_extractor(banner)
        print s.print_object()
        del s
    archive.close()
