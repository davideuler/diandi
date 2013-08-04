# Scrapy settings for kuaidisite project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'kuaidisite'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['kuaidisite.spiders']
NEWSPIDER_MODULE = 'kuaidisite.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'kuaidisite (+http://www.diandi.com)'

DOWNLOAD_DELAY = 0.5
RANDOMIZE_DOWNLOAD_DELAY = True
