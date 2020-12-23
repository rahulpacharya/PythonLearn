# -*- coding: utf-8 -*-

#when you load a time series data, you can specify 
# the index to be the date column.
import pandas as pd 
import numpy as np
# We create date values
date = [pd.Timestamp("2017-01-01"),
        pd.Timestamp("2017-01-02"),
        pd.Timestamp("2017-01-03")]

# We create random time series with date as index
timeSeries = pd.Series(np.random.randn(len(date)), index=date)

print(timeSeries)
print(timeSeries.index)

#If you want to pull out the value at a given timestamp
print("On January 1st 2017: ",timeSeries['2017-01-01'])
print("In date range :",timeSeries['2017-01-01':'2017-01-03'])

#########
# date_range() Function  helps in creating a set of sequential 
# date time values in a given range.
# Say you know the start date and the end date, and 
# you would want to generate a set of dates in that range.

dt_range = pd.date_range(start='2017-01-01',end='2017-01-19',freq='B')
print("Date Range : Business Day : ",dt_range)

dt_time_range_hr = pd.date_range(start="2017-01-01", periods=3, freq='H')
print("Date Range : Hourly : ",dt_time_range_hr)

dt_time_range_min = pd.date_range(start="2017-01-01", periods=3, freq='T')
print("Date Range : Minutes : ",dt_time_range_min)

dt_time_range_sec = pd.date_range(start="2017-01-01", periods=3, freq='S')
print("Date Range : Seconds : ",dt_time_range_sec)

# say you want to generate date-time values that are 
# 1 day, 1 hour, 1 minute and 10 seconds apart. (custom freq.)
dt_specific_apart = pd.date_range(start="2017-01-01", periods=5, freq='1D1h1min10s')
print("Specific data time apart:",dt_specific_apart)

# Instead of specifying a date, you can also specify 
# a day from when you want to generate the date time.

weekly_every_friday = pd.date_range(start="2017-01-01", periods=5, freq='W-FRI')
print("Date generated every Friday :",weekly_every_friday)

# You have generated separate indices with different dates 
# and would want to combine them 

#10 first business days in January starting 2017
a = pd.date_range(start="2017-01-01", periods=10, freq='BAS-JAN')
#10 last buisiness days in February starting 2017
b = pd.date_range(start="2017-01-01", periods=10, freq='A-FEB')
print("Union :")
print("a : ",a)
print("b : ",b)
print("aUb : ",a.union(b))


#Resampling
import numpy as np
import pandas as pd
#create a random customer incidence scenario for every minute.
#(600 iterations/times.. so 600 minutes)
customerArrival = pd.date_range('18/09/2017 8:00', periods=600, freq='T')
custArrivalTs = pd.Series(np.random.randint(0, 100, len(customerArrival)), index=customerArrival)
print(custArrivalTs.head(10))

#you are not interested in customer incidence every minute 
#but you would want to get the mean customer incidence every 10 mins.
#Downsample
# High frequency to low frequency
#default aggregation is ar. mean
print(custArrivalTs.resample('10min').mean().head(10))
print(custArrivalTs.resample('10min').sum().head(10))
# to find max value occured in time interval
# i.e maximum incidence at a given hour.
print(custArrivalTs.resample('1h').max().head(10))

#downsampling with custom function
def custom_resampler(array_like):
    return np.sum(array_like) + 5
print(custArrivalTs.resample('10min').apply(custom_resampler).head(10))

# to see the opening, closing, high and low incidence values 
# in a given interval of time
print(custArrivalTs.resample('1h').ohlc().head(10))

######
# Upsampling and Filling missing data
# the frequency of the data points is more than that of the original data captured.
# low frequency to high frequency
sampleRng = pd.date_range('9/19/2017 8:00', periods=10, freq='H')

sampleTs = pd.Series(np.random.randint(0, 100, len(sampleRng)), index=sampleRng)
print(sampleTs)
# you created a sample time series every 1 hour.
# you want to study your data every 15 mins, you have to
# perform upsampling.
print(sampleTs.resample('15min').mean().head())
# above output Shows NaN for intervals since data was not captured
# The Forward and Backward filling can be used to fill missing values
print(sampleTs.resample('15min').fillna("ffill").head())
print(sampleTs.resample('15min').fillna("backfill").head())
print(sampleTs.resample('15min').fillna("backfill",limit=2).head())
# Forward or Backward filling is a work around to fill the missing values.
# It might not be accurate.
# Some algorithms can fill the missing values based on the data patterns.
# This approach works better to get more accurate insights from Time Series Data.
# This method is called interpolation.
print(sampleTs.resample('15min').interpolate().head())

#####################################
# Hands On 1
# close_AA = closeTS['2011-01-01':'2011-03-01']
# Hands On 2
# upsample = closeTS.resample('1M').max().head()
# Hands On 3
# downsample = closeTS.resample('1d').fillna("ffill",limit=2).head(10)
#####################################

