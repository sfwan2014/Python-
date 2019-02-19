#!/usr/bin/python
# -*- coding: UTF-8 -*-

from YPData import *
import time

class Spider:

    def __init__(self):
        self.curpage = 0
        self.basicUrl = "https://api3.jiumiaodai.com/vip/index?vip%2Findex=&ticket=S3tLO5Pi%2FP3%2B5cl2f6Euq137C3O1OLES%2BZ0vCNp%2FZP5u41UXLC6y%2BIhZ3p1fMm1f0BiNKNQp3fJ2wdujMXvoWxJSRgO78yTo9wq5DazPKLHUVRRZokoH75nFx53fl50RfqRikseow8e9X4PFI0%2B%2F3RtYotmaoScmMgmADg870F8f%2Fqj4Uy8OKQ%2FFrHwzpjsKg6Bn6PJ9PY7SNlHkATcGvv0I2kGA%2BntxhdBWVQaYTL%2FfmmH2k7dd3yujDA1gWRxi&page="
        self.dataHandle = YPData()
        self.pagesize = 20  # 每页的数据条数
        self.totalpage = 12079  # 总的页数

    # 启动
    def start(self):

        count = self.dataHandle.getSpiderCount()
        handlePage = count / self.pagesize  # 已经处理的页数

        # print handlePage

        totalPage = self.totalpage

        for i in range(0, totalPage):
            print i
            page = totalPage - i - handlePage
            if page < 0:
                return



            url = self.basicUrl + "%s" % page
            res = self.dataHandle.getData(url)

            if res == -1:
                # 等待 模拟手动流量网页速度
                self.wait()
                continue
            # 解析数据
            userList = self.dataHandle.parse(res)
            # 存入数据库
            self.dataHandle.insertDB(userList)
            # 等待 模拟手动流量网页速度
            self.wait()

    def wait(self):
        time.sleep(50)    # 50秒，频次低

spider = Spider()
spider.start()

# spider.dataHandle.dropTable()