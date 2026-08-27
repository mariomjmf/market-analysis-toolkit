import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import openpyxl
import xlsxwriter
from collections import defaultdict

# Background reference; general properties to be used throughout the code, update as needed

eu_exchanges = {"Xetra","London Stock Exchange","Deutsche Boerse AG","Euronext Amsterdam", "NASDAQ Helsinki","SIX Swiss Exchange","Euronext Paris","Borsa Italiana","Bolsas y Mercados Espanoles","Oslo Bors Asa"}

class Asset:

    n_assets = 0

    def __init__(self, ticker, name, asset_type, sector, exchange, currency, description):
        self.ticker = ticker
        self.name = name
        self.asset_type = asset_type
        self.sector = sector
        self.exchange = exchange
        self.currency = currency
        self.description = description
        self.region = "EU" if self.exchange in eu_exchanges else "US"

df = pd.read_csv("data/AssetDB.csv")
companies = {row.stock:Asset(row.yfinance_ticker, row.name,row.asset_type, row.sector, row.exchange, row.currency, row.description) for row in df.itertuples()}

eu_assets = [a for a in companies.values() if a.region == "EU"]
us_assets = [a for a in companies.values() if a.region == "US"]

sectors = defaultdict(list)
for a in companies.values():
    sectors[a.sector].append(a)

for sector in sectors:
    print(sector)