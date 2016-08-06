# -*- encoding: utf-8 -*-

import simplejson
import collections
import operator
import gzip
import sys


def humanize_bytes(bytes, precision=1):
    """
    From Complete Guide to Shodan
    Return a humanized string representation of a number of bytes.
    """
    abbrevs = (
        (1 << 50L, 'PB'),
        (1 << 40L, 'TB'),
        (1 << 30L, 'GB'),
        (1 << 20L, 'MB'),
        (1 << 10L, 'kB'),
        (1, 'bytes')
    )
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)


def open_shodan_file(filename):
    """Open file of the provided Shodan output file."""
    try:
        if filename.endswith('.gz'):
            file_in = gzip.open(filename, 'r')
            return file_in
        else:
            file_in = open(filename, 'r')
            return file_in
    except Exception, e:
        print "Error: %s" % e
        sys.exit(1)


def dicct(*argv, **kwargv):
    return kwargv
