import scrapy


class MyntraSpider(scrapy.Spider):
    name = "myntra"
    allowed_domains = ["www.myntra.com"]
    start_urls = ["https://www.myntra.com/men-casual-shirts"]

    def parse(self, response):
        print(response.text)
        product_urls = response.xpath('//*[@class="product-base"]/a/@href').getall()
        print(product_urls)
        for product_url in product_urls:
            yield response.follow(url=product_url, callback=self.scrape_product_details)

    def scrape_product_details(self, response):
        print(response.text)
