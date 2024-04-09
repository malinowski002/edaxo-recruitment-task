import requests

class ApiReader:
    def __init__(self, url="https://api.nbp.pl/api/exchangerates/tables/A?format=json"):
        self.url = url
    def get_from_nbp_api(self, currency):
        url = self.url
        # send a GET request to the NBP API
        response = requests.get(url)
        data = response.json()

        # read a date
        date = data[0]["effectiveDate"]

        # look for and read a specific currency data
        for record in data[0]["rates"]:
            if record["code"] == currency:
                rate = record["mid"]

        return date, rate