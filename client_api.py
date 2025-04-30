import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("API_BASE_URL")

def fetch_crypto_data(limit=10):
    url = f"{BASE_URL}/assets?limit={limit}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["data"]
