import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" \
               f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

def export_to_csv():
    engine = create_engine(DATABASE_URL)
    df = pd.read_sql("SELECT * FROM data_cryptos", engine)
    df.to_csv("data_history.csv", index=False)
