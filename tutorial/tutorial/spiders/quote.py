import scrapy

from tutorial.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/page/1/",
                  "http://quotes.toscrape.com/page/2/"
                  ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #    f.write(response.body)
        # self.log('Saved file %s' % filename)
        for quote in response.xpath("//div[@class='quote']"):
            # yield {
            # 'text': quote.xpath("./span[@class='text']/text()").get(),
            # 'author': quote.xpath(".//small[@clss='author']/text()").get(),
            # 'tags': quote.xpath(".//a[@class='tag']/text()").getall(),
            # }
            quoteItem = QuotesItem()
            quoteItem['text'] = quote.xpath("./span[@class='text']/text()").get()
            quoteItem['author'] = quote.xpath(".//small[@class='author']/text()").get()
            quoteItem['tags'] = quote.xpath(".//a[@class='tag']/text()").getall()

            yield quoteItem
