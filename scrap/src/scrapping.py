import requests
from bs4 import BeautifulSoup
from utils import regex_price

class KambistaScrap:
    def __init__(self, url):
        self.url = url

    def extract(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return {
            "buy": float(soup.find(id="valcompra").text),
            "sell": float(soup.find(id="valventa").text)
        }


class RextieScrap:
    def __init__(self, url):
        self.url = url
    def extract(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        buy_section = soup.find_all("div", class_="buy")


class CambioSeguroScrap:
    def __init__(self, url):
        self.url = url

    def extract(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        section = soup.find("ul", class_="info-tasas").find_all("li", class_="use_hover")
        buy, sell = [float(regex_price(c.text)) for c in section]
        return {
            "buy": buy,
            "sell": sell
        }