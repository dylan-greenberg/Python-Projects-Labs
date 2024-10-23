#Step 1(10 points): Remotely Download "Treasury Constant Maturity Rate" from FRED
#(https://fred.stlouisfed.org/categories/115) from 02/01/2014 to 02/01/2016:
#6-Month
#1-Year
#5-Year
#10-Year
#Step 2( 5 points ): Determine the average and standard deviation for each of the maturities( maturity is 6-month, 1 year, etc.)
#Step 3( 5 points ): Select only those rows that have value more or less than avg +/- 1 std
#Step 4( 10 points ): Create a dataframe which has only those rows for which all of the maturities
#has value outside of avg +/- 1 std. Hint: think about joins for frames in step 3
#Step 5( 5 points): Save the generated dataframe as sigma.xlsx
#Please upload this filled file and sigma.xlsx

import pandas_datareader.data as wb
import datetime as date
import pandas as pd

start_date = date.datetime(2014, 2, 1)
end_date = date.datetime(2016, 2, 1)

df_6mo = wb.DataReader('DGS6MO', 'fred', start_date, end_date).reset_index()
df_1yr = wb.DataReader('DGS1', 'fred', start_date, end_date).reset_index()
df_5yr = wb.DataReader('DGS5', 'fred', start_date, end_date).reset_index()
df_10yr = wb.DataReader('DGS10', 'fred', start_date, end_date).reset_index()

df = df_6mo.merge(df_1yr, on='DATE', how='inner')
df = df.merge(df_5yr, on='DATE', how='inner')
df = df.merge(df_10yr, on='DATE', how='inner')

df_6mo_mean = df_6mo['DGS6MO'].mean()
df_1yr_mean = df_1yr['DGS1'].mean()
df_5yr_mean = df_5yr['DGS5'].mean()
df_10yr_mean = df_10yr['DGS10'].mean()

df_6mo_std = df_6mo['DGS6MO'].std()
df_1yr_std = df_1yr['DGS1'].std()
df_5yr_std = df_5yr['DGS5'].std()
df_10yr_std = df_10yr['DGS10'].std()

final_df = df[
    ((df['DGS6MO'] > (df_6mo_mean + df_6mo_std)) | (df['DGS6MO'] < (df_6mo_mean - df_6mo_std))) &
    ((df['DGS1'] > (df_1yr_mean + df_1yr_std)) | (df['DGS1'] < (df_1yr_mean - df_1yr_std))) &
    ((df['DGS5'] > (df_5yr_mean + df_5yr_std)) | (df['DGS5'] < (df_5yr_mean - df_5yr_std))) &
    ((df['DGS10'] > (df_10yr_mean + df_10yr_std)) | (df['DGS10'] < (df_10yr_mean - df_10yr_std)))
]

print(final_df)

final_df.to_excel('sigma.xlsx', index=False)

