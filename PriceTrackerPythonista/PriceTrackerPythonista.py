import requests
from bs4 import BeautifulSoup
import time

class PriceTracker:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    def check_price(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id="productTitle").get_text().strip()
        price = soup.find(id="priceblock_ourprice").get_text()
        converted_price = float(price.replace('R$', '').replace(',', '.').strip())

        return title, converted_price

    def run(self):
        title, price = self.check_price()
        print(f"Product: {title}\nCurrent Price: R$ {price}")

if __name__ == "__main__":
    URL = "https://www.amazon.com.br/Lava-Lou\u00E7as-Electrolux-LL08S-Servi\u00E7os-Inox/dp/B084Q84ZXV"
    tracker = PriceTracker(URL)
    tracker.run()
