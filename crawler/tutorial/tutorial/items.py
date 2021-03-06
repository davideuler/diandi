# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    link = Field()
    desc = Field()

class KuaidiSiteItem(Item):
    # define the fields for your item here like:
    # name = Field()
    mailman = Field();
    mailmantel = Field();
    region = Field()
    contact = Field()
    address = Field()
    sitetel = Field()
    sitename = Field()
    lat = Field()
    lng = Field()
    createddate = Field()
