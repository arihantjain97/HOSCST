import requests
import json
from config import FINANCIAL_MODELLING_PREP_API_KEY

#ticker data
TOTAL_STOCK_COUNT = 3
MARKET_CAP_CEILING = 3000000000
MARKET_CAP_FLOOR = 50000000
TICKER_BASE_URL = "https://financialmodelingprep.com/api/v3/stock-screener?marketCapMoreThan=%d&marketCapLowerThan=%d&limit=%d&exchange=%s&apikey=%s"
TICKER_EXCHANGE = 'NASDAQ'

#historical data
HISTORICAL_DATA_BASE_URL = "https://financialmodelingprep.com/api/v3/historical-price-full/%s?timeseries=%d&apikey=%s"
NUM_DAYS = 5

#share quanitity data
SHARE_QUANTITY_BASE_URL = "https://financialmodelingprep.com/api/v4/shares_float?symbol=%s&apikey=%s"

#moving average data
MA_DATA_BASE_URL = "https://financialmodelingprep.com/api/v3/technical_indicator/daily/%s?period=%d&type=%s&apikey=%s"
MA_TYPE = "sma"
MA_PERIOD_LIST = [21, 51, 100]


#get list of microcap tickers
ticker_url = TICKER_BASE_URL % (MARKET_CAP_FLOOR, MARKET_CAP_CEILING, TOTAL_STOCK_COUNT, TICKER_EXCHANGE, FINANCIAL_MODELLING_PREP_API_KEY)
ticker_r = requests.get(ticker_url)
ticker_data = ticker_r.json()
symbols = [stock['symbol'] for stock in ticker_data]



ticker_url = "https://financialmodelingprep.com/api/v4/institutional-ownership/portfolio-holdings-summary?cik=0001067983&apikey=" + FINANCIAL_MODELLING_PREP_API_KEY
ticker_r = requests.get(ticker_url)
ticker_data = ticker_r.json()
symbols = [stock['symbol'] for stock in ticker_data]






'''

for symbol in symbols:
    
    #get vwap, volume, gain per stock
    #wanted labels: 'vwap', 'volume', 'changePercent', 
    historical_data_url = HISTORICAL_DATA_BASE_URL % (symbol, NUM_DAYS, FINANCIAL_MODELLING_PREP_API_KEY)
    historical_data_r = requests.get(historical_data_url)
    historical_data = historical_data_r.json()
    print(historical_data)
    print("\n\n")
    
    #get free-float, outstanding shares
    shares_quantity_url = SHARE_QUANTITY_BASE_URL % (symbol, FINANCIAL_MODELLING_PREP_API_KEY)
    shares_quantity_r = requests.get(shares_quantity_url)
    shares_quantity = shares_quantity_r.json()
    print(shares_quantity)
    print("\n\n")
    
    #get sma
    for period in MA_PERIOD_LIST:
            ma_url = MA_DATA_BASE_URL % (symbol, period, MA_TYPE, FINANCIAL_MODELLING_PREP_API_KEY)
            ma_r = requests.get(ma_url)
            ma_data_full = ma_r.json()
            ma_data = ma_data_full[:NUM_DAYS]
            print(ma_data)
            print("\n\n")
'''
