import re

from task.connectors.api.api_reader import ApiReader


def is_it_date(date_as_string):
    date_pattern = r"\d{4}-\d{2}-\d{2}"

    if re.match(date_pattern, date_as_string):
        return True
    else:
        return False


class TestApiReader:

    def test_get_from_nbp_api(self):
        api_reader = ApiReader()
        date, rate = api_reader.get_from_nbp_api("USD")

        # check whether date is in correct format
        assert is_it_date(date)
        # check whether rate is actually a float
        assert type(rate) == float