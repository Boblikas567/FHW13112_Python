import requests
from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
soup = BeautifulSoup(response.text, features='html.parser')

usd = soup.find(string="USD").find_parent("tr")
rate = usd.find("td", {"data-label": "Офіційний курс"}).text
print(rate)