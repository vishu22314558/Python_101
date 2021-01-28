import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#print("Testing")

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.dataframe(tickerDf)

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)


pr = ProfileReport(tickerDf, explorative=True)

st.title("Pandas Profiling in Streamlit")
st.write(tickerDf)
st_profile_report(pr)
