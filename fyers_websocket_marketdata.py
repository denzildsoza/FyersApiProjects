from fyers_api import fyersModel,accessToken
from fyers_api.Websocket import ws
from datetime import datetime,timedelta
import pandas as pd
client_id = '3H021OQ8ZI-100'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2ODY2Mjc1MjcsImV4cCI6MTY4NjcwMjY0NywibmJmIjoxNjg2NjI3NTI3LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa2gtVEhxcUdSVTh5bUJCblNtRjJYWkNTb1BQMEZDMkdraEhzcUhpTXY1TTd4Qkc3eWlSbE41NHVqd2hlUlFfLVowdC1OWmhGclpYYnJ5RnU5a18xaU1ZYUJHLXIxOHJ2aEJwaDFtYnQtdlFQTXJwbz0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwib21zIjoiSzEiLCJmeV9pZCI6IlhEMDg2ODUiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.k8dKJWMgWTMpLNZA2LMDPByyd2CtY0zTy3dXCcWDim8'

live_data = {}
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="")
ws_access_token = client_id + ":" + access_token
symbol= ["MCX:GOLDM23JULFUT"]    
def custom_message_Thread(msg): 
    if (msg[0]["timestamp"] % 3600 // 60) % 3 == 0:
        print(msg[0]["timestamp"],msg[0]["ltp"], (msg[0]["timestamp"] % 3600 // 60) % 3)
        


fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="")           
fyersSocket.websocket_data = custom_message_Thread

data_type = "symbolData"  

fyersSocket.subscribe(symbol=symbol, data_type=data_type)

fyersSocket.keep_running()  

