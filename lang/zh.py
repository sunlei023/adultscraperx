text = {
    'name': 'adultscraperx',
    'tittle': 'AdultScraperX',
    'content': "##### 适用于Gsetant平台的AdultScraperX 成人电影元数据搜刮，可实现日本步兵，骑兵，动漫，欧美等多种资源的匹配与元数据获取。Gsetant中可在管理员插件管理页面通过本项目地址进行自动安装 https://github.com/gsetant/adultscraperx\n### 对本地文件的存储要求和服务配置\n##### 由于多种影片之间存在番号冲突的现象，所以本插件要求日本步兵，日本骑兵，日本动漫，欧美资源需要按照一定规则分开存储。具体规则如下\n##### 在Gsetant 服务端AdultScraperX 插件设置中设置目录标记:\n- 欧美与日本(骑兵、步兵、动漫)的目录标记可以在插件中自定义配置:\n- 配置主目录标记，必须含有(前、后)特殊字符如：-M- 、\*M\*、=M=以此类推\n- 目录标记只可出现一次，并且与主目录文件夹名的标记一致才可识别\n##### 本地主目录配置标记举例：\n- 修改你的本地文件夹为如下：\n- volume1/有码=M=/（无数个子目录）/（无数个文件）.mp4\n- volume1/无码=NM=/（无数个子目录）/（无数个文件）.mp4\n- volume1/动漫=A=/（无数个子目录）/（无数个文件）.mp4\n- volume1/欧美=E=/（无数个子目录）/（无数个文件）.mp4",
    'japan_censored_directory_mark': '日本-有码目录标记',
    'japan_uncensored_directory_mark': '日本-无码目录标记',
    'japan_animation_directory_mark': '日本-动漫目录标记',
    'europe_directory_mark': '欧美-目录标记',
    'japan_title_style':'日本标题样式',
}
