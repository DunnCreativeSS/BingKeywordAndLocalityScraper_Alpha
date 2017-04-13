# -*- coding: utf-8 -*-
import scrapy
import os
import errno
import os
import one
import pycurl
from StringIO import StringIO
from scrapy.command import ScrapyCommand

# scrapy api imports
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
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

from scrapy.contrib.spiders import CrawlSpider, Rule
import os
from scrapy import Request
from scrapy.crawler import CrawlerProcess
import scrapy
from ast import literal_eval
import sys


class DmozSpider(scrapy.Spider):
    def __init__(self, **kwargs):
	#super(DmozSpider, self).__init__(**kwargs)
	pass
    process = CrawlerProcess({
    # An example of a custom setting
		'LOG_LEVEL': 'DEBUG',
		'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})
    search = {}
    name = "hello"
    base = 'https://www.bing.com/search?q='
    start_urls = []
    i = 0	
    count = 0
    a = 0
    filename = '/home/jarett/hello/answers.csv'
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY

    try:
	file_handle = os.open(filename, flags)
    except OSError as e:
	if e.errno == errno.EEXIST:  
	    pass
	else:  
	    raise
    else:  
	with os.fdopen(file_handle, 'w') as file_obj:
	    file_obj.write('url,font count,pagerank,emails on homepage,ranking for\n')

    domains = []
    for line in open('/home/jarett/hello/cities.csv', 'r'):
        count = count + 1
	
	line3 = line.replace('\n', '')
	line2 = line3.replace(' ', '+')
	search[count] = line3.replace(',', '')
        x = 0
        #100 for realzies
        while x <= 100:
	    url = base + line2 + '&first=' + str(x) + '&count=10'
	    start_urls.append(url)
	    x = x + 10

    print start_urls
    def parse(self, response):
	DmozSpider.i = DmozSpider.i + 1
	DmozSpider.a = DmozSpider.a + 1
	if DmozSpider.i >= 5:
            DmozSpider.i = 0

	filename = '/home/jarett/hello/oneinput-test-' + str(DmozSpider.a) + '.csv'
	urls = response.xpath('//*[@id="b_results"]/li/h2/a/@href').extract()
	
	with open(filename, 'a') as f:

	    for url in urls:
	        parsed_uri = urlparse( url )
	        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	        if domain not in DmozSpider.domains:
		    if 'https' or 'http' in url:
		        DmozSpider.domains.append(domain)
			f.write(domain + "," + str(int(response.url[(response.url.index('first=') + 6):-9]) / 10 + 1) + "," + str(DmozSpider.search[int(DmozSpider.a / 10) + 1]) + "\n")

	
	url = 'http://localhost:6800/schedule.json'
	
	values = {'project' : 'hello', 'spider' : 'one', 'pr': str(int(response.url[(response.url.index('first=') + 6):-9]) / 10 + 1), 'a': str(DmozSpider.a)}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	log.msg(response)


