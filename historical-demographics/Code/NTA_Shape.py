# Code from: https://gist.github.com/aerispaha/f098916ac041c286ae92d037ba5c37ba

import pandas as pd



def read_shapefile(shp_path):
	"""
	Read a shapefile into a Pandas dataframe with a 'coords' column holding
	the geometry information. This uses the pyshp package
	"""
	import shapefile

	#read file, parse out the records and shapes
	sf = shapefile.Reader(shp_path)
	fields = [x[0] for x in sf.fields][1:]
	records = sf.records()
	shps = [s.points for s in sf.shapes()]

	#write into a dataframe
	df = pd.DataFrame(columns=fields, data=records)
	df = df.assign(coords=shps)

	return df

shape_df = read_shapefile('../Data/nynta_18a/nynta')

shape_df.to_csv('../Data/nta_shapes.csv')
