# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request,FormRequest
from neitui.items import NeituiItem
from neitui.settings import HEADERS,COOKIES
class NeituiSpider(Spider):
	name = "neitui"
	allowed_domains = ["www.neitui.me","api.weibo.com"]
	start_urls = [
        "http://www.neitui.me/?name=resume&handle=lists&endworkage=17&keyword=java&lastupdatetime=2015-01-05&city=%E6%9D%AD%E5%B7%9E&order=updatetime:desc&beginworkage=1"
    ]

	def __init__(self):
		self.headers = HEADERS
		self.cookies = COOKIES

	def __str__(self):
		return "NeituiSpider"

	def start_requests(self):
		for i, url in enumerate(self.start_urls):
			yield FormRequest(url, meta = {'cookiejar': i}, \
                              headers = self.headers, \
                              cookies =self.cookies,
                              callback = self.parse)#jump to login page

	def parse(self, response):
		import sys
		reload(sys)
		sys.setdefaultencoding('utf8')
		try:
			items = []
			hxs = Selector(response)
			for li in hxs.xpath("//div[contains(@class, 'commentjobs')]/ul/li/a"):
				item = NeituiItem()
				url = li.xpath('@href')[0].extract()
				name = li.xpath('./div/div/strong/text()')[0].extract()
				titleString = li.xpath(".//div[contains(@class,'jobtitle')]")[0].xpath('.//text()').extract()
				title = ''.join(titleString)
				detailStrings = li.xpath(".//div[contains(@class,'jobdetail')]//text()").extract()
				detail = ''.join(detailStrings)
				item['name'] = name
				item['title'] = title
				item['url'] = url
				item['detail'] = detail
				item['content'] = li.extract()
				yield item
		except Exception,e:
			print str(e)
			raise
