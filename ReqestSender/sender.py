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
            'XSRF-TOKEN': 'eyJpdiI6Im9XZk9senVyUHg5V3g0V3ZheGNXa1E9PSIsInZhbHVlIjoid2hqNG5mVTJ6S2FBQU1LXC9vVGpOeFM2VVVqbDBDMjl6dURhRXMyNkFSbDFMQkU2RlpsREhET3hLTHRiUzZueVdJWlpxVk1CeVpiMERRakdJNkZ1aXduTE9cL0V6YVlkNklsTUkwd1pvWXgrNzZKVnhvU0NZWCtOdXB4ZUJTOHVweCIsIm1hYyI6IjkwNWExYTM5ZGIzNjcxYTY5YWNmM2U3NTc5NGFlYjYyOTA3NGJjNDZmNmJjYWQ3YWU3NmNmMjllY2Q5ODQyYTkifQ%3D%3D',
            'autoam_session': 'eyJpdiI6IkRlNDdOM0VWMmZoZWJNWlQzY2tOeUE9PSIsInZhbHVlIjoid3NMV2JuQlRmSjJHM09ZTGtQR3VcL3pURUhvUFNHNFh1VURFdDVJejZrQm5PdG1KNkJKMXRKZHVVeHlCbjczVEhiK0loRVNSb3FpVENDblQwWWU4cHZIblBpWHp5bjlnT2ZhNk04anB1Z1hcL0tmYzg2a3kxeGxNa0Z1aWd6dlpUcSIsIm1hYyI6IjMxYWNjMTQzMGNkNGU0MDBjYjRiZWM0NGJlMzcyOTk0Y2MxMWM2NWJkMzdmZWU4MmRjNjA4ZWZjNWZhMDg1YTYifQ%3D%3D',
            '_ga_FP90EBRFYF': 'GS1.1.1723790521.1.1.1723790543.38.0.1243323666',
            '_ga': 'GA1.1.2097262647.1723790521',
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRF-Token': 'aa3PoLkvcvG1AMwQMkFxfYz1FvrEmHpRhB03wAi4',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://auto.am',
            'DNT': '1',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://auto.am/search/all?q=%7B%22category%22%3A%221%22%2C%22year%22%3A%7B%22gt%22%3A%221911%22%2C%22lt%22%3A%222025%22%7D%2C%22usdprice%22%3A%7B%22gt%22%3A%220%22%2C%22lt%22%3A%22100000000%22%7D%7D',
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
    def getCardData(cardHtml,cardUrl):
        vehicle = Vehicle()
        vehicle = vehicle.createObject(cardHtml,cardUrl)
        #vehicle.showObject()
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
            return self.getCardData(cardHtml,cardLink)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            parsedPageData = list(executor.map(processSingleCard, cardLinks))

        return parsedPageData

    @staticmethod
    def saveData(parsedPageData,filename='vehicles_data.csv'):
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

