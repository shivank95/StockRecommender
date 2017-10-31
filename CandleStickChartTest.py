import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates #Weird date format in matplotlib
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('StockData/tsla.csv', parse_dates=True, index_col=0)

"""
OHLC - Open High Low Close - Candlesticks condense this data and show it very efficiently
Below we create a new DataFrame based on Adj Close and then resample it with a 10 day window
This shrinks the data size to something more manageable - it also normalizes multiple datasets.
"""
df_ohlc = df['Adj Close'].resample('10D').ohlc()

#Need to adjust the volume data as well based on 10D - so data is not too granular as seen in past tests.
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True) #Don't want dates to be an index anymore. Dates is now a regular column
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #Covert to mdates

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date() #converts the axis from the raw mdate numbers to dates

#Candles stick plotting 
candlestick_ohlc(ax1, df_ohlc.values, width=5, colorup='g') 

#Volume graphing - The fill_between function will graph x, y, then what to fill to/between. In our case, we're choosing 0.
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()