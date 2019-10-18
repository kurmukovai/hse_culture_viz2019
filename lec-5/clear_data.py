import pandas as pd
import numpy as np

wine = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

wine = wine[wine.price <= 30]
wine = wine.drop('region_2', axis=1)
wine = wine.dropna()


val, counts = np.unique(wine.taster_name.values, return_counts=True)
# print([v for v,c in zip(val, counts) if c <  300])
# print('\n')
# print(np.unique(wine.country.values, return_counts=True))

wine.query('''taster_name != "Anne Krebiehl\xa0MW" \
and taster_name != "Lauren Buzzeo" \
and taster_name != "Matt Kettmann" \
and taster_name != "Susan Kostrzewa" \
and taster_name != "Christina Pickard" \
and taster_name != "Fiona Adams" \
and country != "Canada"''', inplace=True) 

values, counts = np.unique(wine.variety.values, return_counts=True)
for v,c in zip(values, counts):
    if c < 30:
        wine.query(f'variety != "{v}"', inplace=True)
        
wine.reset_index(inplace=True)
wine.drop('index', axis=1, inplace=True)

wine.to_excel('wine-data-20k.xlsx', index=False)