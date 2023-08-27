import scrapy


class CruisemapperSpiderSpider(scrapy.Spider):
    name = "cruisemapper_spider"
    allowed_domains = ["www.cruisemapper.com"]
    start_urls = ["https://www.cruisemapper.com/ships"]
    headers = {
        'authority': 'www.cruisemapper.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.1.1245601111.1690878780; _ga_S7E9PPFQCS=GS1.1.1690878779.1.1.1690879138.0.0.0; __gads=ID=ce6649adbfa2be26-221f283c26e30047:T=1690878781:RT=1690879140:S=ALNI_MYKAs677agZp_wBDYFwUhp5yOUkow; __gpi=UID=00000d3b03e3fc44:T=1690878781:RT=1690879140:S=ALNI_MY7GGhClbariDS-X283HNC1Wqa1AA',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    custom_settings = {
        'FEED_URI': 'cruisemapper.csv',
        'FEED_FORMAT': 'csv',
        "ROBOTSTXT_OBEY": False,
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, callback=self.parse)

    def parse(self, response):
        product_urls = response.xpath('//div[@class="shipListItem"]/a/@href').getall()
        next_page_url = response.xpath('//*[@class="fa fa-chevron-right"]/parent::a/@href').get()
        for product_url in product_urls:
            yield scrapy.Request(url=product_url, headers=self.headers, callback=self.scrape_product_details)
        if (next_page_url):
            yield scrapy.Request(url=next_page_url, headers=self.headers, callback=self.parse)

    def scrape_product_details(self, response):
        item = {}

        item['name'] = response.xpath('//*[@class="pageTitle shipItemTitle"]/text()').get()
        item['Flag state'] = response.xpath("//td[contains(text(),'Flag state')]/following-sibling::td/text()").get()
        list_year_age = response.xpath(
            "//td[contains(text(),'Year of build')]/following-sibling::td/text()").get().replace('\xa0', '').split('/')
        item["Year of Build"] = list_year_age[0]
        if (len(list_year_age) > 1):
            item["Age"] = list_year_age[1].split(':')[1]
        item['Builder'] = response.xpath("//td[contains(text(),'Builder')]/following-sibling::td/text()").get()
        item['Class'] = response.xpath("//td[contains(text(),'Class')]/following-sibling::td/text()").get()
        item['Building cost'] = response.xpath(
            "//td[contains(text(),'Building cost')]/following-sibling::td/text()").get()
        item['Speed'] = "".join(response.xpath("//td[contains(text(),'Speed')]/following-sibling::td//text()").getall())
        item['Length (LOA)'] = "".join(
            response.xpath("//td[contains(text(),'Length (LOA)')]/following-sibling::td//text()").getall())
        item['Beam (width)'] = "".join(
            response.xpath("//td[contains(text(),'Beam (width)')]/following-sibling::td//text()").getall())
        item['Gross Tonnage'] = response.xpath(
            "//td[contains(text(),'Gross Tonnage')]/following-sibling::td/text()").get()
        item['Passengers'] = response.xpath("//td[contains(text(),'Passengers')]/following-sibling::td/text()").get()
        item['Crew'] = response.xpath("//td[contains(text(),'Crew')]/following-sibling::td/text()").get()
        item['Passengers-to-space ratio'] = response.xpath(
            "//td[contains(text(),'Passengers-to-space ratio')]/following-sibling::td/text()").get()
        item['Decks'] = response.xpath("//td[contains(text(),'Decks')]/following-sibling::td/text()").get()
        item['Cabins'] = response.xpath("//td[contains(text(),'Cabins')]/following-sibling::td/text()").get()
        item['Decks with cabins'] = response.xpath(
            "//td[contains(text(),'Decks with cabins')]/following-sibling::td/text()").get()
        item['Last Refurbishment'] = response.xpath(
            "//td[contains(text(),'Last Refurbishment')]/following-sibling::td/text()").get()
        item['Sister-ships'] = response.xpath(
            "//td[contains(text(),'Sister-ships')]/following-sibling::td/text()").get()
        item['Christened by'] = response.xpath(
            "//td[contains(text(),'Christened by')]/following-sibling::td/text()").get()
        item['Owner'] = response.xpath("//td[contains(text(),'Owner')]/following-sibling::td/text()").get()
        item['Operator'] = response.xpath("//td[contains(text(),'Operator')]/following-sibling::td/text()").get()
        item['detail url'] = response.url

        yield item
