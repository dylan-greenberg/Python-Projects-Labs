import pandas as pd
import datetime as date
import matplotlib.pyplot as plt
import pandas_datareader.data as wb
import yfinance as yf

pd.set_option('display.max_columns', None)

# Initialize date range
startDate = date.datetime(2010,3,1)
endDate = date.datetime(2019,4,1)

# initialize SPX ticker for remote data load
SPX_Ticker = '^SPX'

# load FTSE index from CSV file and filter on correct dates
FTSE = pd.read_csv('^ftm_d.csv', index_col='Date')
FTSE.index = pd.to_datetime(FTSE.index, format='mixed')
FTSE = FTSE[(FTSE.index >= startDate) & (FTSE.index <= endDate)]

# remotely download SPX index from yfinance
SPX = yf.download(SPX_Ticker, startDate, endDate)

FTSE.rename(columns={'Close':'FTSE_Close'}, inplace=True)
SPX.rename(columns={'Close':'SPX_Close'}, inplace=True)

FTSE.drop(columns=['Open', 'High', 'Low', 'Volume'], axis=1, inplace=True)
SPX.drop(columns=['Open', 'High', 'Low', 'Volume', 'Adj Close'], axis=1, inplace=True)

FTSE['Current Return EUR'] = (FTSE['FTSE_Close']/FTSE['FTSE_Close'][0])
SPX['Current Return USD'] = (SPX['SPX_Close']/SPX['SPX_Close'][0])

FTSE['EUR Returns'] = (FTSE['Current Return EUR']*1000)
SPX['US Returns'] = (SPX['Current Return USD']*1000)

SPX_FTSE = SPX.join(FTSE, how='inner')

# print both dataframes to make sure everything looks good
print(FTSE.head())
print(SPX.head())
print(SPX_FTSE.head())

xAxis = SPX_FTSE.index
SPX_y = SPX_FTSE['US Returns']
FTSE_y = SPX_FTSE['EUR Returns']
plt.ylabel('Return')
plt.xlabel('Date')
plt.plot(xAxis, SPX_y, 'b', label='US Returns')
plt.plot(xAxis, FTSE_y, 'r', label='EUR Returns')
plt.legend()
plt.show()





