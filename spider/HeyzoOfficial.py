# -*- coding: utf-8 -*-
from app.core.model.meta_data import MetaData
from app.plugins.adultscraperx.spider.uncensored_spider import UnsensoredSpider
import sys
if sys.version.find('2', 0, 1) == 0:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
else:
    from io import StringIO
    from io import BytesIO


class HeyzoOfficial(UnsensoredSpider):

    def __init__(self):
        super().__init__()
        self.checkUrl = 'https://www.heyzo.com/'


    def search(self, q):
        '''
        执行查询函数
        '''
        item = []
        queryKeyword = q.replace('heyzo-', '')

        '获取查询结果列表页html对象'
        url = 'https://www.heyzo.com/moviepages/%s/index.html' % queryKeyword

        html_item = self.get_html_byurl(url)
        if html_item['issuccess']:
            media_item = self.analysis_media_html_byxpath(
                html_item['html'], queryKeyword)
            item.append(media_item)
        else:
            pass  # print repr(html_item['ex'])

        return item

    def analysis_media_html_byxpath(self, html, q):
        """
        根据html对象与xpath解析数据
        html:<object>
        html_xpath_dict:<dict>
        return:<dict{issuccess,ex,dict}>
        """

        '''
        xpath_number = "//div[@class='col-md-3 info']/p[1]/span[2]/text()"
        number = html.xpath(xpath_number)
        if len(number) > 0:
            number = self.tools.cleanstr(number[0])
            self.media.number = number
        '''
        media = MetaData()
        number =  'heyzo-%s' % self.tools.cleanstr(q.upper())
        media.number = number

        xpath_title = "//div[@id='wrapper']/article/section[1]/div[@id='movie']/h1/text()"
        title = html.xpath(xpath_title)
        if len(title) > 0:
            title = self.tools.cleantitlenumber(
                self.tools.cleanstr(title[0]), number)
            media.title = title

        xpath_summary = "//p[@class='memo']/text()"
        summary = html.xpath(xpath_summary)
        if len(summary) > 0:
            summary = summary[0]
            media.summary = summary

        media.poster = 'https://www.heyzo.com/contents/3000/%s/images/player_thumbnail.jpg' % q
        media.thumbnail = media.poster

        media.studio = 'Heyzo'

        xpath_collections = "//tr[@class='table-series']/td[2]/text()"
        collections = html.xpath(xpath_collections)
        if len(collections) > 0:
            collections = self.tools.cleanstr(collections[0])
            if not collections == '-----':
                media.collections = collections

        xpath_year = "//tr[@class='table-release-day']/td[2]/text()"
        year = html.xpath(xpath_year)
        if len(year) > 0:
            year = self.tools.cleanstr(year[0])
            media.year = year
            media.originally_available_at = year

        xpath_category = "//ul[@class='tag-keyword-list']/li/a/text()"
        categorys = html.xpath(xpath_category)
        category_list = []
        for category in categorys:
            category_list.append(self.tools.cleanstr(category))
        categorys = ','.join(category_list)
        if len(categorys) > 0:
            media.category = categorys

        actor = {}
        xpath_actor_name = "//tr[@class='table-actor']/td//a/span/text()"
        #xpath_actor_url = "//tr[@class='table-actor']/td//a/@href"
        actor_name = html.xpath(xpath_actor_name)
        #actor_url = html.xpath(xpath_actor_url)
        if len(actor_name) > 0:
            for i, actorname in enumerate(actor_name):
                # if actor_url[i].find('nowprinting') > 0:
                #     actor.update({actorname: ''})
                # else:
                actor.update({actorname: ''})
            media.actor = actor

        return media
