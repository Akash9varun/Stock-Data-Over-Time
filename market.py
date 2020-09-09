import pandas as pd
import yfinance
from pandas_datareader import data

start_date = '2020-07-01'
end_date = '2020-07-27'

ticker = 'RELIANCE.NS'

data = data.get_data_yahoo(ticker, start_date, end_date)
data.head()
import matplotlib.pyplot as plt
data['Adj Close'].plot()
plt.show()

data['Adj Close'].plot(figsize=(10, 7))

plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()