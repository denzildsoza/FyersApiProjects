
from fyers_api import fyersModel,accessToken
from fyers_api.Websocket import ws
from datetime import datetime,timedelta
import pandas as pd
client_id = '3H021OQ8ZI-100'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2ODYxMDkyNjAsImV4cCI6MTY4NjE4NDIwMCwibmJmIjoxNjg2MTA5MjYwLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa2ZfeE13NG5wTmZzQjk3MGtQOUpfaFNlZko4XzFVemxtMmZGVk5qUnhrSlYtYjdJVFppaVRPbzlOeV90SUJzcWREOTRKQXNZeHdBN094NUJVa2dIV1JfdFkycnNUMUlpamlYUG51VkMtRWY3bzNhTT0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwib21zIjoiSzEiLCJmeV9pZCI6IlhEMDg2ODUiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9._5y9Vmq6RiTQ3MJ3GJiWyK-zcEnPfsDNbFonO0jbDDc'

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="D:\Python Projects\hello_api")









# orderIdf = open("access_token.txt", "r").read()
# for i in orderIdf:
#     if i == "+":
#         break
#     orderId = orderId+i
    
# target = int(orderIdf[len(orderId)+1:])
# data = {"id":orderId}
# a = fyers.orderbook(data=data)
# obj = a["orderBook"][0]

# status , filledQty , tradedPrice , usymbol , side =  [obj[k] for k in ('status','filledQty','tradedPrice','symbol','side')]
# print(status , filledQty , tradedPrice , usymbol , side)


data = {
                "symbol":'NSE:NIFTY2360818650CE',
                "qty":50,
                "type":4, 
                "side":-1,
                "productType":"INTRADAY",
                "limitPrice":10,
                "stopPrice":15,
                "validity":"DAY",
                "disclosedQty":0,
                "offlineOrder":"True",
                "stopLoss":0,
                "takeProfit":0
            }
x = fyers.place_order(data)
print(x)                
# OrderId = x['id']
# fyers_object = open("orderId.txt", "w")
# fyers_object.write(f'{OrderId}+{4}')
# fyers_object.close()
