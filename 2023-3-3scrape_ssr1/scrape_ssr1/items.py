# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeSsr1Item(scrapy.Item):
    titleCh = scrapy.Field()
    titleEn = scrapy.Field()
    categories = scrapy.Field()
    screenLocation = scrapy.Field()
    screenTime = scrapy.Field()
    totalTime = scrapy.Field()
    star = scrapy.Field()
    image = scrapy.Field()
    image_urls = scrapy.Field()
    introduction = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
