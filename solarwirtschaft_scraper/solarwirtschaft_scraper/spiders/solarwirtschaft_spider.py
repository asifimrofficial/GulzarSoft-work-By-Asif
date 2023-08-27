import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class SolarwirtschaftSpiderSpider(scrapy.Spider):
    name = "solarwirtschaft_spider"
    allowed_domains = ["www.solarwirtschaft.de"]
    start_urls = ["https://www.solarwirtschaft.de/unsere-mitglieder/mitgliedersuche/"]
    driver = None
    custom_settings = {'ROBOTSTXT_OBEY': False,
                       'RETRY_TIMES': 5,
                       'FEED_URI': 'output/solar_wirtschaft_v3.xlsx',
                       'FEED_FORMAT': 'xlsx',
                       'FEED_EXPORTERS': {'xlsx': 'scrapy_xlsx.XlsxItemExporter'},
                       # 'FEED_EXPORT_FIELDS': [''],
                       # 'DOWNLOAD_DELAY': 1
                       }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def parse(self, response, **kwargs):
        artical_links = response.xpath('//a[@class="article__link"]/@href').getall()
        next_page_link = response.xpath('//a[contains(@class,"page-next")]/@href').get()
        for artical_link in artical_links:
            self.driver.get(artical_link)
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'_brlbs-btn-accept-all')]"))).click()
            except:
                pass
            response = self.driver.page_source
            response = scrapy.Selector(text=response)
            item = self.scrape_artical_data(response)
            item['Detail Page Url'] = artical_link
            yield item

        if next_page_link:
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def scrape_artical_data(self, response):
        item = dict()
        item['Company name'] = response.xpath('//h2[@class="item__headline"]/text()').get('').strip()
        item['Street/No'] = response.xpath('//li[contains(@class,"streetname")]/text()').get('').strip()
        item['Postal Code'] = response.xpath('//li[contains(@class,"zipcode")]/text()').get('').strip()
        item['City'] = response.xpath('//li[contains(@class,"city")]/text()').get('').strip()
        item['Country'] = response.xpath('//li[contains(@class,"country")]/text()').get('').strip()
        item['Phone'] = response.xpath('//li[contains(@class,"phonenumber")]/a/text()').get('').strip()
        item['Email'] = response.xpath('//li[contains(@class,"email")]/a/text()').get('').strip()
        return item

# def email_decoder(encoded_email):
#     print(encoded_email)
#     decoded_email = ""
#     for char in encoded_email:
#         if char.isalpha():
#             shift = 13 if char.islower() else 13
#             decoded_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a')) if char.islower() else chr(
#                 (ord(char) - shift - ord('A')) % 26 + ord('A'))
#             decoded_email += decoded_char
#         elif char.isdigit():
#             decoded_email += chr((ord(char) - 5 - ord('0')) % 10 + ord('0'))
#         else:
#             decoded_email += char
#     print(decoded_email)
#     return decoded_email
