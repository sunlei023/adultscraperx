# -*- coding: utf-8 -*-

import re
import sys

from app.core.model.meta_data import MetaData
from app.plugins.adultscraperx.spider.uncensored_spider import UnsensoredSpider

if sys.version.find('2', 0, 1) == 0:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
else:
    from io import StringIO
    from io import BytesIO

from PIL import Image


class Fc2Club(UnsensoredSpider):
    basicUrl = 'fc2club.com'

    def __init__(self):
        super().__init__()
        self.checkUrl = 'fc2club.com'

    def search(self, q):
        """
        执行查询函数
        :param q:
        :return:
        """
        item = []
        '获取查询结果页html对象'
        url = 'https://%s/html/%s.html' % (self.basicUrl, q)
        html_item = self.get_html_byurl(url)
        if html_item['issuccess']:
            media_item = self.analysisMediaHtmlByxpath(
                html_item['html'], q)
            item.append( media_item)
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

        xpath_title = "/html/body/div[2]/div/div[1]/h3"
        title = html.xpath(xpath_title)[0].text
        media.title = title

        summary = title
        media.summary = summary

        xpath_poster_url = "//*[@id='slider']/ul[1]/li[1]/img"
        poster_url = 'https://' + self.basicUrl + html.xpath(xpath_poster_url)[0].attrib['src']
        media.poster = poster_url
        media.thumbnail = poster_url

        studio = 'FC2'
        media.studio = studio

        directors = ''
        media.directors = directors

        xpath_collections = "/html/body/div[2]/div/div[1]/h5[3]/a[1]"
        collections = html.xpath(xpath_collections)[0].text
        media.collections = collections

        year = ''
        media.year = year
        media.originally_available_at = year

        xpath_category = "/html/body/div[2]/div/div[1]/h5[6]/a"
        categorys = html.xpath(xpath_category)
        category_list = []
        for category in categorys:
            category_list.append(self.tools.cleanstr(category.text))
        categorys = ','.join(category_list)
        if len(categorys) > 0:
            media.category = categorys

        xpath_actor_name = "/html/body/div[2]/div/div[1]/h5[5]/a"
        actor_name = html.xpath(xpath_actor_name)[0].text
        if actor_name != '':
            media.actor = actor_name

        return media
