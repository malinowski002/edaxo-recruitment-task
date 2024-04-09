import json
from task.config import JSON_DATABASE_NAME
# from task.currency_converter import ConvertedPricePLN
from datetime import datetime



class JsonFileDatabaseConnector:
    def __init__(self) -> None:
        self._data = self._read_data()

    @staticmethod
    def _read_data() -> dict:
        try:
            # open and load data from file
            with open(JSON_DATABASE_NAME, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(".json file not found!")
            # in case of an eror return an empty dictionary
            return {}

    def save(self, entity: ...) -> int:
        # find an available, next ID number for new record
        available_id = 1
        while str(available_id) in self._data:
            available_id += 1

        # get current date and time
        now = datetime.now()

        # put read data in a dictionairy
        self._data[str(available_id)] = {
            "id": available_id,
            "currency": entity.currency,
            "rate": entity.currency_rate,
            "price_in_pln": entity.price_in_pln,
            "date": now.strftime("%Y-%m-%d")
        }

        try:
            # dump data in a json file
            with open(JSON_DATABASE_NAME, "w") as file:
                json.dump(self._data, file, indent=4)
        except IOError:
            print("An error ocurred while saving a file!")

        return 0

    def get_all(self) -> list[...]:
        all_records = []
        # get all items, put them in a list, and return the list
        for item in self._data:
            all_records.append(self._data[item])
        return all_records


    def get_by_id(self, record_id) -> ...:
        # look for a specific item and return it
        for item in self._data:
            record = self._data[item]
            if self._data[item]["id"] == record_id:
                return record

