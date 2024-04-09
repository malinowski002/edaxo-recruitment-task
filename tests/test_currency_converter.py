import sys
sys.path.append("../task")
from task.currency_converter import PriceCurrencyConverterToPLN, ConvertedPricePLN

class TestPriceCurrencyConverterToPLN:
    class MockFileReader:
        # mock reading from a file
        def get_from_local_file(self, currency):
            return "2024-04-07", 4.2

    class MockApiReader:
        # mock getting data from api
        def get_from_nbp_api(self, currency):
            return "2024-04-07", 4.2

    def test_convert_to_pln(self):
        print(sys.path)
        converter = PriceCurrencyConverterToPLN()
        converter.f_reader = self.MockFileReader()

        result = converter.convert_to_pln(currency="EUR", price=100, source="nbp")

        # check if result is of ConvertedPricePLN type
        assert type(result) == ConvertedPricePLN
        # check if returned currency is expected currency
        assert result.currency == "EUR"
        # check if returned price is expected price
        assert result.price_in_source_currency == 100
        # check if currency rate is a positive number
        assert result.currency_rate > 0.0