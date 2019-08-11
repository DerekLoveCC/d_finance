from pandas_datareader import get_data_yahoo as  get_data
import scipy.stats as stats
import scipy as sp
from pandas_datareader import DataReader

vix = DataReader("VIXCLS", "fred")
print(vix.shape)
print(vix.head())


# def ret_f(ticker, begdate, enddate):
#     p = get_data(ticker, begdate, enddate)
#     return (p.Close.values[1:] / p.Close.values[:-1] - 1)
#
#
# begdate = '20130101'
# enddate = '20151231'
# y = ret_f('IBM', begdate, enddate)
# x = ret_f('MSFT', begdate, enddate)
#
# print(sp.stats.bartlett(x, y))


