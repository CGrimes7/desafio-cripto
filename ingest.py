from database import engine, SessionLocal
from models import Base, Crypto, CryptoMarketData
from api_client import fetch_crypto_data

def ingest_data():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    cryptos = fetch_crypto_data()

    for crypto in cryptos:
        crypto_obj = Crypto(
            id=crypto["id"],
            name=crypto["name"],
            symbol=crypto["symbol"],
            rank=int(crypto["rank"]),
        )
        session.merge(crypto_obj)

        market_data = CryptoMarketData(
            id=crypto["id"] + "_market",
            crypto_id=crypto["id"],
            price_usd=float(crypto["priceUsd"]),
            volume_usd_24hr=float(crypto["volumeUsd24Hr"]),
            market_cap_usd=float(crypto["marketCapUsd"]),
        )
        session.merge(market_data)

    session.commit()
    session.close()
