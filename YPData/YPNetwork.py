# -*- coding: UTF-8 -*-

import urllib2
import urllib


class YPNetwork:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Referer": "https://www.coursera.org/learn/wharton-customer-analytics/lecture/1OcWO/descriptive-data-collection-net-promoter-score-and-self-reports",
            "Host": "www.coursera.org",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest"}

    def getHTMLData(self):
        os = open('test.html', 'r')
        res = os.read().decode('utf-8')
        return res

    def getRequestData(self, url):
        print url

        request = urllib2.Request(url)
        try:
            response = urllib2.urlopen(request)
            res = response.read().decode('utf-8')
        except urllib2.HTTPError, e:
            if hasattr(e, 'reason'):
                print e.reason
            if hasattr(e, 'code'):
                print e.code
            res = -1
        finally:
            return res