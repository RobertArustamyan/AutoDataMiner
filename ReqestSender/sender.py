import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = '/home/robert/Applications/firefox-127.0b6/firefox/firefox-bin'
service = Service('/usr/bin/geckodriver')

driver = webdriver.Firefox(service=service, options=options)

class Sender:
    def __init__(self):
        self.pureUrl = 'https://auto.am/'
        self.searchUrlTemplate = 'https://auto.am/search/all?q={{"category":"51","page":"{page}","sort":"latest","layout":"list","user":{{"dealer":"0","official":"0","id":""}},"year":{{"gt":"1911","lt":"2025"}},"usdprice":{{"gt":"0","lt":"100000000"}},"mileage":{{"gt":"10","lt":"1000000"}}}}'

    def getPageHtml(self,page):
        searchPageUrl = self.searchUrlTemplate.format(page=page)
        driver.get(searchPageUrl)
        pageHtml = driver.page_source
        return pageHtml

    @staticmethod
    def getCardsLinks(pageHtml):
        if not pageHtml:
            raise ValueError("The pageHtml parameter is empty or None.")

        try:
            soup = BeautifulSoup(pageHtml, 'lxml')
            searchResultDiv = soup.find('div', id='search-result')
            pageOffers = searchResultDiv.find_all('a', href=True)
            offersLinks = list(set(a['href'] for a in pageOffers if '/offer/' in a['href']))
            return offersLinks

        except Exception as e:
            print(f"An error occurred while parsing the page: {e}")
            return []

if __name__ == '__main__':
    sender = Sender()
    sender.getCardsLinks(sender.getPageHtml(1))
