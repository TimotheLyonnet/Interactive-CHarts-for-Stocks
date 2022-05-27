#Three simple charts for stocks

import pandas as pd
import cufflinks as cf
import plotly.offline as plyo
plyo.init_notebook_mode(connected = True)
import pandas_datareader.data as web
from datetime import date  


#Enter dates of interest (end date is taken as today by default)
startdate = input("What to use as start date? (YYYY/MM/DD) ")
enddate = date.today()


#Enter stock ticker for which you want the charts
stock_ticker = input('What stock do you want to analyse? (enter ticker): ')


#Import stock data with Yahoo
stock = web.DataReader(stock_ticker, start = startdate, end = enddate, data_source = 'yahoo')


#First plot: simple line plot for stock price
plyo.iplot(
    stock['Adj Close'].iplot(asFigure = True, 
                      theme = 'polar', 
                      title = stock_ticker, 
                      xTitle = 'Date', 
                      yTitle = 'Share Price',
                      )
)


##Second plot: candle chart
quotes = stock[['Open', 'High', 'Low', 'Close']]
quotes = quotes.iloc[-60:]
quotes.tail()

#QuantFig:
qf = cf.QuantFig(
    quotes,
    title = stock_ticker + 'candle chart',
    legend = 'top',
    name = stock_ticker
)

plyo.iplot(
    qf.iplot(asFigure = True, 
              title = stock_ticker, 
              xTitle = 'Date', 
              yTitle = 'Share Price',
                      )
             )


#Third plot: Simple Moving Average plot
stock_df = pd.DataFrame(stock)
stock_df['SMA1'] = stock_df['Adj Close'].rolling(window = 42).mean()
stock_df['SMA2'] = stock_df['Adj Close'].rolling(window = 252).mean()
stock_df.dropna()

plyo.iplot(
    stock_df[['Adj Close', 'SMA1', 'SMA2']].iplot(asFigure = True, 
                      theme = 'polar', 
                      xTitle = 'Date', 
                      yTitle = 'Share Price',
                      )
)



