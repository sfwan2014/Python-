#!/usr/bin/python
# -*- coding: UTF-8 -*-

from SFSQLTool import *
from YPNetwork import *
from YPParse import *


class YPData:

    TABLE_NAME = 'BUY_ORDER'

    def __init__(self):

        self.createTable()

    # 创建表
    def createTable(self):
        db = SQLTool()
        sql = "CREATE TABLE %s ( \
                NAME CHAR(20) NOT NULL, \
                PHONE CHAR(28), \
                STATUS CHAR(16), \
                TIME CHAR(40), PRIMARY KEY (`TIME`,`PHONE`) )" % YPData.TABLE_NAME
        print sql
        db.createtable(sql)
        db.close()

    def dropTable(self):
        db = SQLTool()
        sql = 'DROP TABLE IF EXISTS %s' % YPData.TABLE_NAME
        db.excute(sql)
        db.close()

    def query(self):
        db = SQLTool()
        sql = 'select * from %s' % YPData.TABLE_NAME
        results = db.fetch(sql)
        if results != -1:
            for row in results:
                name = row[0]
                phone = row[1]
                status = row[2]
                time = row[3]
                print "name=%s,phone=%s,status=%s,time=%s" % \
                      (name, phone, status, time)

        db.close()

    def parse(self, res):
        parse = YPParse()
        userList = parse.parse(res)
        return userList

    def insertDB(self, userList):
        db = SQLTool()
        for p in userList:
            name = p.name;
            phone = p.phone;
            orderstatus = p.orderstatus
            ordertime = p.ordertime
            sql = "INSERT INTO %s (NAME, \
                    PHONE, STATUS, TIME)  \
                    VALUES('%s', '%s', '%s', '%s')" % \
                  (YPData.TABLE_NAME, name, phone, orderstatus, ordertime)
            db.add(sql)

        db.close()


    def getData(self, url):
        net = YPNetwork()
        res = net.getRequestData(url)
        # res = net.getHTMLData()
        return res


    def getSpiderCount(self):
        db = SQLTool()
        sql = 'select * from %s' % YPData.TABLE_NAME
        count = db.fetchCount(sql)
        db.close()
        return count


# spider = YPData()
# spider.start()
# spider.query()
# spider.dropTable()