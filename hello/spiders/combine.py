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
reload(sys)
domains = []
emails = {}
kwscores = {}
pr = {}
sys.setdefaultencoding("utf-8")
for line in open('/home/jarett/hello/emails2.csv', 'r'):
    domain = line.split(',')[0]
    if domain not in domains:
        domains.append(domain)
        if line.split(',')[1] is not "":
            emails[domain] = line.split(',')[1]
        kwscores[domain] = line.split(',')[2]
        pr[domain] = line.split(',')[3]
    else:
        if line.split(',')[1] is not "":
	    emails[domain] = emails[domain] + ';' + line.split(',')[1]
        kwscores[domain] = str(int(kwscores[domain]) + int(line.split(',')[2]))
	
    
with open('/home/jarett/hello/combinedenablon.csv', 'a') as f:
    for domain in domains:
        score = ((10 - int(pr[domain])) * 10) + int(kwscores[domain])
        f.write(domain + "," + str(score) + "," + str(int(kwscores[domain]) / 2) + "," + emails[domain] + "\n")
    
		
		
	      
