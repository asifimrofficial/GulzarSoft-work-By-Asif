# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


# useful for handling different item types with a single interface


class FlipkartScraperPipeline(ImagesPipeline):
    print("hi")

    def get_media_requests(self, item, info):
        i = 0
        for image_url in item['product_images']:
            i += 1
            print(image_url)
            yield scrapy.Request(image_url, meta={'i': i})

    def file_path(self, request, response=None, info=None, *, item=None):
        path = item["product_title"]
        i = request.meta["i"]
        return f'/{path}-{i}.jpeg'
        # return f'/{item["Product_name"]}.jpg'

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise scrapy.exceptions.DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
