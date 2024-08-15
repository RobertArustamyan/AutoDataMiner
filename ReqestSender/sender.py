import requests
from bs4 import BeautifulSoup
import json
from DataStructures.VehicleObject import Vehicle

class Sender:

    def __init__(self):
        self.pureUrl = 'https://auto.am'
        self.searchUrl = 'https://auto.am/search'
        self.cookies = {
            '_ga_FP90EBRFYF': 'GS1.1.1723708277.33.1.1723709962.7.0.1578253137',
            '_ga': 'GA1.1.1676492422.1722873823',
            '_ym_uid': '1722873824559707672',
            '_ym_d': '1722873824',
            '_fbp': 'fb.1.1722873825429.177400002601892586',
            'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IlYzbnRGTVNObkNCZUVCSzU4UmxGVUE9PSIsInZhbHVlIjoiaXNvQk05a3pOTjlSdVd5TW5WOWkydHJSSHR1SUdVVklYa3pvb3Zqdk00b3dtTk5KYm1nYnYzSFNcL1M5UHJGdUJta0dCQUR0bU5nU0pqVEE0SEprc3duY29cL0NmVFAwV2szdTE5NlR1dXNkWEdpcGE2WFhtTU0wRmlkTXJJKzZWeWVManN1TG0yM240b3Q3bmxGckY5RGIwTTFPUEVPK0djXC9rcEZ4Q2pjdGs5MmhkRkRiUFhDb3ZPUGNhN0ZjWGQ5QmwrTzlET0kyQVQzTU1zRnVWVDlQXC9YK3ZTTkh4djNjNUlkcm5UT2krdkE9IiwibWFjIjoiZTFjZmQxNzU4Y2U5NWMwZDU0Mjk2ZGQyOGZiYjI4Y2YwMGEwN2UyOWNjMzNiZWM4NWRmMGU2MDA0YWExZjg3NiJ9',
            '_gid': 'GA1.2.420357243.1723293346',
            'XSRF-TOKEN': 'eyJpdiI6IndUK2VSSE1WXC9sdWFSUUdVMmpiSDVRPT0iLCJ2YWx1ZSI6Im92bHNKaitwXC9cL21RRzlhdnFPcFNNWlUwSjhXaFVzM0RlOWcxaURpTFJoWngrMDVrYVRFS3h3RFRrTkNGK1R6RHdTNjVERjJkNjVnclUyRERGZUJxcE1LTG1ZcWRJOFBjbXJxUGd0Q2t6eFlTMUF2d0N3OGpNKzY5eWZ6d3JDNjkiLCJtYWMiOiI0MzZjMmRlZGI5YTMzMjY4NWNhNzYyNWVmMmRiOWU5MWY2ZWU2OGNlZjQ1MDFmZjkyMGQwYmQxZjRjODJkMzg2In0%3D',
            'autoam_session': 'eyJpdiI6Ik91ZDliRmhSbmowRno5WWV4ajNlUmc9PSIsInZhbHVlIjoiRENNSTIyemtvRXFJdWxIZytpY2hOQnh3R1I2bzU5c2hhelB3NnQ2emRKXC9Ya2xvUVZGSmxRYnpIS1ZnVlI0UXBJcVdKTjFrVDMzTXc1YWJyTTFqa0p2N0kzdkNMaFwvWDNxWWlWRjU5K3NidW1oaTBMOUhkK2tUZ1F4cXVzbzVhTSIsIm1hYyI6IjUyM2Q1ZTVmZjM1Yzc1OWEzOTI1NzJlMjU4YjU1YWNjNjY5MjJjZjM0ZmY2MDY2MjBlZjJhNmVjNmI1MTZmZGUifQ%3D%3D',
            '_ym_isad': '2',
            '_ym_visorc': 'b',
            'cf_use_ob': '0',
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRF-Token': 'F9gl0OhDGC60gAvAfoBhWWOp5RmnxBhVM5RstGNS',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://auto.am',
            'Connection': 'keep-alive',
            'Referer': 'https://auto.am/search/all?q={%22category%22:%2251%22,%22page%22:%221%22,%22sort%22:%22latest%22,%22layout%22:%22list%22,%22user%22:{%22dealer%22:%220%22,%22official%22:%220%22,%22id%22:%22%22},%22year%22:{%22gt%22:%221911%22,%22lt%22:%222025%22},%22usdprice%22:{%22gt%22:%220%22,%22lt%22:%22100000000%22},%22mileage%22:{%22gt%22:%2210%22,%22lt%22:%221000000%22}}',
            # 'Cookie': '_ga_FP90EBRFYF=GS1.1.1723708277.33.1.1723709962.7.0.1578253137; _ga=GA1.1.1676492422.1722873823; _ym_uid=1722873824559707672; _ym_d=1722873824; _fbp=fb.1.1722873825429.177400002601892586; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlYzbnRGTVNObkNCZUVCSzU4UmxGVUE9PSIsInZhbHVlIjoiaXNvQk05a3pOTjlSdVd5TW5WOWkydHJSSHR1SUdVVklYa3pvb3Zqdk00b3dtTk5KYm1nYnYzSFNcL1M5UHJGdUJta0dCQUR0bU5nU0pqVEE0SEprc3duY29cL0NmVFAwV2szdTE5NlR1dXNkWEdpcGE2WFhtTU0wRmlkTXJJKzZWeWVManN1TG0yM240b3Q3bmxGckY5RGIwTTFPUEVPK0djXC9rcEZ4Q2pjdGs5MmhkRkRiUFhDb3ZPUGNhN0ZjWGQ5QmwrTzlET0kyQVQzTU1zRnVWVDlQXC9YK3ZTTkh4djNjNUlkcm5UT2krdkE9IiwibWFjIjoiZTFjZmQxNzU4Y2U5NWMwZDU0Mjk2ZGQyOGZiYjI4Y2YwMGEwN2UyOWNjMzNiZWM4NWRmMGU2MDA0YWExZjg3NiJ9; _gid=GA1.2.420357243.1723293346; XSRF-TOKEN=eyJpdiI6IndUK2VSSE1WXC9sdWFSUUdVMmpiSDVRPT0iLCJ2YWx1ZSI6Im92bHNKaitwXC9cL21RRzlhdnFPcFNNWlUwSjhXaFVzM0RlOWcxaURpTFJoWngrMDVrYVRFS3h3RFRrTkNGK1R6RHdTNjVERjJkNjVnclUyRERGZUJxcE1LTG1ZcWRJOFBjbXJxUGd0Q2t6eFlTMUF2d0N3OGpNKzY5eWZ6d3JDNjkiLCJtYWMiOiI0MzZjMmRlZGI5YTMzMjY4NWNhNzYyNWVmMmRiOWU5MWY2ZWU2OGNlZjQ1MDFmZjkyMGQwYmQxZjRjODJkMzg2In0%3D; autoam_session=eyJpdiI6Ik91ZDliRmhSbmowRno5WWV4ajNlUmc9PSIsInZhbHVlIjoiRENNSTIyemtvRXFJdWxIZytpY2hOQnh3R1I2bzU5c2hhelB3NnQ2emRKXC9Ya2xvUVZGSmxRYnpIS1ZnVlI0UXBJcVdKTjFrVDMzTXc1YWJyTTFqa0p2N0kzdkNMaFwvWDNxWWlWRjU5K3NidW1oaTBMOUhkK2tUZ1F4cXVzbzVhTSIsIm1hYyI6IjUyM2Q1ZTVmZjM1Yzc1OWEzOTI1NzJlMjU4YjU1YWNjNjY5MjJjZjM0ZmY2MDY2MjBlZjJhNmVjNmI1MTZmZGUifQ%3D%3D; _ym_isad=2; _ym_visorc=b; cf_use_ob=0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

    def getPageHtml(self,page):
        search = {
            'search': json.dumps({
                'category': '51',
                'page': page,
                'sort': 'latest',
                'layout': 'list',
                'user': {
                    'dealer': '0',
                    'official': '0',
                    'id': ''
                },
                'year': {
                    'gt': '1911',
                    'lt': '2025'
                },
                'usdprice': {
                    'gt': '0',
                    'lt': '100000000'
                },
                'mileage': {
                    'gt': '10',
                    'lt': '1000000'
                }
            })
        }

        response = requests.post(
            url=self.searchUrl,
            headers=self.headers,
            cookies=self.cookies,
            data=search
        )
        if response.status_code == 200:
            return response.text
        else:
            raise ValueError("Invalid Response Status code in getPageHtml")

    def getCardHtml(self, offerLink):
        cardUrl = self.pureUrl + offerLink
        response = requests.get(cardUrl)
        if response.status_code == 200:
            return response.text
        else:
            raise ValueError("Invalid Response Status code in gertCardHtml")
    def getCardData(self, cardHtml):
        vehicle = Vehicle()
        vehicle.createObject(cardHtml)

    @staticmethod
    def getCardsLinks(pageHtml):
        if not pageHtml:
            raise ValueError("The pageHtml parameter is empty or None.")

        try:
            soup = BeautifulSoup(pageHtml, 'lxml')
            pageOffers = soup.find_all('a', href=True)
            offersLinks = list(set(a['href'] for a in pageOffers if '/offer/' in a['href']))
            return offersLinks

        except Exception as e:
            print(f"An error occurred while parsing the page: {e}")
            return []

if __name__ == '__main__':
    sender = Sender()
    links = sender.getCardsLinks(sender.getPageHtml(1))
    for link in links:
        sender.getCardData(sender.getCardHtml(link))
    links = sender.getCardsLinks(sender.getPageHtml(3))
    for link in links:
        sender.getCardData(sender.getCardHtml(link))
    links = sender.getCardsLinks(sender.getPageHtml(2))
    for link in links:
        sender.getCardData(sender.getCardHtml(link))

