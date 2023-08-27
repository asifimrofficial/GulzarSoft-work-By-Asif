import csv
import re
from copy import deepcopy

import scrapy


class GlflamasonSpiderSpider(scrapy.Spider):
    name = "glflamason_spider"
    allowed_domains = ["lodges.glflamason.org"]
    start_urls = ["https://lodges.glflamason.org/public/Lodge-Search"]
    headers = {
        'authority': 'lodges.glflamason.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'ASP.NET_SessionId=kl12g1kw35emddzgqgkzbom4',
        'origin': 'https://lodges.glflamason.org',
        'pragma': 'no-cache',
        'referer': 'https://lodges.glflamason.org/public/Lodge-Search',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }
    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': "",
        '__VIEWSTATEGENERATOR': "",
        '__EVENTVALIDATION': "",
        'ctl00$ContentPlaceHolder1$HiddenFieldLatitude': '',
        'ctl00$ContentPlaceHolder1$HiddenFieldLongitude': '',
        'ctl00$ContentPlaceHolder1$MyAccordion_AccordionExtender_ClientState': '3',
        'ctl00$ContentPlaceHolder1$_content$TextBoxSearchAddress': '',
        'ctl00$ContentPlaceHolder1$_content$TBWE2_ClientState': '',
        'ctl00$ContentPlaceHolder1$AccordionPane1_content$TextBoxSearchCity': '',
        'ctl00$ContentPlaceHolder1$AccordionPane1_content$TextBoxWatermarkExtender1_ClientState': '',
        'ctl00$ContentPlaceHolder1$AccordionPane2_content$TextBoxSearchLodgeNumber': '',
        'ctl00$ContentPlaceHolder1$AccordionPane2_content$TextBoxWatermarkExtender2_ClientState': '',
        'ctl00$ContentPlaceHolder1$AccordionPane3_content$TextBoxSearchZip': "",
        'ctl00$ContentPlaceHolder1$AccordionPane3_content$TextBoxWatermarkExtender3_ClientState': '',
        'ctl00$ContentPlaceHolder1$AccordionPane3_content$ButtonSearchZip': 'Search',
        'ctl00$ContentPlaceHolder1$AccordionPane5_content$TextBoxSearchDistrict': '',
        'ctl00$ContentPlaceHolder1$AccordionPane5_content$TextBoxWatermarkExtender4_ClientState': '',
        'ctl00$ContentPlaceHolder1$AccordionPane6_content$TextBoxSearchCounty': '',
        'ctl00$ContentPlaceHolder1$AccordionPane6_content$TextBoxWatermarkExtender5_ClientState': '',
        'ctl00$ContentPlaceHolder1$AccordionPane4_content$TextBoxSearchName': '',
        'ctl00$ContentPlaceHolder1$AccordionPane4_content$TextBoxWatermarkExtender6_ClientState': '',
    }

    def parse(self, response):

        yield scrapy.Request(url=self.start_urls[0], method="POST", headers=self.headers,
                             callback=self.fetch_form_data)

    def fetch_form_data(self, response):
        zip_codes = read_zip_codes_from_csv('input.csv')
        for zip_code in zip_codes:
            event_validation = response.xpath("//*[@id='__EVENTVALIDATION']/@value").get()
            view_state = response.xpath("//*[@id='__VIEWSTATE']/@value").get()
            data = deepcopy(self.data)
            data['__VIEWSTATE'] = view_state
            data['__EVENTVALIDATION'] = event_validation
            data['ctl00$ContentPlaceHolder1$AccordionPane3_content$TextBoxSearchZip'] = zip_code

            yield scrapy.FormRequest(url=response.url, formdata=data, method='POST', headers=self.headers,
                                     callback=self.scrape_detail_page_link)

    def scrape_detail_page_link(self, response):
        detail_page_link = response.xpath("//*[contains(@id,'_HyperLinkLodge')]/@href").get()
        yield response.follow(url=detail_page_link, headers=self.headers, callback=self.scrape_details)

    def scrape_details(self, response):
        glflamason_data = {}
        lodge_officers_list = []
        lodge_officers_dic = {}
        # Lodge Address Data Collection
        lodge_address_list = response.xpath("//span[contains(@id,'LabelInfo1')]//text()").getall()
        previous_key = None
        for item in lodge_address_list:
            split_data = item.split(':')
            if len(split_data) >= 2:
                key = split_data[0].strip(' \xa0')
                value = split_data[1].strip(' \xa0')
                glflamason_data[key] = value
                previous_key = key
            elif previous_key is not None:
                glflamason_data[previous_key] += item.strip(' \xa0')
        email = response.css('a[id*="HyperLinkEmailLodge"]::attr(href)').get('')
        glflamason_data['email'] = \
            response.css('a[id*="HyperLinkEmailLodge"]::attr(href)').get('').split(':')[1].split('?')[0]
        glflamason_data['phone number'] = response.css("span[id*='LabelInfo2']::text").get('').split(':')[1].strip(
            '\xa0')
        meetings = response.xpath("//span[contains(@id,'LabelInfo3')]/text()").getall()
        for meeting in meetings:
            if 'Meeting Time' in meeting:
                glflamason_data['meeting time '] = meeting.split('Time:')[1].strip('\xa0')
            elif 'Lodge Meetings' in meeting:
                glflamason_data['meeting'] = \
                    meeting.split(':')[1].strip('\xa0')
        glflamason_data['direction'] = response.css("a[id*='Directions']::attr(href)").get('')
        table_rows = response.css('[id*="GridViewOfficers"] tr')
        # Lodge Officers Data Collection
        for row in table_rows[1:]:
            lodge_officers_dic['title'] = row.xpath(".//td[1]/text()").get('').strip()
            lodge_officers_dic['first name'] = row.xpath(".//td[2]/text()").get('').strip()
            lodge_officers_dic['last name'] = row.xpath(".//td[3]/text()").get('').strip()
            lodge_officers_dic['officer phone'] = row.xpath(".//td[4]/text()").get('').strip().replace('-', '')
            lodge_officers_dic['officer email'] = row.xpath(".//td[5]/a/@href").get('').lstrip('mailto:')
            lodge_officers_list.append(lodge_officers_dic)
        glflamason_data['Lodge Officers Data'] = lodge_officers_dic
        # Lodge Members Statistics
        members_statistics_list = response.css("[id*='LabelStats']::text").getall()
        for item in members_statistics_list:
            key = item.split(':')[0].strip()
            value = item.split(':')[1].strip()
            glflamason_data[key] = value
        # District Deputy Grand Master details
        data = response.css("[id*='LabelDDGM']::text").getall()
        glflamason_data['deputy_GM name'] = data[0]
        glflamason_data['deputy_GM phone'] = re.sub("\D", '', data[1])
        glflamason_data['deputy_GM email'] = response.css("[id*='LabelDDGM'] a::text").get()
        # District Deputy Grand Master details
        data = response.css("[id*='LabelDI'] a::text").get()
        glflamason_data['DI_name'] = data[0]
        glflamason_data['DI_phone'] = re.sub("\D", '', data[1])
        glflamason_data['DI_email'] = response.css("[id*='LabelDI'] a::text").get()

        glflamason_data['detail page url'] = response.url
        yield glflamason_data


def read_zip_codes_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        return [row['zip codes'] for row in csv.DictReader(csvfile)]
