#!/usr/bin/python
#coding=utf-8

__author__ = 'yaozizhenjun'

import urllib
import urllib2
import re
import thread
import time

#糗事百科爬虫
class QSBK(object):
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        #存放段子的变量,每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
    #传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'链接糗事百科失败,错误原因:' ,e.reason
                return None
    #传入某页代码,返回本业不带有图片的段子列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print '页面加载失败......'
            return None
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class.*?">(.*?)</div>.*?'+
            '<div class="content">.*?<span>(.*?)</span>.*?</div>(.*?)<div class="stats">.*?<i class="number">(.*?)</i>.*?</span>', re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            #是否含有图片
            havingImg = re.search('img',item[3])
            #如果不含图片,加入到list中
            if not havingImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,'\n',item[2])
                #item[0]是发布者,item[1]是发布者年龄,item[2]是段子内容,item[4]是点赞数
                pageStories.append([item[0].strip(),item[1].strip(),text.strip(),item[4].strip()])
        return pageStories
    #加载并提取页面内容,加入带列表中
    def loadPage(self):
        #如果当前未看页数少于2页,则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                #获取新的一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放在全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1
    #调用该方法每次敲击回车打印出一个段子
    def getOneStory(self,pageStories,page):
        #遍历一页的段子
        for story in pageStories:
            #等待用户输入
            input = raw_input()
            #每当输入回车一次,判断一下是否需要加载新页面
            self.loadPage()
            #如果输入Q,则程序结束
            if input == 'Q':
                self.enable = False
                return
            print u'第%d页\t发布人:%s\t发布人年龄:%s\t赞:%s\n%s' %(page,story[0],story[1],story[3],story[2])
    #开始方法
    def start(self):
        print u'正在读取糗事百科,按回车键看新段子,Q退出'
        #使变量为True,程序可以正常运行
        self.enable = True
        #局部变量,控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                #从全局list中获取一页的段子
                pageStories = self.stories[0]
                #当前读到的页数加一
                nowPage += 1
                #将全局list中第一个元素删除,因为已经取出
                del self.stories[0]
                #输出该页的段子
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()




