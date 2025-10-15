import yfinance as yf
import datetime as dt
import numpy as np
import matplotlib.pyplot as mpl

ticker = str(input('ticker? ')).upper()
years = float(input('years? '))
if years == int(years):
    years = int(years)
binCount = int((365*years)/20)

stock = [ticker]
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365*years)

df = yf.download(stock, start = startDate, end = endDate, auto_adjust = False)
adjusted_close = df['Adj Close']
log_returns = np.log(adjusted_close / adjusted_close.shift(1))

mpl.hist(log_returns, bins = binCount, color = 'orange', density = True)
mpl.title(ticker + ' Daily Logarithmic Return Over Previous ' + str(years) + ' Years')
mpl.show()
input("Click Enter to Exit")
exit()