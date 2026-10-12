import random
from collections import defaultdict
from main_classes import Automated, Manual 
# Asset class not loaded as it is not required in main code :: See more in
# 'data_utils.py' and 'main_classes.py'. Likewise for 'Portfolio'
from data_utils import load_companies, load_data, find_project_root

# Locate the project folder from anywhere by searching upward for data/AssetDB.csv
data_path = find_project_root() / "data" / "AssetDB.csv"

# Load list of companies from csv outlined above -- See 'data_utils.py' for details
companies, df = load_companies(data_path)

eu_assets = [a for a in companies.values() if a.region == "EU"]
us_assets = [a for a in companies.values() if a.region == "US"]

sectors = defaultdict(list)
for a in companies.values():
    sectors[a.sector].append(a)

# Using the loaded companies, load the yfinance data using code -- See 'data_utils.py' for details
assetdata = load_data(companies) # Extra parameter: load_data(companies, days = ###)

random.seed(42) # Use random seed for traceability and repeatability
Portfolio1 = Automated("Randomized Portfolio")
Portfolio1.build(companies, 40)

Portfolio2 = Automated("60/40", weights={"US":0.6,"EU":0.4})
Portfolio2.build(companies, 30)
