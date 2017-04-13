# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
import scrapy
import sys
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import re
import sys
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
    start_urls = []
    emails = []
    pr = ""
    reload(sys)
    sys.setdefaultencoding("utf-8")
    def __init__(self, category='', pages='http://dcssquared.com,http://highpassiveincomewebsite.com', **kwargs):
	
        self.start_urls = pages.split(',')
        
	print pages
    name = "emailsnkeywords"
    a = 0.0
    def parse(self, response):
	DmozSpider.a = DmozSpider.a + 1
        filename = '/home/jarett/hello/emails2.csv'
	parsed_uri = urlparse( response.url )
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        for line in open('/home/jarett/hello/answers.csv', 'r'):	
            if domain in line:
                DmozSpider.pr = line.split(',')[1]
                break
	emails = response.xpath('//*[contains(text(),"@")]/text()')
	kwscore = 0
	outemails = "" 	
        pattern = re.compile("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")
        for keyword in open('/home/jarett/hello/keywords.csv'):
	    
            if keyword.strip('\n') in (response.body.decode(response.encoding)).encode("utf-8").lower():
                kwscore = kwscore + 2
        newmail = True
	for index, emails2 in enumerate(emails):
            for (email) in re.findall(pattern, emails2.extract()):
		if email not in DmozSpider.emails:
		    for line in open('/home/jarett/hello/emails2.csv', 'r'):	
			if email in line:
			    newmail = False
		    
		    if newmail:
          	        with open(filename, 'a') as f:
			    
	                    f.write(domain + "," + email + "," + str(kwscore) + "," + str(DmozSpider.pr) + "\n")
	                    print response.url
        if kwscore > 0 and newmail == False:
            with open(filename, 'a') as f:
	        f.write(domain + ",," + str(kwscore) + "," + str(DmozSpider.pr) + "\n")
	        print response.url
	    
