import json
import tempfile
import pytest

from task.connectors.database.json import JsonFileDatabaseConnector

class TestJsonFileDatabaseConnector:
    def setup_method(self):
        # create a connector and mock data inside
        self.connector = JsonFileDatabaseConnector()
        self.connector._data = {
            "1": {"id": 1, "currency": "EUR", "rate": 4.2, "price_in_pln": 10.0, "date": "2024-04-08"},
            "2": {"id": 2, "currency": "CZK", "rate": 0.2, "price_in_pln": 8.40, "date": "2024-04-07"},
            "3": {"id": 3, "currency": "USD", "rate": 3.9, "price_in_pln": 100.0, "date": "2024-04-07"}
        }

    def test_get_by_id(self):
        record_id = 1

        record = self.connector.get_by_id(record_id)

        # check whether id is correct
        assert record["id"] == record_id
        # check if all expected values are in the record
        assert "currency" in record
        assert "rate" in record
        assert "price_in_pln" in record
        assert "date" in record

    def test_get_all(self):
        all_records = self.connector.get_all()

        # check whether list is not empty
        assert len(all_records) > 0

        for record in all_records:
            # check if all expected values are in the record
            assert "id" in record
            assert "currency" in record
            assert "rate" in record
            assert "price_in_pln" in record
            assert "date" in record