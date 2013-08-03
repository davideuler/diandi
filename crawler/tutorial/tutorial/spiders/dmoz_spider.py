from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import TutorialItem


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #print("filename %s" % filename)
        #open(filename, 'wb').write(response.body)

        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')

        for site in sites:
            title = site.select('a/text()').extract()
            link = site.select('a/@href').extract()
            desc = site.select('text()').extract()
            print title, link, desc
        items = []
        for site in sites:
           item = TutorialItem()
           item['title'] = site.select('a/text()').extract()
           item['link'] = site.select('a/@href').extract()
           item['desc'] = site.select('text()').extract()
           items.append(item)
        return items