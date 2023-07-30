import csv

import scrapy


class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    allowed_domains = ["www.flipkart.com"]
    start_urls = ["https://www.flipkart.com/"]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'Network-Type=4g; T=TI168968105133900191886002122581596257230502413329397848907482088706; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE2OTE0MDkwNTEsImlhdCI6MTY4OTY4MTA1MSwiaXNzIjoia2V2bGFyIiwianRpIjoiM2VlMWJhNjAtZGMxMC00MTM0LWE0NjktZmJkYTQyNzFlYjIzIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjg5NjgxMDUxMzM5MDAxOTE4ODYwMDIxMjI1ODE1OTYyNTcyMzA1MDI0MTMzMjkzOTc4NDg5MDc0ODIwODg3MDYiLCJrZXZJZCI6IlZJNjY2RkVCQTRGMDQ5NEVCQUJGNERCNUJFMDY5NzExMDEiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.07h1Jfd7-EQr7QLJV12Ws1BkTLTIoqchYRyXY5WCoaw; K-ACTION=null; vh=569; vw=1280; dpr=1.5; _pxvid=a58a3f9c-2561-11ee-bcdb-2f8935521f5a; __pxvid=a60205c3-2561-11ee-ac07-0242ac120002; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19564%7CMCMID%7C69453933372697657344842806805403300082%7CMCAID%7CNONE%7CMCOPTOUT-1690282704s%7CNONE%7CMCAAMLH-1690285864%7C6%7CMCAAMB-1690880304%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; qH=5985e3313e9e348f; s_cc=true; pxcts=6b159ec9-2ac9-11ee-aa87-70776961644a; fonts-loaded=en_loaded; s_sq=%5B%5BB%5D%5D; gpv_pn_t=Store%20Browse; gpv_pn=Store%20%3AClothing%20and%20Accessories%7CLehenga%20Cholis%7CWomen%27s%20Lehenga%20Cholis; SN=VI666FEBA4F0494EBABF4DB5BE06971101.TOK475A55CE146D47F8B1FA406E4350CB0A.1690276751.LO; Network-Type=4g; S=d1t18PT9FP1g/XT8/E0g5Pz8/Pz0piAwp0kDGuENwa1GVpQkqfzeU0/hmd2q5i4UrL2cKex8enc+bSf+bLJ75PXnSeQ==; _px3=2de0f684c8af710601f6ca625ea2fbc1c358d4edc56f4fad1fcb148a0dc043f3:Nufsq56iqdD+SEETBPBQ/9lYxia0BcWe+tuWMH6etIl8UWOmU3mtzuaGKf0m1y3FdWRPphfMQbdb5InBzUL7Yw==:1000:W9DiLi5S0UAKa5jULeQFXwRRKFvuygr6Q0h6+vAOPomve7Vd1vtKSP8cHLpopC9+SLBCRteJVZMSOEdnvvtee+3QML42odSRw3q+GapVmqRrsFGjNsCPSCJeYSMfJd4NphD7pDj/jQYGMhug2d1RXwf0YCO9Mp3WQrk67YjReyF4dinKblNFA3Fs8Ot5BMRsw6IwBtXCtdKKyPJx43nfEw==; K-ACTION=null; SN=VI666FEBA4F0494EBABF4DB5BE06971101.TOK475A55CE146D47F8B1FA406E4350CB0A.1690277349.LO; T=TI168968105133900191886002122581596257230502413329397848907482088706; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE2OTE0MDkwNTEsImlhdCI6MTY4OTY4MTA1MSwiaXNzIjoia2V2bGFyIiwianRpIjoiM2VlMWJhNjAtZGMxMC00MTM0LWE0NjktZmJkYTQyNzFlYjIzIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjg5NjgxMDUxMzM5MDAxOTE4ODYwMDIxMjI1ODE1OTYyNTcyMzA1MDI0MTMzMjkzOTc4NDg5MDc0ODIwODg3MDYiLCJrZXZJZCI6IlZJNjY2RkVCQTRGMDQ5NEVCQUJGNERCNUJFMDY5NzExMDEiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.07h1Jfd7-EQr7QLJV12Ws1BkTLTIoqchYRyXY5WCoaw',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.248", "Google Chrome";v="114.0.5735.248"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    custom_settings = {
        'FEED_URI': 'output.csv',
        'FEED_FORMAT': 'csv',
        # 'ITEM_PIPELINES': {
        #     "flipkart_scraper.pipelines.FlipkartScraperPipeline": 300},
        # 'IMAGES_STORE': "IMAGES",
    }

    def start_requests(self):
        links = read_links_from_csv("input.csv");
        for link in links:
            # print(link)
            list_link = link.get('url')
            print(list_link)
            yield scrapy.Request(
                url=list_link,
                headers=self.headers, callback=self.parse
            )

    def parse(self, response):
        product_links = response.xpath('//*[@class="_2UzuFa"]/@href').getall()
        for product_link in product_links:
            yield response.follow(
                url=product_link,
                headers=self.headers, callback=self.productInformation)
        pagination = response.xpath('//*[@class="yFHi8N"]/a/@href').getall()
        next_page = pagination[-1]
        if next_page:
            yield response.follow(url=next_page, headers=self.headers, callback=self.parse)

    def productInformation(self, response):
        item = {}
        item["bread crumbs"] = ">".join(response.xpath('//*[@class="_2whKao"]/text()').getall())
        item["title"] = response.xpath('//*[@class="B_NuCI"]/text()').get()
        item["original_Price"] = response.xpath('//*[@class="_3I9_wc _2p6lqe"]/text()[2]').get()
        discount_price = response.xpath('//*[@class="_30jeq3 _16Jk6d"]/text()').get()
        item["discount_price"] = discount_price.strip('₹')
        discount = response.xpath('//*[@class="_3Ay6Sb _31Dcoz pZkvcx"]/span/text()').get()
        if discount:
            item["discount %"] = discount.split('%')[0]
        item["rating"] = response.xpath('//*[@class="_3LWZlK _3uSWvT"]/text()').get()
        review = response.xpath('//*[@class="_2_R_DZ"]/span/text()').get()
        if review:
            item["rating count"] = review.split()[0]
        item["colors"] = response.xpath('//*[@class="kmlXmn _31hAvz"]/@href').getall()
        item["size"] = ",".join(response.xpath('//*[@class="_1fGeJ5 _2UVyXR _31hAvz"]/text()').getall())
        item["offers"] = ",".join(response.xpath('//*[@class="_16eBzU col"]/span[2]/text()').getall())
        item["seller"] = response.xpath('//*[@id="sellerName"]/span/span/text()').get()
        item["seller rating"] = response.xpath('//*[@class="_3LWZlK _1D-8OL"]/text()').get()
        item["service"] = response.xpath('//*[@class="_2MJMLX"]/text()').get()
        item["description"] = response.xpath('//*[@class="K4SXrT funtru"]/div/div/div[2]/div[2]/p/text()').getall()
        item["product_images"] = [image.split('?')[0] for image in response.xpath('//*[@class="q6DClP"]/@src').getall()
                                  if '?' in image]
        product_detail_keys = response.xpath('//*[@class="col col-3-12 _2H87wv"]/text()').getall()
        product_detail_values = response.xpath('//*[@class="col col-9-12 _2vZqPX"]/text()').getall()
        # item["product_details"] = [item for pair in zip(product_detail_keys, product_detail_values) for item in pair]
        result_list = [f"{key.strip()}: {value}" for key, value in zip(product_detail_keys, product_detail_values)]
        item["product_details"] = ",".join(result_list)
        print(item["product_details"])
        specs = response.xpath('//*[@class="flxcaE"][1]')
        if specs:
            keys = specs.xpath('//*[@class="_1hKmbr col col-3-12"]/text()').getall()
            values = specs.xpath('//*[@class="_21lJbe"]/text()').getall()

            result_list = [f"{key.strip()}: {value}" for key, value in zip(keys, values)]
            # merged_list = [item for pair in zip(keys, values) for item in pair]
            item["specifications"] = ",".join(result_list)
        yield item
        # print(item["specifications"])


def read_links_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        return list(csv.DictReader(csvfile))
