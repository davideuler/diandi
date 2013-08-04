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

        f = codecs.open('record.txt', 'w' )
        for site in sites:
           item = KuaidiSiteItem()
           #item['title'] = site.select('a/text()').extract()
           item['company'] = site.select("//span[@class='font999']/text()").extract()
           item['sitename'] = site.select("//a[@class='networkComname']/text()").extract()

           #print("company: %s" % (item['company']) )
           strs = ""
           for i in item['company']:
              strs = strs + i
           print( "company: %s" % strs)
           print strs
           line = json.dumps(dict(item), ensure_ascii=False) + "\n"
           print("dump: %s" % line)
           print("unicode company: %s" % unicode(item['company'][0]) )

           #f.write(item['company'])

           items.append(item)
        f.close()
        return items
