# -*- encoding: utf-8 -*-

import shodan
import collections
import operator
import simplejson
import shodan.helpers as helpers
from modules import humanize_bytes


class ShodanObject(object):
    def __init__(self, data_file):
        self.data_file = data_file
        self.product = ""
        self.hash = ""
        self.version = ""
        self.ip = 0
        self.isp = ""
        self.os = ""
        self.shodan = {}
        self.hostnames = []
        self.location = {}
        self.timestamp = ""
        self.domains = []
        self.org = ""
        self.data = ""
        self.port = 0
        self.transport = ""
        self.ip_str = ""
        self.total_data = 0
        self.databases = collections.defaultdict(int)

    def print_data_banner(self):
        counter = 0
        for banner in helpers.iterate_files(self.data_file):
            for key, value in banner.iteritems():
                if key == "product":
                    self.product = value
                if key == "hash":
                    self.hash = value
                if key == "version":
                    self.version = value
                if key == "ip_str":
                    self.ip_str = value
            counter += 1
            print str(counter) + "\t" + self.product + "\t" + self.version + "\t" + self.ip_str

    def totals_top10(self):

        for banner in helpers.iterate_files(self.data_file):
            try:
                data = banner['data'].replace('MongoDB Server Information\n', '').split('\n},\n')[2]
                data = simplejson.loads(data + '}')
                self.total_data += data['totalSize']
                for db in data['databases']:
                    self.databases[db['name']] += 1
            except Exception, e:
                print "Error: %s" % e
                pass

        print ('Total storage: {}'.format(humanize_bytes(self.total_data)))

        counter = 0

        for name, count in sorted(self.databases.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]:
            counter += 1
            print ('#{}\tdatabase name:{}\tappear:{}'.format(counter, name, count))
