from json import JSONDecodeError
import requests
from requests import ConnectTimeout, HTTPError, TooManyRedirects, ReadTimeout


def result(ip):
    url = "https://ip-location5.p.rapidapi.com/get_geo_info"

    payload = "ip={}".format(ip)
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Host": "ip-location5.p.rapidapi.com",
        "X-RapidAPI-Key": "6dca1e101dmsh8b4ec45bd2463b9p1aaffajsn2f145d14116a"
    }
    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        if response.status_code == 200:
            try:
                return response.json()
            except (ValueError, KeyError, IndexError, TypeError, JSONDecodeError):
                return None
        else:
            return None
    except (ConnectTimeout, ConnectionError, HTTPError, TooManyRedirects, ReadTimeout):
        return None