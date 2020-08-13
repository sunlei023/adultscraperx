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

class Caribbean(UnsensoredSpider):

    basicUrl = 'www.caribbeancom.com'

    def __init__(self):
        super().__init__()
        self.checkUrl = 'www.caribbeancom.com'

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
            pass  # print repr(html_item['ex'])

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
        media.web = 'caribbean'


        xpath_title = "//*[@id='moviepages']/div/div[1]/div[1]/div[2]/h1"
        title = html.xpath(xpath_title)[0].text

        media.title = title

        xpath_summary = "//*[@id='moviepages']/div/div[1]/div[1]/p"
        summary = html.xpath(xpath_summary)[0].text

        media.summary = summary

        media.poster = 'https://%s/moviepages/%s/images/l_l.jpg' % (self.basicUrl, number)
        media.thumbnail = 'https://%s/moviepages/%s/images/l_l.jpg' % (self.basicUrl, number)

        studio = 'Caribbeancom'
        media.studio = studio

        directors = ''
        media.directors = directors

        collections = 'Caribbeancom'
        media.collections = collections

        xpath_year = "//*[@id='moviepages']/div/div[1]/div[1]/ul/li[2]/span[2]"
        year = html.xpath(xpath_year)[0].text
        media.year = year
        media.originally_available_at = year

        xpath_category = "//*[@id='moviepages']/div/div[1]/div[1]/ul/li[4]/span[2]/a"
        categorys = html.xpath(xpath_category)
        category_list = []
        for category in categorys:
            category_list.append(self.tools.cleanstr(category.text))
        categorys = ','.join(category_list)
        if len(categorys) > 0:
            media.category = categorys


        xpath_actor_name = "//*[@id='moviepages']/div/div[1]/div[1]/ul/li[1]/span[2]/a/span"
        actor_name = html.xpath(xpath_actor_name)
        actor_dict = {}
        for actor in actor_name:
            actor_dict[actor.text] = 'https://images.d2pass.com/images/d2p_toolbar/images/d2p_logo.png'
        media.actor = actor_dict
        return media

        
    def actorPicture(self, url, r, w, h):
        cropped = None
        try:
            response = self.client_session.get(url)
        except Exception as ex:
            print('error : %s' % repr(ex))
            return cropped

        try:
            img = Image.open(BytesIO(response.content))
        except Exception as ex:
            return cropped

        rimg = img.resize((125, 125), Image.ANTIALIAS)
        # (left, upper, right, lower)
        cropped = rimg.crop((0 , 0, 125, 125))
        return cropped


