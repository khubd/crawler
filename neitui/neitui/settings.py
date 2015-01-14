# -*- coding: utf-8 -*-

# Scrapy settings for neitui project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'neitui'

SPIDER_MODULES = ['neitui.spiders']
NEWSPIDER_MODULE = 'neitui.spiders'

ITEM_PIPELINES = {
    'neitui.pipelines.JsonWriterPipeline': 300,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'neitui (+http://www.yourdomain.com)'
HEADERS={
	        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip,deflate,sdch",
            "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "Host":"www.neitui.me",
            "Pragma":"no-cache",
            "Referer":"http://www.neitui.me/index.php",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",

}
COOKIES={
		    "saeut":"115.193.179.233.1411834522183034",
            "PHPSESSID":"cd96a95e58c3aff92357137b1259efcc",
            "__NEITUI_MESSAGE_LASTINFOS__":"0_0_1_0",
            "neitui_uid":"NDIxMTc=",
            "neitui_key":"da5ab825c6b765baddbcadc33e0f81ce",
            "Hm_lvt_21de977c0eb6fd0c491abddcb289ff96":"1419872485,1420096604",
            "Hm_lpvt_21de977c0eb6fd0c491abddcb289ff96":"1420385184",

}