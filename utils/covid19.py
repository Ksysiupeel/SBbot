import requests
from models.covid_country_info import Country_Info


class Covid:
    def __init__(self, country_prefix: str):
        self.country_prefix = country_prefix

    def get(self):
        url = "https://covid-19-data.p.rapidapi.com/country/code"

        params = {"code": self.country_prefix}

        headers = {
            'x-rapidapi-key': "API KEY",
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=params).json()

        return Country_Info(response)