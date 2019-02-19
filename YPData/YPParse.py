#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lxml import etree
import re
from Person import *

class YPParse:

    def parse(self, data):
        # 创建xpath解析对象
        selector = etree.HTML(data)

        links = selector.xpath("//table/tbody/tr")

        userList = []
        for tr in links:
            str = etree.tostring(tr)
            # print str
            html = etree.XML(str)
            # print html
            phones = html.xpath("//td[@data-col-seq='1']/text()")
            names = html.xpath("//td[@data-col-seq='3']/text()")
            orderstatuss = html.xpath("//td[@data-col-seq='7']/text()")
            paytimes = html.xpath("//td[@data-col-seq='8']/text()")

            phone = ''
            if len(phones) > 0:
                phone = phones[0]

            name = ''
            if len(names) > 0:
                name = names[0]

            status = ''
            if len(orderstatuss) > 0:
                status = orderstatuss[0]

            paytime = ''
            if len(paytimes) > 0:
                paytime = paytimes[0]

            user = Person(name, phone, status, paytime)
            userList.append(user)
            msg = "%s %s %s %s" % (phone, name, status, paytime)
            print msg

        return userList