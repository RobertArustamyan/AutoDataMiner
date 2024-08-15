import requests
from bs4 import BeautifulSoup
import json
import os
from DataStructures.VehicleObject import Vehicle
import concurrent.futures
import csv
from datetime import datetime

class Sender:

    def __init__(self):
        self.pureUrl = 'https://auto.am'
        self.searchUrl = 'https://auto.am/search'
        self.cookies = {
            '_ga_FP90EBRFYF': 'GS1.1.1723745309.35.1.1723745339.30.0.1575909923',
            '_ga': 'GA1.1.1676492422.1722873823',
            '_ym_uid': '1722873824559707672',
            '_ym_d': '1722873824',
            '_fbp': 'fb.1.1722873825429.177400002601892586',
            'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IlYzbnRGTVNObkNCZUVCSzU4UmxGVUE9PSIsInZhbHVlIjoiaXNvQk05a3pOTjlSdVd5TW5WOWkydHJSSHR1SUdVVklYa3pvb3Zqdk00b3dtTk5KYm1nYnYzSFNcL1M5UHJGdUJta0dCQUR0bU5nU0pqVEE0SEprc3duY29cL0NmVFAwV2szdTE5NlR1dXNkWEdpcGE2WFhtTU0wRmlkTXJJKzZWeWVManN1TG0yM240b3Q3bmxGckY5RGIwTTFPUEVPK0djXC9rcEZ4Q2pjdGs5MmhkRkRiUFhDb3ZPUGNhN0ZjWGQ5QmwrTzlET0kyQVQzTU1zRnVWVDlQXC9YK3ZTTkh4djNjNUlkcm5UT2krdkE9IiwibWFjIjoiZTFjZmQxNzU4Y2U5NWMwZDU0Mjk2ZGQyOGZiYjI4Y2YwMGEwN2UyOWNjMzNiZWM4NWRmMGU2MDA0YWExZjg3NiJ9',
            '_gid': 'GA1.2.420357243.1723293346',
            '_ym_isad': '2',
            'XSRF-TOKEN': 'eyJpdiI6IlNFOXJFMm41UXdHQjFocVhDak5HdHc9PSIsInZhbHVlIjoiTURqa1VJOXJHaUVsUEVpY09lM3ZuQU5MR2xvZlwvQThhNDdhWndyTFlMcHNQMEhwZmx6UU1mZ2ZiSjg1Ulwvd1FhWDg4bnU2VnpNK25mbDNYOW1WTDYzMnNXN3lkZ1l3aUR0S3RKaFwvSFhaN3Z2VTVaTm13M0I0eDd5ZTVodjJQXC9KIiwibWFjIjoiNTc3YWM4ZTgyNDJkODkwZmNjMGEwMDNkMjlhYmVkZDg1OThlNmYwMzE4YmQ3NjBmMTk5ZTExNTA3MThhMzc5NSJ9',
            'autoam_session': 'eyJpdiI6IkFwVzNoR1VxdU1ONWF3XC9JdElUV3lRPT0iLCJ2YWx1ZSI6InAwQUhoU0RFd1phM3F2RmFxVGRiSTR1bnhNMjVnZFVNS0pneklyQVp2dXRIZVJPeVFnOStIOFUrbGUxR1BrdWgzZ2tqVEZDOWN0c1NhWHZiQnM3WXVmZmZNc3B0SUZON0NMXC9PNFh1ZDl6UnFXVDdNRWd1TG50Z0F1WUdNVGtnNSIsIm1hYyI6IjMxMDcxY2EzM2EzMjE0ZjZmOWM5NzNmMDE2OGYwOWMzYjZlOTE3MzYxMTNiNjczYjBjMTFhYzJjMWRhNTdhOWMifQ%3D%3D',
            '_ym_visorc': 'w',
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRF-Token': '4fsLYUU3eh9NgDKstk3QbdoFDewSFbazCAioDfy6',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://auto.am',
            'Connection': 'keep-alive',
            'Referer': 'https://auto.am/search/all?q={%22category%22:%2251%22,%22page%22:%221%22,%22sort%22:%22latest%22,%22layout%22:%22list%22,%22user%22:{%22dealer%22:%220%22,%22official%22:%220%22,%22id%22:%22%22},%22year%22:{%22gt%22:%221911%22,%22lt%22:%222025%22},%22usdprice%22:{%22gt%22:%220%22,%22lt%22:%22100000000%22},%22mileage%22:{%22gt%22:%2210%22,%22lt%22:%221000000%22}}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

    def getPageHtml(self, page):
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

    @staticmethod
    def getCardData(cardHtml):
        vehicle = Vehicle()
        vehicle = vehicle.createObject(cardHtml)
        return vehicle

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

    def processCards(self, page):
        pageHtml = self.getPageHtml(page)
        cardLinks = self.getCardsLinks(pageHtml)

        def processSingleCard(cardLink):
            cardHtml = self.getCardHtml(cardLink)
            return self.getCardData(cardHtml)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            parsedPageData = list(executor.map(processSingleCard, cardLinks))

        return parsedPageData

    @staticmethod
    def saveData(parsedPageData,filename='../vehicles_data.csv'):
        keys = parsedPageData[0].__dict__.keys()
        file_exists = os.path.isfile(filename)

        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)

            if not file_exists:
                writer.writeheader()

            for vehicle in parsedPageData:
                writer.writerow(vehicle.__dict__)


    def getAllData(self):
        for i in range(1, 200):
            print(f'Page {i} started {datetime.now()}')
            processedData = self.processCards(i)
            print(f'Page {i} finished {datetime.now()}')
            self.saveData(processedData)


if __name__ == '__main__':
    sender = Sender()
    sender.getAllData()

