# Data loading code: 
# Input: 'companies' --> Load companies from list of companies generated from csv in 'com

import pandas as pd
import yfinance as yf
from pathlib import Path
from datetime import datetime, timedelta
from main_classes import Asset

def find_project_root():
    start = Path.cwd().resolve()
    for folder in [start, *start.parents]:
        if (folder / "data" / "AssetDB.csv").exists():
            return folder
    raise FileNotFoundError("Could not find data/AssetDB.csv above " + str(start))

def load_companies(data_path):
    df = pd.read_csv(data_path)
    companies = {row.stock:Asset(row.yfinance_ticker, row.name,row.asset_type, row.sector, row.exchange, row.currency, row.description) for row in df.itertuples()}
    return(companies,df)

def load_data(companies, days=50):
    today = datetime.today()
    startdate = today - timedelta(days)
    print(str(today))
    tickerlist = [a.ticker for a in companies.values()]
    assetdata = yf.download(tickerlist, start = startdate, end = today)
    return assetdata