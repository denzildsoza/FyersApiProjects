from fyers_api import fyersModel
from fyers_api import accessToken
from fyers_api.Websocket import ws
import fyers_login as l
fyers = fyersModel.FyersModel(client_id=l.client_id, token=l.access_token,log_path="")
access_token = l.client_id + ":" + l.access_token

data_type = "orderUpdate"  
run_background  = False

def custom_message(msg):
    print (f"Custom:{msg}")  

ws.websocket_data = custom_message
fyersSocket = ws.FyersSocket(access_token=access_token,run_background=False,log_path="")
fyersSocket.subscribe(data_type=data_type)
fyersSocket.subscribe(data_type=data_type)
fyersSocket.keep_running()





















