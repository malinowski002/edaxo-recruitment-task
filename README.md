#### Autor: Kacper Malinowski

- `example_currency_rates.json` - lokalne źródło danych z kursami walut
- `database.json` - baza danych z zapisanymi kursami walut

#### Projekt składa się z:
- modułu `connectors`, który zawiera klasy odpowiedzialne za połączenie ze źródłami danych
- `currency_converter.py` będącego głównym modułem aplikacji zawierającym klasę `PriceCurrencyConverterToPLN` umożwliającą konwersję cen między walutami
- modułu `database`, który zawiera implementacje baz danych (json i sql) do zapisu cen
- modułów `local` i `api` odpowiedzialnych za odczyt danych kolejno z lokalnych plików i API NBP
- katalog `tests` zawierający testy jednostkowe dla poszczególnych modułów aplikacji

#### Użycie:
Do projektu utworzono prostą, konsolową aplikację, umożliwiającą użytkowniką wybór konkretnych opcji tj. tryb uruchomienia, waluta czy źródło danych. Po podaniu wszystkich wartości otrzymywany jest wynik w poniższej postaci:
```
Price in source currency: 8.0
Currency: CZK
Currency rate: 0.19
Rate fetch date: 2023-09-01
Price in PLN: 1.52
```