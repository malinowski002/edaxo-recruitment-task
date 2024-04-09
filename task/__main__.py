from logging import getLogger

from task.currency_converter import PriceCurrencyConverterToPLN
from connectors.database.json import JsonFileDatabaseConnector
from connectors.database.sql import SqlDatabaseConnector

logger = getLogger(__name__)

def save_to_db(converted_price, mode):
    # depending on running mode, use either local file or db
    if mode == "dev":
        j_file_database_connector = JsonFileDatabaseConnector()
        j_file_database_connector.save(converted_price)

    elif mode == "prod":
        s_database_connector = SqlDatabaseConnector()
        s_database_connector.save(converted_price)

def main():
    while True:
        try:
            print("1. Convert currency")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                converter = PriceCurrencyConverterToPLN()
                # user entering running mode (dev or prod)
                while True:
                    mode = input("Enter running mode [dev/prod]: ")
                    if mode.lower() not in ["dev", "prod"]:
                        print("Enter a valid mode!")
                    else:
                        break

                # user entering currency code
                while True:
                    currency = input("Enter currency [EUR/CZK/etc.]: ")
                    if len(currency) != 3 and not currency.isalpha():
                        print("Enter a valid currency code!")
                    else:
                        break

                # user entering amount, assuming it is a number
                amount = float(input("Enter amount: "))

                # user entering source
                while True:
                    source = input("Enter source [file/nbp]: ")
                    if source.lower() not in ["file", "nbp"]:
                        print("Enter a valid source!")
                    else:
                        break

                # actual conversion proccess + saving data in db or json file
                converted_price = converter.convert_to_pln(currency=currency, price=amount, source=source)
                save_to_db(converted_price, mode)

                # outputting to user
                print(f"Price in source currency: {converted_price.price_in_source_currency}")
                print(f"Currency: {converted_price.currency}")
                print(f"Currency rate: {converted_price.currency_rate}")
                print(f"Rate fetch date: {converted_price.currency_rate_fetch_date}")
                print(f"Price in PLN: {converted_price.price_in_pln}\n")

                logger.info("Job done!")

            elif choice == "2":
                logger.info("Exiting.")
                break
            else:
                print("Enter a valid option.")
        except Exception as err:
            logger.error(f"An error {err} occured!")

if __name__ == "__main__":
    main()