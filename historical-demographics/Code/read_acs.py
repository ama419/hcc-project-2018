import pandas as pd

# NTAs of interest
NTAs = ['MN09', 'MN06', 'MN04', 'MN34', 'MN11', 'MN33', 'MN09', 'MN03'] #might add some in BX

# PUMAs of interest
PUMAs = [3802, 3803, 3804] #maybe add 3801

# Community Districts of interest
CDs = [] # Add: CD9, CD10, CD11; maybe: CD12, CD1, CD4, more??

# Sample file
fname = '../Data/ACS/acs_demo_06to10_ntas.xlsx'

# Read file, transpose, set index, set columns
df = pd.read_excel(fname, sheet_name='Manhattan')
df = df.transpose().reset_index()
df.columns = df.loc[0]

# Remove duplicate row
df = df.drop(0)

# Get NTA code
df['NTA'] = df['Demographic and Housing\n Subjects\n'].fillna(method = 'ffill').str.split().str[0]

# Select data for NTAs of interest
df = df[df['NTA'].isin(NTAs)]