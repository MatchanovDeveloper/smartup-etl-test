import requests
import json
import pandas as pd
from config import get_headers


def get_data(url, key):
    response = requests.get(url, headers=get_headers())

    if response.status_code != 200:
        return "Xatolik"

    records = response.json()

    if not records:
        return pd.DataFrame()

    return pd.json_normalize(records[key])