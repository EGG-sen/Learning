import scrapy

from scrape_ssr1.items import ScrapeSsr1Item


class ScrapeSsr1Spider(scrapy.Spider):
    name = "scrape_ssr1"
    allowed_domains = ["ssr1.scrape.center/page/"]
    start_urls = ["http://ssr1.scrape.center"]

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
            scrapeSsr1Item['titleCh'] = i.xpath(".//a[@class='name']/h2[@class='m-b-sm']/text()").get().split('-')[0]
            scrapeSsr1Item['titleEn'] = i.xpath(".//div/a[@class='name']/h2[@class='m-b-sm']/text()").get().split('-')[
                1]
            scrapeSsr1Item['categories'] = i.xpath(".//div/button/span/text()").getall()
            scrapeSsr1Item['screenLocation'] = i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
                                                       "el-col-md-16']/div[@class='m-v-sm info'][1]/span[1]/text()").get()
            scrapeSsr1Item['screenTime'] = i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
                                                   "el-col-md-16']/div[@class='m-v-sm info'][2]/span/text()").get()
            scrapeSsr1Item['totalTime'] = i.xpath(".//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 "
                                                  "el-col-md-16']/div[@class='m-v-sm info'][1]/span[3]/text()").get()
            scrapeSsr1Item['star'] = i.xpath(".//div[@class='el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4']/p["
                                             "@class='score m-t-md m-b-n-sm']/text()").get().strip()
            
            yield scrapeSsr1Item
