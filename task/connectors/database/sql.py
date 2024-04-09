from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# define a data model for the "records" table
class Record(Base):
    __tablename__ = "records"

    # define all columns
    id = Column("id", Integer, primary_key=True, autoincrement=True, unique=True)
    currency = Column("currency", String)
    rate = Column("rate", Float)
    price_in_pln = Column("price_in_pln", Float)
    date = Column("date", String)

    def __init__(self, id, currency, rate, price_in_pln, date):
        self.id = id
        self.currency = currency
        self.rate = rate
        self.price_in_pln = price_in_pln
        self.date = date

    def __repr__(self):
        # create a string representation of a record
        return f"id={self.id}, currency={self.currency}, rate={self.rate}, price_in_pln={self.price_in_pln}, date={self.date}"


class SqlDatabaseConnector:
    def __init__(self):
        # create and initialize an SQLAlchemy db engine
        self.engine = create_engine("sqlite:///database.db", echo=True)
        # create a table based on Base model
        Base.metadata.create_all(bind=self.engine)

        # create a session connecting to the db
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save(self, converted_price):
        # create variables for all the values (for cosmetic reasons)
        currency = converted_price.currency
        rate = converted_price.currency_rate
        price_in_pln = converted_price.price_in_pln
        date = converted_price.currency_rate_fetch_date
        # create a new record based on prev values
        record = Record(id=None, currency=currency, rate=rate, price_in_pln=price_in_pln, date=date)
        # add a record to the db
        self.session.add(record)
        self.session.commit()

    def get_all(self) -> list[...]:
        # get all records from the db
        return self.session.query(Record).all()

    def get_by_id(self, given_id) -> ...:
        # SELECT ... WHERE ID = ...
        return self.session.query(Record).filter_by(id=given_id).first()
