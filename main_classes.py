# Class definition code to be used in 'main.py'

import random
from abc import ABC, abstractmethod

# Background reference; general properties to be used throughout the code, update as needed

eu_exchanges = {"Xetra","London Stock Exchange","Deutsche Boerse AG","Euronext Amsterdam", "NASDAQ Helsinki","SIX Swiss Exchange","Euronext Paris","Borsa Italiana","Bolsas y Mercados Espanoles","Oslo Bors Asa"}

# Main 'Asset' class storing asset information; exchange, currency, name, ticker, and sector where applicable
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
        Asset.n_assets += 1

# General "Portfolio" abstract class as blueprint for manual or automatic portfolio creation
class Portfolio(ABC):
    def __init__(self, name):
        self.name = name
        self.portfolio_assets=[]

    @abstractmethod
    def build(self):
        pass

# Manual Portfolio subclass to be filled in with a manual list of tickers
class Manual(Portfolio):
    def __init__(self, name):
        super().__init__(name)

    def build(self, assetlist):
        for asset in assetlist:
            if asset not in self.portfolio_assets:
                self.portfolio_assets.append(asset)

# Automated Portfolio subclass to be filled with region and/or sector weightings (or neither for random selection)
# Asset selection is still randomized for any type of portfolio (Random/Region Split/Region + Sector Split); worth considering separating this code
# so the portfolios don't have to be created on each run and can be stored separately from the main data import and data analysis.
class Automated(Portfolio):
    def __init__(self, name, weights=None):
        super().__init__(name)
        self.weights = weights

    def build(self, companies, n = None):
        if self.weights is None:
            self.portfolio_assets = random.sample(list(companies.values()), n)
            return

        for region, split in self.weights.items():
            if isinstance(split,dict): # Region + Sector splits
                for sector, pct in split.items():
                    pool = [a for a in companies.values() if a.region == region and a.sector == sector]
                    count = round(n * pct)
                    self.portfolio_assets += random.sample(pool, min(count, len(pool)))
            else: # Region split only
                pool = [a for a in companies.values() if a.region == region]
                count = round(n * split)
                self.portfolio_assets += random.sample(pool, min(count, len(pool)))