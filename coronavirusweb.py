# imports
import requests
import json
from bs4 import BeautifulSoup

# base url for the data
_url = 'https://www.worldometers.info/coronavirus/'


# Helper function
def text(el: BeautifulSoup) -> str:
    return el.text


def check():
    _update = {}
    req = requests.get(_url).content
    soup = BeautifulSoup(req, 'html.parser')
    rows = soup.find_all('tr')[9:227]   # Get all the countries only
    for row in rows:
        cols = row.find_all('td')[1:]  # The first item is the serial num
        _update[text(cols[0])] = {
            "TC": text(cols[1]),
            "NC": text(cols[2]) if text(cols[2]) != "" else "0",  # Make the new cases "0" instead of ""
            "TD": text(cols[3]),
            "ND": text(cols[4]) if text(cols[4]) != "" else "0",
            "TR": text(cols[5]),
            "AC": text(cols[6]),
            "SC": text(cols[7]),
            "TCpM": text(cols[8]),
            "DpM": text(cols[9]),
            "TT": text(cols[10]),
            "TpM": text(cols[11])
        }

    with open('worldwide.json', 'w') as f:
        json.dump(_update, f)


check()
