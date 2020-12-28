import re

from app.plugins.adultscraperx import config
from app.plugins.adultscraperx.config import get_info
from app.plugins.adultscraperx.setting import spider_config
from app.tools.cache_tools import set_cache, check_cache
from app.tools.log_tools import log


def search(meta_info, user_setting):
    plugin_name = config.get_info('en').get('name')
    meta_data_list = []
    video_title = meta_info.get('video_title')
    part_file = meta_info.get('part_file')
    movie_type = ''
    title_style = ''
    log('info', 'title:%s' % video_title, plugin_name)

    if not user_setting.get('japan_title_style') == '':
        title_style = user_setting.get('japan_title_style')

    if user_setting.get('japan_censored_directory_mark') in part_file:
        movie_type = 'censored'
    elif user_setting.get('japan_uncensored_directory_mark') in part_file:
        movie_type = 'uncensored'
    elif user_setting.get('japan_animation_directory_mark') in part_file:
        movie_type = 'animation'
    elif user_setting.get('europe_directory_mark') in part_file:
        movie_type = 'europe'

    if movie_type != '' or not spider_config.SOURCE_LIST[movie_type]:
        for template in spider_config.SOURCE_LIST[movie_type]:
            # 循环模板列表
            code_list = []

            re_list = re.finditer(
                template['pattern'], video_title, re.IGNORECASE)
            for item in re_list:
                code_list.append(item.group())

            while '' in re_list:
                re_list.remove('')

            if len(code_list) == 0:
                continue
            # 对正则匹配结果进行搜索
            for code in code_list:
                web_list = template['web_list']
                code = template['formatter'].format(code)
                cache_data = check_cache(code, get_info('en').get('name'))
                if cache_data:
                    meta_data_list.extend(cache_data)
                else:
                    for webSiteClass in web_list:
                        web_site = webSiteClass()
                        items = web_site.search_with_img(code)
                        for item in items:
                            item['code'] = code
                            item['original_title'] = item['title']
                        meta_data_list.extend(items)
    # 标题样式设定
    for dict_item in meta_data_list:
        try:
            if title_style == 'number':
                dict_item['title'] = dict_item['number']
            elif title_style == 'numbertitle':
                dict_item['title'] = '%s  %s' % (
                    dict_item['number'], dict_item['original_title'])
        except Exception as ex:
            log('error', ex, plugin_name)
            continue

    return meta_data_list
