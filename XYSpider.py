# -*- coding: UTF-8 -*-

import urllib2

from lxml import etree
import re
import os
import sys
import time

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# url = 'http://www.baidu.com'
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# res = response.read().decode('utf-8')
# # print res;
# tree = etree.HTML(res)
# nodes = tree.xpath(u"dic[@id='detailbody']/h1")


class XYSpider:
    def __init__(self):
        self.hostURL = "http://www.xingyun.cn"
        self.pageSubPath = "/elites/"
        self.page = 1

    def getHomeUrl(self):
        return self.hostURL+self.pageSubPath+str(1)

    def getPageUrl(self, page):
        return self.hostURL+self.pageSubPath+str(page)

# xingyuShow_getDynamicListByScrollLoad.action?curPage=1&dynamicLoadIndex=2&showType=0&userid=200500894596
    def getDetailUrl(self, userId, curPage, dynamicLoadIndex):
        url = self.hostURL + "/xingyuShow_getDynamicListByScrollLoad.action?"+ "showType=0" \
              + "&userid="+userId + "&curPage="+str(curPage) + "&dynamicLoadIndex="+str(1)
        return url

    # 获取某页数据
    def getPage(self, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    # 获取首页数据
    def getHomePage(self, page):
        url = self.getPageUrl(page)
        print url
        return self.getPage(url)

    # 获取详情动态页面
    def getDetailPage(self, userId, curPage, dynamicLoadIndex):
        url = self.getDetailUrl(userId, curPage, dynamicLoadIndex)
        print url
        return self.getPage(url)

    # 获取userid列表
    def getUserId(self, pageData):
        # 创建xpath解析对象
        selector = etree.HTML(pageData)
        # 获取用户 id  u/xxxxxxx
        links = selector.xpath('//div[@class="userDetailsList2"]/div[@class="userDetails_box2"]/div[@class="model_user_icon_wrap"]/a/@href')
        userIdList = []
        for link in links:
            # 去除 /
            removeF = re.compile('/', re.S)
            # 去除 u
            removeU = re.compile('u', re.S)
            link = re.sub(removeF, "", link)
            link = re.sub(removeU, "", link)
            userIdList.append(link)
        return userIdList

    def getImageList(self, pageData):
        selector = etree.HTML(pageData)
        links = selector.xpath('//div[@class="div_trends"]/div[@class="trends"]/div[@class="trends_cont"]/div/div[@class="cont_wrap"]/div[@class="imgCont "]/ul/li/input/@src_url')
        return links;

    def getUserName(self, pageData):
        selector = etree.HTML(pageData)
        links = selector.xpath('//div[@class="trends_cont"]/div[@class="details"]/p/a/text()')
        if len(links) > 0:
            return links[0]
        return ""

    # 保存的根目录
    def getHomeDirectory(self):
        cwd = os.getcwd()
        dir = cwd + '/images'
        self.createDirector(dir)
        return dir

    # 保存路径
    def getSaveDirectory(self, name):
        dir = self.getHomeDirectory()
        path = dir + "/" + name
        self.createDirector(path)
        return path

    # 创建文件夹
    def createDirector(self, dir):
        if not(os.path.exists(dir)):
            os.mkdir(dir)

    def getSavePath(self, imgName, userName):
        dir = self.getSaveDirectory(userName)
        path = dir + "/" + imgName + ".jpg"
        return path

    def saveImage(self, imgName, userName, imgData):
        path = self.getSavePath(imgName, userName)
        fo = open(path, "wb")
        fo.write(imgData)
        fo.close()

    def getImageData(self, link):
        return urllib2.urlopen(link).read()


    def start(self):
        print "开始"
        result = self.getHomePage(1)
        userList = self.getUserId(result);
        # print userList;
        index = 0
        for userId in userList:
            #if index > 10: # 数据太多,怕被封ip
            #    break

            result = self.getDetailPage(userId, 1, 1)
            userName = self.getUserName(result)
            if len(userName) == 0:
                continue
            msg = "获取"+userName+"图片"
            print msg
            imageLinks = self.getImageList(result)
            count = 0
	    maxCount = len(imageLinks)
            for link in imageLinks:
                image = self.getImageData(link)
                time.sleep(0.05)
                self.saveImage(str(1000+count), userName, image)
                count+=1
		per = count/(maxCount*1.0)
		print "%s%%..." % str(per*100)
            # print result
            index += 1

        print "结束"




spider = XYSpider()
spider.start()
