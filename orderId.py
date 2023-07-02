
from fyers_api import fyersModel,accessToken
from fyers_api.Websocket import ws
from datetime import datetime
import pandas as pd
import time
client_id = '3H021OQ8ZI-100'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2ODcyMzEzMzIsImV4cCI6MTY4NzMwNzQxMiwibmJmIjoxNjg3MjMxMzMyLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa2tSdGtnQm1xTFRDRXJKTTMyRTNnUEp5SktMSHRxODl4YzRUMmlaaTQxQll0eXQ2M24zTkNxeHV0SHIwUzc2MHhtVTZvMWpBQ0F1S1RqQkxBdXlyMkJKdjVhdWNhWmVRV0dJNFgyQzlKQUh2RXE4QT0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwib21zIjoiSzEiLCJmeV9pZCI6IlhEMDg2ODUiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.tE2wL1Qd87r3DdQ--Y7UrlCi5NmfJgMzYTXRcUkS4x8'

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

data = {"id":'23062000135233'}
response = fyers.orderbook(data=data)
print(response)
obj = response["orderBook"][0]
status , filledQty , tradedPrice , usymbol , side =  [obj[k] for k in ('status','filledQty','tradedPrice','symbol','side')]

limitfactor =round(tradedPrice- 4, 1)
triggerlimit=round(tradedPrice- 3,1)
start_time = time.time()
data = {
                "symbol":usymbol,
                "qty":filledQty,
                "type":4, 
                "side":-1,
                "productType":"MARGIN",
                "limitPrice":limitfactor,
                "stopPrice":triggerlimit,
                "validity":"DAY",
                "disclosedQty":0,
                "offlineOrder":"True",
                "stopLoss":0,
                "takeProfit":0
            }
while True:
  x = fyers.place_order(data)
print("--- %s seconds ---" % (time.time() - start_time))
print(x)                
# OrderId = x['id']
# fyers_object = open("orderId.txt", "w")
# fyers_object.write(f'{OrderId}+{4}')
# fyers_object.close()
