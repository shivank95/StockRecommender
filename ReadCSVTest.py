import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('StockData/tsla.csv', parse_dates=True, index_col=0)

print(df.head(6))

#df.plot()
#plt.show() #Shows only volume

#df['Adj Close'].plot()	#Shows adjusted price chart
#plt.show()

#print(df[['High','Low']]) #Can reference specific columns

#Moving averages
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

#print(df.head()) 
#100ma will be NaN because there arn't 100 datapoints to work with.. df.head has the beginning period of data.
#But with min_periods=0 the first 100 will be calculated as it goes - with as many data points it can find.

print(df.tail()) #This will work because this has the most current period's data

print(df.head())

## Simple Graph with 100MA, Adj Close and Volume

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()