# TIMEZONES
# most used standard time zone is (coordinated universal time) UTC
# All other time zones are expressed as offset of UTC.
import pytz 
print(pytz.common_timezones[-5:])
print(pytz.timezone('US/Eastern'))

# Localization is the first step towards standardizing the time zone. Any specific time stamp is first localized to a given time zone.
# set your datetime index to a specific time zone.
# the given timezone is localized to UTC using the tz= parameter
# You can also localize using the tz_localize() function
import pandas as pd 
import random 
timeZoneRng = pd.date_range('9/18/2017 9:30', periods=6, freq='D',tz='UTC')
timeZoneTs = pd.Series(np.random.randn(len(timeZoneRng)), index=timeZoneRng)
print(timeZoneTs)
print(timeZoneTs.index.tz)

# If you want to convert your date-time value to another time zone
# you can use the tz_convert function.
print(timeZoneTs.tz_convert('US/Eastern'))

# You can create date values and convert them to 
# different time zones and also perform similar operations with
# time stamp values.
# Create a sample timestamp using TimeStamp function, 
# Localize and Convert the timestamp to the desired value.
sampleTimeStamp =  pd.Timestamp('2011-09-19 04:00')
timeStamp_utc = sampleTimeStamp.tz_localize('UTC')
print(timeStamp_utc)
print(timeStamp_utc.tz_convert('US/Eastern'))

# To offset the time based on Daylight Savings, 
# you can use the DateOffset() function
from pandas.tseries.offsets import Hour
stamp = pd.Timestamp('2012-03-12 01:30', tz='US/Eastern')
print(stamp)
print(stamp + Hour())

# Combining multiple timezones
dateRng = pd.date_range('9/19/2017 9:30', periods=10, freq='B')
timeSeries =  pd.Series(np.random.randn(len(dateRng)), index=dateRng)
tz1 = timeSeries[:7].tz_localize('Asia/Singapore')
tz2 = tz1[2:].tz_convert('Asia/Seoul')
combine = tz1 + tz2
print(combine.index)



import pandas as pd
import numpy as np 
# creates a sample time series
sampleRng = pd.date_range(start='2017', periods=60, freq='MS')
sampleTs = pd.Series(np.random.randint(-10, 10, size=len(sampleRng)), sampleRng).cumsum()
print(sampleTs.head(10))
# plot the sample
sampleTs.plot(c='r', title='Sample time series')

# Lag plot
# In the lag plot, you plotted the actual data against 
# the data with a time lag. This helps in determining 
# how the current data is predicting the future data.
from pandas.plotting import lag_plot
lag_plot(sampleTs)

# Auto correlation plot
# refers to correlating the data with itself. 
# Here we are correlating the data with a one-time lag.
# The plot gives a more accurate picture of how the data point
# is correlated among themselves.

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(sampleTs)
# When the autocorrelation plot shows an exponential behavior, 
# the time series is stationary.

# Stationarity Check
# Runnning ADF test

import random 
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
sampleRng = pd.date_range(start='2017', periods=120, freq='MS')
sampleTs = pd.Series(np.random.randint(-10, 10, size=len(sampleRng)), sampleRng).cumsum()

tsResult = adfuller(sampleTs)
print('ADF Statistic: %f' % tsResult[0])
print('p-value: %f' % tsResult[1])
for key, value in tsResult[4].items():
    print('\t%s: %.3f' % (key, value))
    
# The more negative the ADF statistic value is 
# the more likely the data is stationary.

# The ADF Statistic should be compared to critical p-values 
# that are at 1, 5, and 10%.

# If the ADF statistic value is less than the critical value at 5% 
# and the p-value is less than 0.05, then we can reject 
# the null hypothesis that the data is non-stationary with 95% confidence level.
    
# Here ADF Statistic: -2.524889
# p-value: 0.109535 is greater than 0.05 
# so we accept the null hypothesis, which means 
# the data is non-stationary.
    
# COMPONENTS OF TIME SERIES
# Trend, Seasonal, Cycle, Random

from statsmodels.tsa.seasonal import seasonal_decompose
sampleTs_decomp = seasonal_decompose(sampleTs, period=12) 
sampleTs_trend = sampleTs_decomp.trend 
sampleTs_seasonal = sampleTs_decomp.seasonal 
sampleTs_residual = sampleTs_decomp.resid

sampleTs_trend.plot(title='Sample time series trend')
sampleTs_seasonal.plot(title='Sample time series seasonal')
sampleTs_residual.plot(title='Sample time series residual')

# Forecasting models
from statsmodels.tsa.arima_model import ARIMA 
# 1) Autoregression 
model = ARIMA(sampleTs, order=(1, 1, 0)) 
predValues = model.fit()
# 2) Moving Average
model = ARIMA(sampleTs, order=(0, 1, 1)) 
movingAvgRes = model.fit() 
# 3) AIRMA
model = ARIMA(sampleTs, order=(1, 0, 1)) 
arimares = model.fit() 