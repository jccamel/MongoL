# -*- encoding: utf-8 -*-

from ShodanClass import ShodanObject

if __name__ == "__main__":
    data_file = "data/mongodb_list.json"
    s = ShodanObject(data_file)
    s.print_data_banner()
