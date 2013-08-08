# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from kuaidisite.items import KuaidiSiteItem
import json
import urllib
import sys
import codecs


cityname = '上海';
cityid = 31;

pagefrom = 1
pageto = 2

urlformat = "http://www.kuaidi100.com/network/net_%d_all_all_%d.htm"

def formaturl(url_format,cityid,pageno):
    return url_format % (cityid,pageno)

#sys.stdout = codecs.getwriter('utf-8')(sys.stdout) 

class KuaidiSpider(BaseSpider):
    name = "kuaidi"
    allowed_domains = ["www.kuaidi100.com"]
    start_urls = [
        #"http://www.peekyou.com/work/autodesk/page=%d" % i for i in xrange(18)
        formaturl(urlformat,cityid,page) for page in range( pagefrom, pageto)
    ];


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select("//div[@class='networkListItem']")

        items = []

        f = codecs.open('record.txt', 'w' ,encoding='utf-8')
        for site in sites:
           item = KuaidiSiteItem()
           #item['title'] = site.select('a/text()').extract()
           item['company'] = site.select("span[@class='font999']/text()").extract()
           item['sitename'] = site.select("a[1]/strong/text()").extract()
           item['region'] = site.select("text()[3]").extract()
           item['address'] = site.select("text()[4]").extract()
           item['sitetel'] = site.select("text()[5]").extract()

           line = json.dumps(dict(item), ensure_ascii=False) + "\n"
           print("dump: %s" % line)
           #print "site:",item 
           #print("unicode company: %s" % unicode(item['company'][0]) )

           f.write(line)

           items.append(item)
        f.close()
        return items
