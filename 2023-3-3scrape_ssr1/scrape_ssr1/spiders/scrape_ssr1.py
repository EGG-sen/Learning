import scrapy

from scrape_ssr1.items import ScrapeSsr1Item


class ScrapeSsr1Spider(scrapy.Spider):
    name = "scrape_ssr1"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["http://ssr1.scrape.center/"]

    def detail_parse(self, response):
        scrapeSsr1Item = response.meta['scrapeItem']
        scrapeSsr1Item['introduction'] = response.xpath(".//div[@class='drama']/p/text()").get()
        scrapeSsr1Item['director'] = response.xpath(".//p[@class='name text-center m-b-none m-t-xs']/text()").get()
        scrapeSsr1Item['actor'] = response.xpath(".//p[@class='el-tooltip name text-center m-b-none m-t-xs "
                                                 "item']/text()").getall()
        yield scrapeSsr1Item

    def parse(self, response):
        for i in response.xpath("//div[@class='el-card__body']/div[@class='el-row']"):
            # yield {
            #     "titleCh": i.xpath(".//a[@class='name']/h2[@class='m-b-sm']/text()").get().split('-')[0],
            #     "titleEn": i.xpath(".//div/a[@class='name']/h2[@class='m-b-sm']/text()").get().split('-')[1],
            #     "categories": i.xpath(".//div/button/span/text()").getall(),
            #     "screenLocation": i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
            #                               "el-col-md-16']/div[@class='m-v-sm info'][1]/span[1]/text()").get(),
            #     "screenTime": i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
            #                           "el-col-md-16']/div[@class='m-v-sm info'][2]/span/text()").get(),
            #     "totalTime": i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
            #                          "el-col-md-16']/div[@class='m-v-sm info'][1]/span[3]/text()").get(),
            #     "star": i.xpath(".//div[@class='el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4']/p["
            #                     "@class='score m-t-md m-b-n-sm']/text()").get().strip()
            # }
            scrapeSsr1Item = ScrapeSsr1Item()
            scrapeSsr1Item['titleCh'] = i.xpath(".//a[@class='name']/h2[@class='m-b-sm']/text()").get()
            scrapeSsr1Item['titleEn'] = i.xpath(".//div/a[@class='name']/h2[@class='m-b-sm']/text()").get()
            scrapeSsr1Item['categories'] = i.xpath(".//div/button/span/text()").getall()
            scrapeSsr1Item['screenLocation'] = i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
                                                       "el-col-md-16']/div[@class='m-v-sm info'][1]/span[1]/text()").get()
            scrapeSsr1Item['screenTime'] = i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
                                                   "el-col-md-16']/div[@class='m-v-sm info'][2]/span/text()").get()
            scrapeSsr1Item['totalTime'] = i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
                                                  "el-col-md-16']/div[@class='m-v-sm info'][1]/span[3]/text()").get()
            scrapeSsr1Item['star'] = i.xpath(".//div[@class='el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4']/p["
                                             "@class='score m-t-md m-b-n-sm']/text()").get()
            scrapeSsr1Item['image_urls'] = i.xpath('.//a/img[@class="cover"]/@src').get()

            # url = "http://ssr1.scrape.center/" + i.xpath(".//a[@class='name']//@href").get()
            # 用于连接之前的网址与后面的网址
            url = response.urljoin(i.xpath(".//a[@class='name']//@href").get())

            # 翻页操作，回调parse方法处理
            for j in range(2, 11):
                next_urls = "http://ssr1.scrape.center/page/{0}".format(j)
                yield scrapy.Request(url=next_urls, callback=self.parse)

            yield scrapy.Request(url=url, callback=self.detail_parse, meta={'scrapeItem': scrapeSsr1Item})
