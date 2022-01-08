# Security-Screener

Still in progress.
Version: 1.0.0

Analysis tools used:
- Simple moving average. (SMA)
- Exponential moving average. (EMA)
- Moving average convergence divergence. (MACD)
- Relative strength index. (RSI)
- Standard deviation.
- Bollinger bands.
- Stochastic oscillator.
- On-balance volume. (OBV)
- Ichimoku cloud.
- Kairi relative index. (KRI)
- 52-week high and 52-week low.
- Average daily trading volume. (ADTV)
- Earnings per share. (EPS)
- Price-to-earnings ratio. (P/E ratio)
- Bid-ask spread.
- 1 month, 3 months, 6 months, and 1 year growth.
- Market capitalization. 
- Bid and ask.
- Earnings.
- Shares outstanding.
- Earnings before interest, taxes, depreciation, and amortization. (EBITDA)
- Enterprise multiple. 


To do:
- Use the equations to create more data points. Subsequently, use matplotlib to graph the data.
- Create candlestick chart.
- Combine analysis tools (the calculations) and the candlestick chart together.
- [Optional] Create fibonacci retracement levels. (23.6%, 38.2%, 50%, 61.8%, and 78.6%)
- Clean up code by using classes and functions.

Issues:
- Some calculations don't match up with online data.
- Yfinance module slowing down the program. (Possibly use an API and do batch API calls to speed up program)

Notes:
- Most calculations are done for only 1 day (January 6th, 2022). 
- Obviously, more calculations have to be done to make a graph
- Some calculations may be wrong due to date issues, or my general inexperience.
- Use the yf.download() function to get new data.
- Yfinance slows down the program, so comment some things out for faster speeds.
