# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
import scrapy
import sys
import urllib
from scrapy import signals, log
import urllib2
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode
from scrapy.utils.project import get_project_settings
from urlparse import urlparse
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import re
class DmozSpider(scrapy.Spider):
    dicty = {}
    search = {}
    item = {}
    reload(sys)
    sys.setdefaultencoding("utf-8")
    def __init__(self, category='', a='2339', **kwargs):
	
        self.start_urls = ["https://en.m.wikipedia.org/wiki/List_of_United_States_cities_by_population"]
	
    name = "scrape"
    a = 0.0
    cities = []
    def parse(self, response):
	DmozSpider.a = DmozSpider.a + 1
        filename = '/home/jarett/hello/cities.csv'
	italics = response.xpath('//td[2]/i/a/text()').extract()
	links = response.xpath('//td[2]/a/text()').extract()
	for link in links:
	    if link not in DmozSpider.cities:
		DmozSpider.cities.append(link)
	for italic in italics:
	    if italic not in DmozSpider.cities:
		DmozSpider.cities.append(italic)
	print response
	print 'hello'
	print DmozSpider.cities
	
	with open(filename, 'a') as f:
	    for city in DmozSpider.cities:
		if '[' in city:
		    city = city.split('[')[0]
		if DmozSpider.a <= 300:
		    f.write("automotive companies in " + city + "\n")	
		    f.write("chemicals companies in " + city + "\n")	
		    f.write("energy companies in " + city + "\n")	
		    f.write("utilities companies in " + city + "\n")	
		    f.write("financial services companies in " + city + "\n")	
		    f.write("food companies in " + city + "\n")	
		    f.write("beverage companies in " + city + "\n")	
		    f.write("health care companies in " + city + "\n")	
		    f.write("pharmaceuticals companies in " + city + "\n")	
		    f.write("manufacturing companies in " + city + "\n")
		    f.write("mining companies in " + city + "\n")
		    f.write("metals companies in " + city + "\n")
		    f.write("oil companies in " + city + "\n")
		    f.write("gas companies in " + city + "\n")
		
		
	      
