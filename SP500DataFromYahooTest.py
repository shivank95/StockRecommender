import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

import time
"""
Gets S&P500 data from the source code of a wikipedia page. S&P 500 contains the top 500 companies by market capitalization

Then dumps the list into a pickle file - which is just a serialized version of any python object.
"""

def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
        
    with open("Pickles/sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
        
    print(tickers)

    return tickers

#save_sp500_tickers() - Uncomment to actually save a new pickle file with updates.  

#Getting data from Yahoo takes a lot of time. - Maybe 20 - 30 mins based on internet speed

"""
Get data from yahoo and stores it in StockData/{Ticker}.csv
"""
def get_data_from_yahoo(reload_sp500=False):
    
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("Pickles/sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)
    
    if not os.path.exists('StockData'):
        os.makedirs('StockData')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2017, 10, 30)
    
    for ticker in tickers:
        try:
            # just in case your connection breaks, we'd like to save our progress!
            if not os.path.exists('StockData/{}.csv'.format(ticker)):
                df = web.DataReader(ticker, "yahoo", start, end)
                df.to_csv('StockData/{}.csv'.format(ticker))
            else:
                print('Already have {}'.format(ticker))

            #time.sleep(0.5)
        except Exception as e:
            print("Got Exception: " + str(e))
            #time.sleep(0.5)

get_data_from_yahoo()
