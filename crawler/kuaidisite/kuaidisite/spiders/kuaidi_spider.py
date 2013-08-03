# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from kuaidisite.items import KuaidiSiteItem

cityname = '上海';
cityid = 31;

pagefrom = 1
pageto = 5

urlformat = "http://www.kuaidi100.com/network/net_%d_all_all_%d.htm"

def formaturl(url_format,cityid,pageno):
    return url_format % (cityid,pageno)


class KuaidiSpider(BaseSpider):
    name = "kuaidi"
    allowed_domains = ["www.kuaidi100.com"]
    start_urls = [
        #"http://www.peekyou.com/work/autodesk/page=%d" % i for i in xrange(18)
        formaturl(urlformat,cityid,page) for page in range( pagefrom, pageto)
    ];

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')

        items = []
        for site in sites:
           item = KuaidiSiteItem()
           #item['title'] = site.select('a/text()').extract()
           items.append(item)
        return items

