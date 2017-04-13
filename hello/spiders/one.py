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
    def __init__(self, category='', a='1', *args, **kwargs):
	super(DmozSpider, self).__init__(*args, **kwargs) # <- important
        
        self.start_urls = []
	
	for line in open('/home/jarett/hello/oneinput-test-' + str(a) + '.csv'):
	    line = line.replace("/n", '')
	    line2 = line.split(',')[0]
	    parsed_uri = urlparse( line2 )
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	        
	    DmozSpider.dicty[domain] = line.split(',')[1]
	    DmozSpider.search[domain] = line.split(',')[2]
	    self.start_urls.append(line2)
    name = "one"
    a = 0.0
    def parse(self, response):
	DmozSpider.a = DmozSpider.a + 1
        filename = '/home/jarett/hello/answers.csv'
	

        DmozSpider.item[response.url] = []
	
	parsed_uri = urlparse( response.url )
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	    
        for link in LxmlLinkExtractor(allow=response.url,deny = ()).extract_links(response):
            DmozSpider.item[response.url].append(link.url)
	DmozSpider.item[response.url].append(response.url)
        #print DmozSpider.item[response.url]
        outsites = ""
	    
	for index, site in enumerate(DmozSpider.item[response.url]):
            outsites = outsites + site + ","
	outsites = outsites[:-1]
	#print outsites
	with open(filename, 'a') as f:
	    f.write((response.url + "," + str(DmozSpider.dicty[domain]) + "," + DmozSpider.search[domain]).encode("utf-8"))			
	    #print response.url
	url = 'http://localhost:6800/schedule.json'
	values = {'project' : 'hello', 'spider' : 'emailsnkeywords', 'pages': outsites}
        data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	log.msg(response)
