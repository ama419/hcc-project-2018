#!/usr/bin/env python


# Copied from https://dev.socrata.com/foundry/data.cityofnewyork.us/p2mh-mrfv

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Example authenticated client (needed for non-public datasets):
client = Socrata('data.cityofnewyork.us',
                 'Q109zxFWPCLJF8NOCqLNKdJdw',
                 username="kira.schuman@gmail.com",
                 password="Schuman575")

# Pull data from API
results = client.get("p2mh-mrfv", limit=140000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df = results_df[results_df['address_city'] != 'BROOKLYN']
results_df = results_df[results_df['address_city'] != 'STATEN ISLAND']

# Save to CSV
results_df.to_csv('business_licenses.csv')
