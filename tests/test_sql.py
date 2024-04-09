import json
import tempfile
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import task
from task.connectors.database.sql import SqlDatabaseConnector

class MockConvertedPrice():
    price_in_source_currency: float
    currency: str
    currency_rate: float
    currency_rate_fetch_date: str
    price_in_pln: float

class TestJsonFileDatabaseConnector:
    def test_save_and_get_all(self):
        sql_database_connector = SqlDatabaseConnector()

        # create a MockConvertedPrice object
        mocked_converted_price = MockConvertedPrice()
        # set all required values
        mocked_converted_price.price_in_source_currency = 10.0
        mocked_converted_price.currency = "EUR"
        mocked_converted_price.currency_rate = 4.2
        mocked_converted_price.currency_rate_fetch_date = "2024-04-08"
        mocked_converted_price.price_in_pln = 42.0

        sql_database_connector.save(mocked_converted_price)

        all_records = sql_database_connector.get_all()

        # check if a list is returned
        assert type(all_records) == list
        # check whether the list is not empty
        assert len(all_records) > 0

    def test_get_by_id(self):
        sql_database_connector = SqlDatabaseConnector()
        record = sql_database_connector.get_by_id(1)

        # check whether a record is of Record type
        assert type(record) == task.connectors.database.sql.Record
        # check if id is equal to the expected id
        assert record.id == 1