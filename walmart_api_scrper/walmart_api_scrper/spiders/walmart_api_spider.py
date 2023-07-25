import csv
import json
import re

# from ..items import WalmartApiScrperItem
import scrapy


class WalmartApiSpiderSpider(scrapy.Spider):
    name = "walmart_api_spider"
    allowed_domains = ["www.walmart.ca", "api.bazaarvoice.com"]
    start_urls = ["https://www.walmart.ca/browse/toys/10011"]

    custom_settings = {
        # 'FEED_URI': 'output.csv',
        # 'FEED_FORMAT': 'csv',
        'ITEM_PIPELINES': {
            "walmart_api_scrper.pipelines.WalmartApiScrperPipeline": 300},
        'IMAGES_STORE': "IMAGES",
    }

    def price_payload_editor(self, product_id, sku_id):
        return json.dumps({
            "fsa": "L5V",
            "availabilityStoreId": "1061",
            "lang": "en",
            "experience": "whiteGM",
            "pricingStoreId": "1061",
            "geoAddress": {
                "deliveryAddress": {
                    "zipCode": "L5V2N6",
                    "countryCode": "CA"
                },
                "pickupStoreAddresses": [
                    {
                        "nodeId": "1061",
                        "nodeType": "STORE"
                    }
                ],
                "deliveryStoreAddresses": [
                    {
                        "nodeId": "1061",
                        "nodeType": "STORE"
                    }
                ]
            },
            "products": [
                {
                    "productId": f"{product_id}",
                    "skuIds": [
                        f"{sku_id}"
                    ]
                }
            ]
        })

    headers = {
        'authority': 'www.walmart.ca',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'deliveryCatchment=1061; walmart.nearestPostalCode=L5V2N6; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; walmart.nearestLatLng="43.60822,-79.69387"; userSegment=50-percent; vtc=TCbjYc0dcz1gjlkzjAPUuI; walmart.id=ee196ffb-a43e-459e-8864-f9a9ec399d2e; _gcl_au=1.1.1224370931.1688655842; _ga=GA1.2.1430749466.1688655844; s_ecid=MCMID%7C04611159140574387780942481365272090971; _scid=43fb8521-6d07-45c0-9588-265ecf878adf; _pxvid=5c804495-1c0e-11ee-a22c-94f29ca95557; _sctr=1%7C1688583600000; wmt.c=0; DYN_USER_ID=d281b476-c76e-4e40-a973-c4e54ca7c221; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4x440yDZOTOKXfabw5y0wClWZc8uwnCofoZXbgdc8Wg1DvT3/L30ukhY9Csw6G/WwruRUiL8XWW4LgIvqa6IFImpE9Q3WXwDa5FgvP7/bgJgF+tZHhaD+2qI6q2PBzNRVj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0/w+p+K/WjzuYPePvMUDmNzgKO891whEejdvzQcYsAftTdC0GD+nVo3z789gPVCszb/SoGFgAYL9DGZ8K45WCXDCcb9mgycy9jtT1uIyOBHYf8XczTynrpo9lYjtyESE1EaEj+FZRs1wfVGuoIo0cBxS6b2DXsFBiTsbeVYiiN2UqC/BHIiytsv610gg9Ws5TtMIBWDogSu1BWWsXSTY5NdtfWbPEEu7KJ458IAhMgl0r1eX9YGQ0laieVMoEr348=; LT=1688655867643; _cs_c=0; cookiePolicy=true; salsify_session_id=9a8ba3cb-c9f3-4936-88bf-55f8d3d75898; localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJjaXR5IjoiTWlzc2lzc2F1Z2EiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhFQVJUTEFORCwgTUlTU0lTU0FVR0EsT04iLCJmdWxmaWxsbWVudFN0b3JlSWQiOiIxMDYxIiwiZnVsZmlsbG1lbnRUeXBlIjoiSU5TVE9SRV9QSUNLVVAifQ==; _pin_unauth=dWlkPU5tWXpOVEJtWVdRdE5EazFOQzAwTlRVd0xUazFPVFl0TWpRek5UTTNNV1F5WldNMw; crl8.fpcuid=a09d30a0-a4fd-4bd9-83eb-4de6cb85eb36; BVBRANDID=0d4957ce-7b73-4c6f-a39c-acb286014e65; NEXT_GEN.ENABLED=1; _gid=GA1.2.1243505518.1689056936; pxcts=07112ad7-2082-11ee-b7b7-71686f4e484a; cartId=1ad01a8b-6e71-4286-ba3e-bd2aa3585135; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; s_cc=true; BVImplmain_site=2036; s_sq=%5B%5BB%5D%5D; bstc=VL3JA9eYBu-lpXi0De5f6M; xpa=12TNt|18laY|1iNRR|20jZP|4Kq-Y|5sfML|ALEbn|AvWMt|J5Q2f|KX9zf|KxDCx|OAQpG|OCyta|PdYAO|Qligk|RxMsL|S2NR7|S9Aer|Sek64|VUeER|Zsz8o|cGOTQ|cMouF|fTP7G|gUGfp|jE0bf|qRHgs|uAQc6|uk0R3; exp-ck=12TNt118laY11iNRR120jZP15sfML1ALEbn3J5Q2f1KxDCx1OAQpG1PdYAO1Qligk1RxMsL1S2NR73S9Aer4Sek643VUeER1Zsz8o1cGOTQ1fTP7G1gUGfp1uk0R31; ak_bmsc=DF1D80B5359B6C39C2B5CEFFB506671B~000000000000000000000000000000~YAAQP/V0aMGzP0SJAQAA9cmRSRT//Na/zsaKWuUkrGmaNVlN2nZs1KSp+M16t4YQ3gEH6ODSe2XJXKJujJjdVfnbq689GZwbt1q8OcBQ85GI8580+Jqwl8Gu9fxvsDh2ebeupYIRmjGqnDNAu6SqlUuYOU5OLLtSRv8FJzQjZYdA2uU6Zii3deDi1cDReZbGe8hXrDB3ThL9CETcbS2orBmBqP3NcyhVykivuZ5RecCN7dw4LcAoHJufbBrHoh07wKBdm4xu1uwTyJZB9kS3z5OsBY53EEQ0SFF6aT/dnyMj+hq3EGCTUtjQoZ+M3MmY+4flfFWltNTMQygi3QmII6vl5ChkSDf27WeRUJlTs0PMsHXQU8tcvI+6LDZ73XEXCWnkgsNORCLe5Q==; kndctr_C4C6370453309C960A490D44_AdobeOrg_identity=CiYwNDYxMTE1OTE0MDU3NDM4Nzc4MDk0MjQ4MTM2NTI3MjA5MDk3MVIPCK2-7d2SMRgBKgRJUkwx8AGiqsfMlDE=; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19550%7CMCMID%7C04611159140574387780942481365272090971%7CMCAAMLH-1689761242%7C3%7CMCAAMB-1689761242%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689163642s%7CNONE%7CvVersion%7C5.2.0%7CMCAID%7CNONE; walmart.csrf=a52b11e07a9d6f82489ed5f6; DYN_USER_ID.ro=d281b476-c76e-4e40-a973-c4e54ca7c221; kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster=or2; s_visit=1; _4c_=%7B%22_4c_mc_%22%3A%22953624dc-9cf6-402c-8f09-732d5cd8ed0b%22%7D; headerType=whiteGM; _scid_r=43fb8521-6d07-45c0-9588-265ecf878adf; ENV=ak-scus-t1-prod; WM.USER_STATE=GUEST|Guest; xpm=1%2B1689160926%2BTCbjYc0dcz1gjlkzjAPUuI~%2B0; _cs_cvars=%7B%221%22%3A%5B%22appName%22%2C%22home-page%22%5D%7D; _cs_mk_aa=0.6492587868124717_1689160948275; gpv_Page=Home%20Page; cto_bundle=YkQaQF9SMG9peE1tMTJhNUFoY3ZXSDNmN1NscTJXempmdWlLa3BraUdZV0p0ZXgwSmVTJTJCUFRpWjlVeWpwNXBjemRLeW0lMkJJMTc2M1hSd0xmZGhUd2xtem4xaTAzd0Q1Z1gxaTJEZlRZUGExMzE3OGV5VlQyRU9Sb01jVTJKOTJESGhlMTglMkJVTk1WZiUyRiUyQmptdG5OdHJ4TnNmdTlnJTNEJTNE; cto_bundle=YkQaQF9SMG9peE1tMTJhNUFoY3ZXSDNmN1NscTJXempmdWlLa3BraUdZV0p0ZXgwSmVTJTJCUFRpWjlVeWpwNXBjemRLeW0lMkJJMTc2M1hSd0xmZGhUd2xtem4xaTAzd0Q1Z1gxaTJEZlRZUGExMzE3OGV5VlQyRU9Sb01jVTJKOTJESGhlMTglMkJVTk1WZiUyRiUyQmptdG5OdHJ4TnNmdTlnJTNEJTNE; s_gnr=1689161410296-Repeat; _uetsid=35cc59d01fb411eebd9d5d6a01871b51; _uetvid=592c90e01c0e11eea099f9a48ce269bf; authDuration={"lat":"1689161419388000","lt":"1689161419388000"}; _px3=516a7d42300601a17509e738a4329d4c8c0cad19231dea3a90482f5d5825ae88:kcgnYzWuFWiVlQvWCG4GWHinoyPrPRluEzLlklPfCNeE9RjU89++PMsMGTnlkNYAXyVPHjiFBBV7XPAEurkvOw==:1000:LTR3rgDU89CNFjHR7osRXns53NDfohRTyoXYpA+QPw9RTcLha2Jj0q6cf4AOldkv9/JBDnJY292yMs/+/x785z3LyM/63+g4ckAmbHoNofzU07bSLZmrORugHfjxHbpkz0cCnd8pVK/xn+ie9uJU3h713ZMXP+neqOoxfcB5NzJn4f8oGqXJr9rZTJxS7uhUH3fWLHAZFc277hDeOvQb0Q==; _cs_id=e1ac95a1-0405-a9ec-92cd-bb393f01aa8c.1688655868.17.1689161420.1689156379.1.1722819868293; _cs_s=19.0.0.1689163220959; seqnum=124; TS010110a1=0179207e645d561a89c0b4c4afab945905e0e7245cf39f502b0e450b6d496e95a9e759aba74206995518ba00c1b0b42552cfc65327; TS01ea8d4c=0179207e645d561a89c0b4c4afab945905e0e7245cf39f502b0e450b6d496e95a9e759aba74206995518ba00c1b0b42552cfc65327; TS0180da25=0179207e645d561a89c0b4c4afab945905e0e7245cf39f502b0e450b6d496e95a9e759aba74206995518ba00c1b0b42552cfc65327; TSe62c5f0d027=080d3e3cf5ab20003eed11cf3589ec1f6e6730745312bc5d8ff378aa8025d24d7ee927d1862c2ee608b4637616113000a849b61c8a65b6c3ca208c2a0aa5a615414b0db9589f9925339702041fefb576aedfad7878bccd3c98a8f13e2ea7eedc; bm_sv=E310C9353FFE376192B292F201AEC902~YAAQbzsvF4pD60SJAQAAzBLeSRQRRuFuUwbFucfYTstPEpJRWjct6h6cNiC7V71Guuny9ChWIs5dfz+05LjIT7mMbHGDr7h64xNu84x1BI7kkrAaEHUsK+bq/aJv6GjU0gfp08WVZ0V00P5xfHKAHGadcxyNoKUwQnMOpqfW3K05aLSl1SjNg9y/mt6kuQGbM/2BnzDpxXS1Ro4RT+4jruzm3L19J0kHfHsEPcgLz60FjZZKP5XyT1T3gKrgfZQ6Yh0=~1; _pxde=566ac3e31f62fd4ef32308d90b701790b7284e0f0d2be8fa707c27f0e9f4e547:eyJ0aW1lc3RhbXAiOjE2ODkxNjE0OTQ4Mjl9; bm_sv=E310C9353FFE376192B292F201AEC902~YAAQbzsvFxFe7ESJAQAA1yniSRS3bLtRYRH5i+IxKuX3eKmQyYZNv55w6AbSB+IbUVPuLEv7HfZDXPkLyTR8jqcutVmXOdks8Tcg+RVa75iXX0PcuvFS+OWOinbM5vrqXVMycluiEY2OXq3ZX3oG4bMma0SaACkrAKASkivOMh/MeV6alr77WLus64oFmnuhBNVD+lmgbuNeQkW5P7x5WE54KQKywq2GHNYMr2Dtw7TZJqVrMjzP9AR7+bHHXS0rKww=~1; vtc=TCbjYc0dcz1gjlkzjAPUuI; walmart.nearestLatLng="43.60822,-79.69387"; walmart.nearestPostalCode=L5V2N6',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    Reviews_headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://www.walmart.ca',
        'Pragma': 'no-cache',
        'Referer': 'https://www.walmart.ca/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    category = ""

    def start_requests(self):
        links = read_links_from_csv("links.csv")
        for link in links[5:6]:
            print(link)
            list_link = link.get('Link')
            self.category = link.get('Name')
            print(list_link)
            yield scrapy.Request(url=list_link, headers=self.headers, callback=self.brows_cat)

    def brows_cat(self, response):
        product_page_urls = response.xpath('//*[@class="css-3ky18c epettpn0"]/a/@href').getall()
        cat_urls = response.xpath('//*[@class="eaue1ee0 css-xhyxqw elkyjhv0"]/@href').getall()
        if not cat_urls:
            for cat_url in cat_urls[:1]:
                print(cat_url)
                yield response.follow(url=cat_url, headers=self.headers, callback=self.brows_cat)
        else:
            for product_page in product_page_urls[:1]:
                print(product_page)
                yield response.follow(url=product_page, headers=self.headers, callback=self.product_info_scrape)

        next_page_url = response.xpath('//*[@data-automation="pagination-next-button"]/@href').get()
        if next_page_url:
            yield response.follow(url=next_page_url, headers=self.headers, callback=self.brows_cat)

    def product_info_scrape(self, response):
        print("in parse info function")
        product_images_url = []
        item = dict()
        regex = r'window\.__PRELOADED_STATE__=(.*?)(?=</script>)'
        match = re.search(regex, response.text, re.DOTALL).group().strip("window.__PRELOADED_STATE__=").strip(";")
        response_json = json.loads(match)
        product_info = response_json.get("product")
        product_specs = response_json.get('entities').get('skus').get(product_info.get('activeSkuId'))
        product_sku = product_info.get('activeSkuId')
        product_id = product_info.get('item').get('id')
        longDesc = product_specs.get('longDescription')
        shortDesc = product_specs.get('description')
        product_name = product_specs.get('name')
        productCategory = product_specs.get('categories')[0].get('displayName')
        upc = product_specs.get('upc')[0]
        product_images_list = product_specs.get('images')
        for thumbnail in product_images_list:
            product_image = thumbnail.get("enlarged").get("url").split('?')[0]

            product_images_url.append(product_image)

        item["Product_name"] = product_name
        item["LongDesc"] = longDesc
        item["ShortDesc"] = shortDesc
        item["image_urls"] = product_images_url
        item["ProductCategory"] = productCategory
        item["UPC"] = upc
        item["ID"] = product_id
        item["SKU"] = product_sku
        price_api_payload = self.price_payload_editor(product_id, product_sku)
        yield scrapy.Request(url="https://www.walmart.ca/api/product-page/v4/price-offer", method="POST",
                             body=price_api_payload, headers=self.headers, callback=self.scrape_price,
                             meta={"item": item})

    def scrape_price(self, response):
        print("in price scrapping function")
        item = response.meta["item"]
        json_data = json.loads(response.body)
        skus = json_data.get("skus").get(item["SKU"])
        offers = json_data.get("offers")
        if offers:
            current_price = offers.get(skus[0]).get("currentPrice")
            item['current_price'] = f'${current_price}'
            print(f'name: {item["Product_name"]},"price":{item["current_price"]}')
        # write_custom_csv(item, self.category)
        offset = 0
        reviewPage_url = create_url(item["ID"], offset)
        print(reviewPage_url)
        yield scrapy.Request(url=reviewPage_url, headers=self.Reviews_headers, callback=self.scrape_reviews,
                             meta={"review_list": [], "item": item, "offset": offset})

    def scrape_reviews(self, response):

        review_dic = {}
        item = response.meta["item"]
        offset = response.meta["offset"]
        offset += 6
        check = False
        review_list = response.meta["review_list"]
        if response:
            json_response = json.loads(response.body)
            results = json_response.get('Results')
            if len(results) >= 1:
                for review in results:
                    review_dic['Title'] = review.get('Title')
                    review_dic['ReviewText'] = review.get('ReviewText')
                    review_dic['UserNickname'] = review.get('UserNickname')
                    review_dic['Rating'] = review.get('Rating')

                    review_list.append(review_dic)
                    check = True
                reviewPage_url = create_url(item["ID"], offset)
                yield scrapy.Request(url=reviewPage_url, headers=self.Reviews_headers, callback=self.scrape_reviews,
                                     meta={"review_list": review_list, "item": item, "offset": offset})
        if check:
            item["reviews"] = review_list
        write_dict_to_json_file(self.category, item)
        yield item


def read_links_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        return list(csv.DictReader(csvfile))


def write_dict_to_json_file(path, item_dictionary):
    try:
        with open(path, 'r+') as json_file:
            file_data = json.load(json_file)
            file_data.append(item_dictionary)
            json_file.seek(0)
            json.dump(file_data, json_file, indent=4)
            json_file.truncate()
        print(f"Dictionary appended to JSON file '{path}' successfully.")
    except FileNotFoundError:
        with open(path, 'w') as json_file:
            json.dump([item_dictionary], json_file, indent=4)
        print(f"JSON file '{path}' created successfully with the dictionary.")


def create_url(ID, offset):
    return f"https://api.bazaarvoice.com/data/reviews.json?resource=reviews&action=REVIEWS_N_STATS&filter=productid%3Aeq%3A{ID}&filter=contentlocale%3Aeq%3Aen_CA%2Cen_GB%2Cen_US%2Cen_CA&filter=isratingsonly%3Aeq%3Afalse&filter_reviews=contentlocale%3Aeq%3Aen_CA%2Cen_GB%2Cen_US%2Cen_CA&include=authors%2Cproducts&filteredstats=reviews&Stats=Reviews&limit=6&offset={offset}&sort=submissiontime%3Adesc&passkey=e6wzzmz844l2kk3v6v7igfl6i&apiversion=5.5&displaycode=2036-en_ca"
