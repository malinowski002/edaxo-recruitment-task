from dataclasses import dataclass
from connectors.local.file_reader import FileReader
from connectors.api.api_reader import ApiReader

@dataclass(frozen=True)
class ConvertedPricePLN:
    price_in_source_currency: float
    currency: str
    currency_rate: float
    currency_rate_fetch_date: str
    price_in_pln: float


class PriceCurrencyConverterToPLN:
    def __init__(self):
        pass
    def convert_to_pln(self, *, currency: str, price: float, source: str) -> ConvertedPricePLN:
        # read data depending on source
        if source == "file":
            # use a local file reader
            f_reader = FileReader()
            date, rate = f_reader.get_from_local_file(currency)

        elif source == "nbp":
            # use an API reader
            a_reader = ApiReader()
            date, rate = a_reader.get_from_nbp_api(currency)

        # return a ConvertedPricePLN object
        converted_price = ConvertedPricePLN(
            price_in_source_currency=price,
            currency=currency,
            currency_rate=rate,
            currency_rate_fetch_date=date,
            price_in_pln=round(price * rate, 2)
        )
        return converted_price
