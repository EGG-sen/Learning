# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import hashlib
import os
from contextlib import suppress

from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http.request import NO_CALLBACK, Request
from scrapy.utils.python import to_bytes

from scrape_ssr1 import settings
from scrape_ssr1.items import ScrapeSsr1Item


class ScrapeSsr1Pipeline:
    def process_item(self, item, spider):
        item['titleCh'] = item['titleCh'].split('-')[0].strip()
        item['titleEn'] = item['titleEn'].split('-')[1].strip()
        item['totalTime'] = item['totalTime'].split(' ')[0]
        item['categories'] = "、".join(item['categories'])
        if item['screenTime'] is not None:
            item['screenTime'] = item['screenTime'].split(' ')[0]
        # item['star'] = item['star'].strip()
        item['star'] = item['star'].split(' ')[-1]
        item['introduction'] = item['introduction'].replace("\n", '').strip()
        item['actor'] = "、".join(item['actor'])
        return item

# class ImagesPipeline(ImagesPipeline):
#     # 重写get_media_requestsget_media_requests方法,发送下载请求
#     def get_media_requests(self, item, info):
#         requestItems = super(ImagesPipeline, self).get_media_requests(item, info)
#         # 将item数据加入请求中
#         for requestItem in requestItems:
#             requestItem.item = item
#         return requestItems
#
#     # 重写file_path方法
#     def file_path(self, request, response=None, info=None, *, item=None):
#         # 这个方式是在图片将要被存储时候调用，来获取这个图片的存储路径
#         # 获取父类返回的保存地址
#         path = super(ImagesPipeline, self).file_path(request, response, info)
#         images_store = settings.IMAGES_STORE
#         # 创建图片分类文件夹
#         category_path = os.path.join(images_store)
#         if not os.path.exists(category_path):
#             os.mkdir(category_path)
#
#         # 重新返回新的图片保存路径
#         image_name = path.replace('full/', '')
#         image_path = os.path.join(category_path, image_name)
#         return image_path
