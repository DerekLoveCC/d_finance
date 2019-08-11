from matplotlib.pyplot import *
import pandas_datareader as pdatareader
import mpl_finance as fin
import numpy as np
import matplotlib.mlab as mlab

ticker = 'IBM'
begdate = "20150101"
enddate = "20151109"
p = pdatareader.get_data_yahoo(ticker, begdate, enddate)
ret = (p.Close.values[1:] - p.Close.values[:-1]) / p.Close.values[:1]

[n, bins, patches] = hist(ret, 100)

mu = np.mean(ret)
sigma = np.std(ret)
x = mlab.normpdf(bins, mu, sigma)
plot(bins, x, color='red', lw=2)
title("IBM return distribution")
xlabel("Returns")
ylabel("Frequency")
show()
