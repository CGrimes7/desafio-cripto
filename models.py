from sqlalchemy import Column, String, Float, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Crypto(Base):
    __tablename__ = 'cryptocurrencies'

    id = Column(String, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    rank = Column(Integer)

class CryptoMarketData(Base):
    __tablename__ = 'market_data'

    id = Column(String, primary_key=True)
    crypto_id = Column(String, ForeignKey('cryptocurrencies.id'))
    price_usd = Column(Float)
    volume_usd_24hr = Column(Float)
    market_cap_usd = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
