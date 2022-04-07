"""
INFPROG2 P03 - Online Data
Author: Fabio Kapsahili
"""

"""
1.1 "Data sources and retrieval" 

"Write a module with guarded main code and a function that
retrieves the CHF rate for any given currency X.
"""


import requests
import requests_cache

requests_cache.install_cache("currency_cache", expire_after=3600)


def get_rate(currency):
    """
    Retrieves the CHF rate for any given currency X.

    :param currency: The currency code.
    The currency code is validated against the ISO 4217 standard.

    The used API requires a valid API key for authentication and is limited to 100 requests per month.
    Therefore the response is cached for 1 hour.
    """
    url = "https://currency-converter5.p.rapidapi.com/currency/convert"
    querystring = {"format": "json", "from": "CHF", "to": currency, "amount": "1"}
    headers = {
        "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com",
        "X-RapidAPI-Key": "393dbe845dmsh18cb2e731565518p1eb284jsn70cf087372f3",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        return None
