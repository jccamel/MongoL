# -*- encoding: utf-8 -*-

import shodan
import sys

shodankey = ""


def initialize(shodankey):
    try:
        shodanapi = shodan.Shodan(shodankey)
        info = shodanapi.info()
        return shodanapi
    except shodan.APIError, e:
        print 'Error: %s' % e
        sys.exit(1)

# String search:
# port:27017 country:"" city:"" org:"" product:"MongoDB"


def search(api, string):

    try:
        result = api.search(string)
        # Loop through the matches and print each IP
        for service in result['matches']:
            print service['ip_str']
    except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)


if __name__ == "__main__":
    api = initialize(shodankey)
    search(api, "port:27017")
