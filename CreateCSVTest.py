import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2013, 1, 1)
end = dt.datetime(2017, 10, 30)


df = web.DataReader('TSLA', "yahoo", start, end)

print(df.head())

print("\n===== TAIL ====== \n")

print(df.tail(6))

df.to_csv('StockData/tsla.csv')

#Adj Close adjusts based on stock splits and different changes on the price over time.
