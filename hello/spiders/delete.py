# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
import scrapy
import sys
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import re
import urllib
import urllib2
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode
from scrapy.utils.project import get_project_settings
from urlparse import urlparse
class DmozSpider(scrapy.Spider):
    dicty = {}
    search = {}
    item = {}
    reload(sys)
    sys.setdefaultencoding("utf-8")
    def __init__(self, category='', pages=['http://localhost:6800/jobs'], **kwargs):
	
        self.start_urls = pages
	
    name = "delete"
    a = 0.0
    def parse(self, response):
	DmozSpider.a = DmozSpider.a + 1

	jobs = response.xpath('//tr/td[3]/text()').extract()
	print jobs
	for index, job in enumerate(jobs):
            url = 'http://localhost:6800/cancel.json'
	    values = {'project' : 'hello', 'job' : job}
            data = urllib.urlencode(values)
	    req = urllib2.Request(url, data)
	    response = urllib2.urlopen(req)
		
