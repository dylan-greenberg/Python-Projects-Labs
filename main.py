import pandas as pd

df = pd.read_csv(r'/Users/dylangreenberg/Downloads/world_population.csv')
pd.set_option('display.max_columns', None)
print(df.head())
print(df[df['Rank'] <= 10])
print(df[df['Rank'] > 10].head())


