from fyers_api import fyersModel,accessToken
from fyers_api.Websocket import ws
from datetime import datetime,timedelta
import pandas as pd
client_id = '3H021OQ8ZI-100'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2Nzg0MjA0MzMsImV4cCI6MTY3ODQ5NDY1MywibmJmIjoxNjc4NDIwNDMzLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa0NxblJmOTNkNmF2djdObW5xWU9CV1ZQckZHVlF0czFHcG1iUVJTZ29iTGt1Y3BOb2F3ZzY5dUo2VDhQRlN0YzJIaC01V1l1WXZ3bWJrSHRTQ2hXc3Q3c3FmUi1aMTJfVUJERFdLN3l2dHAxV3B6UT0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwib21zIjoiSzEiLCJmeV9pZCI6IlhEMDg2ODUiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.edzJ2yC2YLaK_UnBC1qe8KeFaFBajpyQQmFZuNIMIfw'

live_data = {}
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="D:\Python Projects\hello_api")
ws_access_token = client_id + ":" + access_token
run_background  = False
symbol= ["MCX:GOLD23APRFUT"]    
def custom_message_Thread(msg): 
        
    print(msg)
        
fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="D:\Python Projects\hello_api")           
fyersSocket.websocket_data = custom_message_Thread

data_type = "orderUpdate"  
run_background  = False

fyersSocket.subscribe(data_type=data_type)

fyersSocket.keep_running()  


