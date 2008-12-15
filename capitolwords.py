""" Python library for interacting with Capitol Words API.

    The Capitol Words API (http://www.capitolwords.org/api/) provides access to
    the most commonly used words in Congressional Record each day.
"""

__author__ = "James Turk (jturk@sunlightfoundation.com)"
__version__ = "0.2.0"
__copyright__ = "Copyright (c) 2008 Sunlight Labs"
__license__ = "BSD"

import urllib2
try:
    import json
except ImportError:
    import simplejson as json

class CwodApiError(Exception):
    """ Exception for Capitol Words API errors """

class WordResult(object):
    def __init__(self, d):
        self.__dict__ = d
        
    def __str__(self):
        return '%s said %s times on %s' % (self.word, self.word_count, self.word_date)

def _get_json(url):
    try:
        response = urllib2.urlopen(url).read()
        return json.loads(response)
    except urllib2.HTTPError, e:
        raise CwodApiError('Invalid Request')
    except ValueError, e:
        raise CwodApiError('Invalid Response')

def dailysum(word, year, month=None, day=None,
             endyear=None, endmonth=None, endday=None):
    
    # can't specify only part of the range
    if ((endyear or endmonth or endday)
        and not (endyear and endmonth and endday)):
        raise CwodApiError('Invalid number of parameters')

    # join all supplied params together with /s
    params =  (word, year, month, day, endyear, endmonth, endday)
    paramstr = '/'.join([str(p) for p in params if p])
    
    # get json
    url = 'http://capitolwords.org/api/word/%s/feed.json' % paramstr
    result = _get_json(url)
    return [WordResult(r) for r in result]

def wordofday(year=None, month=None, day=None,
              endyear=None, endmonth=None, endday=None, maxrows=1):
    
    # can't specify only part of the range
    if ((endyear or endmonth or endday)
        and not (endyear and endmonth and endday)):
        raise CwodApiError('Invalid number of parameters')

    # join all supplied params together with /s
    params =  (year, month, day, endyear, endmonth, endday)
    paramstr = '/'.join([str(p) for p in params if p])
    
    if not paramstr:
        paramstr = 'latest'
    url = 'http://capitolwords.org/api/wod/%s/top%s.json' % (paramstr,
                                                             maxrows)
    result = _get_json(url)
    return [WordResult(r) for r in result]
