import requests
import json
#ApiKey is :"HS3SN56LVNNSZEEM"
API_URL = "https://www.alphavantage.co/query"
#base parameters for Api calls
params = {"function": "FUNCTION", "symbol": "symbol","datatype": "json", "apikey": "HS3SN56LVNNSZEEM"}

'''----------------------------------- TIME SERIES API CALLS -----------------------------------------------------------------'''
def intraday(symbol, interval):

    params["function"] = "TIME_SERIES_INTRADAY"
    params["symbol"] = symbol
    params["interval"] = interval
    response = requests.get(API_URL, params)
    return response.json()["Time Series (5min)"]

def daily(symbol):

    params["function"] = "TIME_SERIES_DAILY"
    params["symbol"] = symbol
    response = requests.get(API_URL, params)
    return response.json()['Time Series (Daily)']

def dailyAdjusted(symbol):

    params["function"] = "TIME_SERIES_DAILY_ADJUSTED"
    params["symbol"] = symbol
    response = requests.get(API_URL, params)
    return response.json()['Time Series (Daily)']

def weekly(symbol):

    params["function"] = "TIME_SERIES_WEEKLY"
    params["symbol"] = symbol
    response = requests.get(API_URL, params)
    return response.json()['Weekly Time Series']

def weeklyAdjusted(symbol):

    params["function"] = "TIME_SERIES_WEEKLY_ADJUSTED"
    params["symbol"] = symbol
    response = requests.get(API_URL, params)
    return response.json()["Weekly Adjusted Time Series"]

def monthly(symbol):

    params["function"] = "TIME_SERIES_MONTHLY"
    params["symbol"] = symbol
    response = requests.get(API_URL, params)
    return response.json()["Monthly Time Series"]

def monthlyAdjusted(symbol):

    params["function"] = "TIME_SERIES_MONTHLY_ADJUSTED"
    params["symbol"] = symbol
    response = requests.get(API_URL, params)
    return response.json()["Monthly Adjusted Time Series"]


def quoteEndPoint(symbol, function, interval = "5min"):

    params["function"] = function
    params["symbol"] = symbol
    if(function == "TIME_SERIES_INTRADAY"):
        params["interval"] = interval
    response = requests.get(API_URL, params)
    data = response.json()
    function_key = list(data.keys())
    return float(data[function_key[0]]['05. price'])

def searchEndPoint(keyword):

    params["function"] = "SYMBOL_SEARCH"
    del params["symbol"] 
    params["keywords"] = keyword
    response = requests.get(API_URL, params)
    return response.json()["bestMatches"]

def find(keyword):

    params = {
        "function": "SYMBOL_SEARCH", 
        "keywords": keyword,
        "datatype": "json", 
        "apikey": "HS3SN56LVNNSZEEM"
        }         
    response = requests.get(API_URL, params)
    options = response.json()["bestMatches"]
    if(len(options)):        
        print("results of the search for ('%s'):"%keyword)
        for i in range(len(options)):
            print("%d: %r(%r)"%((i + 1),options[i]["2. name"],options[i]["1. symbol"]))
    else:
        print("%r did not turn up any results" %(keyword))

                    
 
        
