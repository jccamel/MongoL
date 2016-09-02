# -*- encoding: utf-8 -*-
from modules import *


class Diccionario(object):
    def __init__(self, clave):
        self.clav = clave
        self.dicc = {}

    def __del__(self):
        pass

    def dicc_extractor(self, valor):
        i = 1
        for v in valor:
            c = str(self.clav) + str(i)
            self.dicc.setdefault(c, str(v))
            i += 1
        return self.dicc


class Localitz(object):
    def __init__(self):
        self.city = ""
        self.longitude = 0
        self.latitude = 0
        self.country_code = ""
        self.country_name = ""

    def location_extractor(self, loc):
        """
        Se da la posibilidad que hay city=None
        Resolver mediante geolocalizacion
        """
        for key, value in loc.iteritems():
            if key == "city":
                self.city = value
            elif key == "longitude":
                self.longitude = value
            elif key == "latitude":
                self.latitude = value
            elif key == "country_code":
                self.country_code = value
            elif key == "country_name":
                self.country_name = value
            else:
                pass

        dicc = dicct(city=self.city, longitude=self.longitude,
                     latitude=self.latitude, country_code=self.country_code,
                     country_name=self.country_name)
        return dicc

    def __del__(self):
        pass


class ShodanObject(object):
    def __init__(self):
        self.product = ""
        self.hash = ""
        self.version = ""
        self.ip = 0
        self.isp = ""
        self.os = ""
        self.shodan_dic = {}
        self.hostnames = {}
        self.location = {}
        self.timestamp = ""
        self.domains = {}
        self.org = ""
        self.port = 0
        self.transport = ""
        self.ip_str = ""
        self.mongoinfo = {}  # Collections by Shodan info
        self.collections = {}  # Collections after connect and ask
        self.data_system = {}

    def __del__(self):
        pass

    def banner_extractor(self, banner):
        for key, value in banner.iteritems():
            if key == "product":
                self.product = value
            elif key == "hash":
                self.hash = value
            elif key == "version":
                self.version = value
            elif key == "ip":
                self.ip_str = value
            elif key == "isp":
                self.isp = value
            elif key == "os":
                self.os = value
            elif key == "_shodan":
                self.shodan_dic = value
            elif key == "hostnames":
                if len(value) != 0:
                    h = Diccionario('host')
                    self.hostnames = h.dicc_extractor(value)
                    del h
                else:
                    self.hostnames = {}
            elif key == "location":
                if value is None:
                    self.location = {}
                else:
                    l = Localitz()
                    self.location = (l.location_extractor(value))
                    del l
            elif key == "timestamp":
                self.timestamp = value
            elif key == "domains":
                if len(value) != 0:
                    d = Diccionario('domain')
                    self.domains = d.dicc_extractor(value)
                    del d
                else:
                    self.domains = {}
            elif key == "org":
                self.org = value
            elif key == "port":
                self.port = value
            elif key == "transport":
                self.transport = value
            elif key == "ip_str":
                self.ip_str = value
            elif key == 'data':
                try:
                    data = banner['data'].replace('MongoDB Server Information\n', '').split('\n},\n')[2]
                    self.mongoinfo = simplejson.loads(data + '}')
                except:
                    pass
            else:
                pass

    def print_object(self):
        print 'Product:' + '\t' + self.product
        print 'Hash:' + '\t' + str(self.hash)
        print 'Version:' + '\t' + self.version
        print 'ip:' + '\t' + str(self.ip)
        print 'ISP:' + '\t' + self.isp
        print 'OS:' + '\t' + str(self.os)
        print 'Shodan dicctionary:' + '\t' + str(self.shodan_dic)
        print 'Host Names:' + '\t' + str(self.hostnames)
        print 'Location:' + '\t' + str(self.location)
        print 'Time:' + '\t' + self.timestamp
        print 'Domains:' + '\t' + str(self.domains)
        print 'Org.:' + '\t' + self.org
        print 'Port:' + '\t' + str(self.port)
        print 'Transport:' + '\t' + self.transport
        print 'IP:' + '\t' + self.ip_str
        print 'Mongo Info.:' + '\t' + str(self.mongoinfo)
        print 'Mongo Data System:', "\t", self.data_system
        print 'Collections:', "\t", self.collections
        print "--------------------------------------------------------------------"

    def create_dict(self):
        dict = dicct(producto=self.product, version=self.version,
                     isp=self.isp, os=self.os, hostnames=self.hostnames, location=self.location,
                     timestamp=self.timestamp, domains=self.domains,
                     org=self.org, port=str(self.port), ip=str(self.ip_str),
                     mongoinfo=self.mongoinfo, data_system=self.data_system,
                     collections=self.collections)
        return dict
