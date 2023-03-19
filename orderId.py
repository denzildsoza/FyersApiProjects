
from fyers_api import fyersModel,accessToken
from fyers_api.Websocket import ws
from datetime import datetime,timedelta
import pandas as pd
client_id = '3H021OQ8ZI-100'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2Nzg2ODIzMzksImV4cCI6MTY3ODc1Mzg1OSwibmJmIjoxNjc4NjgyMzM5LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa0Rxamp2ekZwTFdZWmNSVnNabElXMlp6dlZwQXVPZFFkNExrYjRpS1V0TS1aRC1fcWhnanF6OVU2dmhsX1dvcU85R2JOUFlpMFB2SkpnSFllU3paUW1QdTJYWkJwcjhaYmpNam5DVmZOUlNGZ2sxOD0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwib21zIjoiSzEiLCJmeV9pZCI6IlhEMDg2ODUiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.zrWMWSql_ean5tNDfNp1iiDNfGtufkJu171ZFDWUqPk'

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
            "symbol":"NSE:TATAPOWER-EQ",
            "qty":1,
            "type":2, 
            "side":1,
            "productType":"INTRADAY",
            "limitPrice":0,
            "stopPrice":0,
            "validity":"DAY",
            "disclosedQty":0,
            "offlineOrder":"False",
            "stopLoss":0,
            "takeProfit":0
                        
        }
x = fyers.place_order(data)
print(x)                
OrderId = x['id']
fyers_object = open("orderId.txt", "w")
fyers_object.write(f'{OrderId}+{4}')
fyers_object.close()
