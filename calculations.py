import pandas as pd
import yfinance as yf

# Data is in business days

apple1y = pd.read_csv("AAPL1Y.csv", index_col=0)  # 253 items
apple5y = pd.read_csv("AAPL5Y.csv", index_col=0)  # 1259 items
aapl = yf.Ticker("AAPL")

# Stocks put into a list for 1 year and 5 years data

closing1y = []
for stock in apple1y["Adj Close"]:
    closing1y.append(round(stock, 2))

volume1y = []
for vol in apple1y["Volume"]:
    volume1y.append(vol)

closingList10 = closing1y[242:]
closingList50 = closing1y[202:]
closingList100 = closing1y[152:]
closingList200 = closing1y[52:]

closingList12 = closing1y[240:]
closingList26 = closing1y[226:]

closingList20 = closing1y[232:]

closingList14 = closing1y[238:]
closingList3 = closing1y[249:]

# General stock information for current day
earnings = aapl.earnings["Earnings"][2021]
shares_outstanding = aapl.info['sharesOutstanding']

bid = aapl.info['bid']
ask = aapl.info['ask']

current_price = aapl.info['regularMarketPrice']

market_cap = aapl.info['marketCap']

ebitda = aapl.info['ebitda']
enterprise_multiple = aapl.info['enterpriseToEbitda']

# Simple moving average (SMA) 10 days, 50 days, 100 days, and 200 days
# 12 and 24 days too for the MACD calculations
# Also, 20 days for Bollinger bands

SMA50 = round(sum(closingList50)/50, 2)

SMA100 = round(sum(closingList100)/100, 2)

SMA200 = round(sum(closingList200)/200, 2)

SMA12 = round(sum(closingList12)/12, 2)
SMA26 = round(sum(closingList26)/26, 2)

SMA20 = round(sum(closingList20)/20, 2)

# Exponential moving average (EMA) 50 days, 100 days, and 200 days
# Also 12 and 26 days for MACD

EMA50 = 0

EMA100 = 0

EMA200 = 0

EMA12 = 0
EMA26 = 0

for i in range(5):
    if i == 0:
        multiplier = 2/(50+1)
        EMAprevious = SMA50
        for stock in closingList50:
            EMA50 = ((stock - EMAprevious)*multiplier) + EMAprevious
            EMAprevious = EMA50
    if i == 1:
        multiplier = 2/(100+1)
        EMAprevious = SMA100
        for stock in closingList100:
            EMA100 = ((stock - EMAprevious)*multiplier) + EMAprevious
            EMAprevious = EMA100
    if i == 2:
        multiplier = 2/(200+1)
        EMAprevious = SMA200
        for stock in closingList200:
            EMA200 = ((stock - EMAprevious)*multiplier) + EMAprevious
            EMAprevious = EMA200
    if i == 3:
        multiplier = 2/(12+1)
        EMAprevious = SMA12
        for stock in closingList12:
            EMA12 = ((stock - EMAprevious)*multiplier) + EMAprevious
            EMAprevious = EMA12
    if i == 4:
        multiplier = 2/(26+1)
        EMAprevious = SMA26
        for stock in closingList26:
            EMA26 = ((stock - EMAprevious)*multiplier) + EMAprevious
            EMAprevious = EMA26

# Moving average convergence divergence (MACD) (12,26)

MACD = round(EMA12 - EMA26, 2)

# Relative strength index (RSI)


# Kairi Relative Index (KRI) for 20 days

KRI = ((closing1y[-1]-SMA20)/SMA20)*100

# Standard deviation (SD) 20 days for January 6th, 2022

R_avg = SMA20
time_period = 20-1
summation = 0

for i in closingList20:
    summation += (i - R_avg)**2

standard_deviation = round((summation/time_period)**(1/2), 2)

# Bollinger bands for January 6th 2022

middle_band = SMA20
upper_band = SMA20 + (standard_deviation*2)
lower_band = SMA20 - (standard_deviation*2)

# Stochastic oscillator 14 days January 6th 2022

lowest_low = min(closingList14)
highest_high = max(closingList14)
lowest_low2 = min(closing1y[237:251])
lowest_low3 = min(closing1y[236:250])
highest_high2 = max(closing1y[237:251])
highest_high3 = max(closing1y[236:250])

percentK = ((closing1y[-1] - lowest_low)/(highest_high - lowest_low)) * 100
percentK2 = ((closing1y[-2] - lowest_low2)/(highest_high2 - lowest_low2)) * 100
percentK3 = ((closing1y[-3] - lowest_low3)/(highest_high3 - lowest_low3)) * 100

percentD = round((percentK+percentK2+percentK3)/3, 2)  # slow stochastic

# On-balance volume (OBV) for January 6th 2022

previous_OBV = volume1y[-2]  # just for interpretation sake
current_volume = volume1y[-1]
OBV = 0

if closing1y[-1] > closing1y[-2]:
    OBV = previous_OBV + current_volume
elif closing1y[-1] < closing1y[-2]:
    OBV = previous_OBV - current_volume
else:
    OBV = previous_OBV

# Ichimoku cloud January 6th 2022

period_high52 = max(closing1y[200:])
period_high26 = max(closing1y[226:])
period_high9 = max(closing1y[243:])

period_low52 = min(closing1y[200:])
period_low26 = min(closing1y[226:])
period_low9 = min(closing1y[243:])

tenkan_sen = (period_high9+period_low9)/2  # conversion line

kijun_sen = ((period_high26+period_low26)/2)  # base line

senkou_spanA = (tenkan_sen+kijun_sen)/2  # leading span A

senkou_spanB = (period_high52+period_low52)/2  # leading span B

chikou_span = closingList26  # lagging span

# 52-week high and 52-week low

fiftytwo_week_high = period_high52

fiftytwo_week_low = period_low52

# Average volume for 30 days. December 7th 2022 to January 6th 2022

average_volume = round(sum(volume1y[231:])/22, 2)

# Earnings Per Share (EPS)

EPS = round(earnings/shares_outstanding, 2)

# Price-Earning Ratio (P/E)

pe_ratio = round(current_price/EPS, 2)


# Bid-ask

bid_ask = round(abs(ask-bid), 3)
bid_ask_percent = round((bid_ask/ask)*100, 3)

# Growth (1m, 3m, 6m, 1y) from December 7th 2021 to January 6th 2022

growth1m = round(closing1y[-1] - closing1y[231], 2)

growth3m = round(closing1y[-1] - closing1y[159], 2)

growth6m = round(closing1y[-1] - closing1y[124], 2)

growth1y = round(closing1y[-1] - closing1y[0], 2)
