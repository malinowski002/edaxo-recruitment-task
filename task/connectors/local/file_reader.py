import json

class FileReader:
    def get_from_local_file(self, currency):
        # open file and get data as JSON
        file = open("example_currency_rates.json")
        data = json.load(file)
        # assuming the latest record is the first one
        date = data[currency][0]["date"]
        rate = data[currency][0]["rate"]
        return date, rate
