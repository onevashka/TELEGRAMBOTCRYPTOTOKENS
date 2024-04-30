import requests
from bs4 import BeautifulSoup
import fake_useragent




user_agent = fake_useragent.UserAgent().random

headers = {

        "user_agent" : user_agent

        }


url = "https://cryptorank.io/all-coins-list"




async def get_price(name_token):

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.select(".sc-22c1b09c-0.fziBJN")[0]
    trs = table.select("tr")[1:]

    for tr in trs:
        if tr.select_one(".sc-50f3633f-0.fFBbnm").text == name_token:
            price = tr.select_one(".sc-50f3633f-0.sc-28f598be-1.kCCAmd.nZrBG").text
            return str(price)
        



