# -*- coding: utf-8 -*-

import re
import sys

from app.core.model.meta_data import MetaData
from app.plugins.adultscraperx.spider.caribbean import Caribbean

if sys.version.find('2', 0, 1) == 0:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
else:
    from io import StringIO
    from io import BytesIO

from PIL import Image

class Caribbeancompr(Caribbean):

    basicUrl = 'www.caribbeancompr.com'

    def __init__(self):
        super().__init__()
        self.checkUrl = 'https://www.caribbeancompr.com/'


    def search(self, q):

        '''
        执行查询函数
        '''
        item = []
        '获取查询结果页html对象'
        url = 'https://%s/moviepages/%s/index.html' % (self.basicUrl, q)
        html_item = self.get_html_byurl(url)
        if html_item['issuccess']:
            media_item = self.analysisMediaHtmlByxpath(
                html_item['html'], q)
            item.append(media_item)
        else:
            pass

        return item

    def analysisMediaHtmlByxpath(self, html, q):
        """
        根据html对象与xpath解析数据
        html:<object>
        html_xpath_dict:<dict>
        return:<dict{issuccess,ex,dict}>
        """
        media = MetaData()
        number = self.tools.cleanstr(q.upper())
        media.number = number
        media.web = 'caribbeancompr'

        xpath_title = "//*[@id='moviepages']/div/div[2]/div[1]/div/div[2]/h1"
        title = html.xpath(xpath_title)[0].text
        # if len(title) > 0:
        #     title = self.tools.cleantitlenumber(
        #         self.tools.cleanstr(title[0]), number)
        media.title = title

        xpath_summary = "//*[@id='moviepages']/div/div[2]/div[1]/div/p"
        summary = html.xpath(xpath_summary)[0].text
        media.summary = summary

        media.poster = 'https://%s/moviepages/%s/images/l_l.jpg' % (self.basicUrl, number)
        media.thumbnail = 'https://%s/moviepages/%s/images/l_l.jpg' % (self.basicUrl, number)


        studio = 'Caribbeancompr'
        media.studio = studio

        directors = ''
        media.directors = directors

        collections = 'Caribbeancompr'
        media.collections = collections

        xpath_year = "//li[@class='movie-spec'][2]/span[@class='spec-content']/text()"
        year = html.xpath(xpath_year)
        if len(year) > 0:
            year = self.tools.cleanstr(year[0])
            media.year = year
            media.originally_available_at = year

        xpath_category = "//li[@class='movie-spec'][5]/span[@class='spec-content']/a/text()"
        categorys = html.xpath(xpath_category)
        category_list = []
        for category in categorys:
            category_list.append(self.tools.cleanstr(category))
        categorys = ','.join(category_list)
        if len(categorys) > 0:
            media.category = categorys


        actor = {}
        xpath_actor_name = "//li[@class='movie-spec'][1]/span[@class='spec-content']/a"
        actor_name = html.xpath(xpath_actor_name)
        if len(actor_name) > 0:
            for i, actorname in enumerate(actor_name):
                actor.update({actorname.text: ''})

            media.actor = actor
            
        return media
        
    def artPicture(self, url, r, w, h):
        cropped = None
        try:
            response = self.client_session.get(url)
        except Exception as ex:
            print('error : %s' % repr(ex))
            return cropped

        img = Image.open(BytesIO(response.content))
        cropped = img.crop((0, 0, img.size[0], img.size[1]))
        return cropped
