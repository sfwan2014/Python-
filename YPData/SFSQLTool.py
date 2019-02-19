#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb


class SQLTool:
    def __init__(self):
        self.db_url = "localhost"
        self.db_user = "root"
        self.db_pwd = "root"
        self.db_dbname = "PyDB"
        self.charset = 'utf8'

        self.db = self.connect()

    def connect(self):
        db = MySQLdb.connect(self.db_url, self.db_user, self.db_pwd, self.db_dbname, charset=self.charset)

        return db

    def close(self):
        self.db.close()

    # 创建表
    def createtable(self, sql):
        self.excute(sql)

    def add(self, sql):
        self.excute(sql)

    def fetch(self, sql):
        try:
            cursor = self.db.cursor()
            # 执行
            count = cursor.execute(sql)
            print count
            # 获取所有记录列表
            results = cursor.fetchmany(count)
            return results

        except:
            print "Error: unable to fetch data sql: %s" % sql
            return -1

    def fetchCount(self, sql):
        try:
            cursor = self.db.cursor()
            # 执行
            count = cursor.execute(sql)
            return count
        except:
            print "Error: unable to fetch data sql: %s" % sql
            return -1

    def excute(self, sql):
        try:
            self.db.cursor().execute(sql)
            self.db.commit()
        except:
            print "excute error sql: %s" % sql
            self.db.rollback()


