from fyers_api import fyersModel
from time import sleep,strftime
from fyers_api.Websocket import ws
import threading
from multiprocessing import Process,Pool
import json



    

accessTokenFile = open("access_token.txt", "r")
access_token = accessTokenFile.read()
client_id = '3H021OQ8ZI-100'
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="C:\logs")
ws_access_token = f"3H021OQ8ZI-100:{access_token}"
fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="C:\logs")
run_background = False
orderUpdateData = {}
data_type = "orderUpdate"  
run_background  = False
bookProfit = {

}

def TrailStoploss():
    if ltp > 



def trailSlBookProfit(filledQty,tradedPrice,usymbol,limitfactor,triggerlimit,bookProfit,bookinglfactor,bookingtfactor):
    bookProfit = {
        "bookProfit" : tradedPrice - bookinglfactor
}
    live_data = {}
    print(usymbol)
    symbol = [str(usymbol)]
    dataType = "symbolData"
    def custom_message_Thread(msg): 
        for symbol_data in msg:
            live_data[symbol_data[f'symbol{-1}']] = live_data[symbol_data['symbol']]
            live_data[symbol_data['symbol']] = symbol_data['ltp']
        

    fyersSocket.websocket_data = custom_message_Thread

    def subscribe_new_symbol(symbol_list):        
        global fyersSocket, data_type
        fyersSocket.subscribe(symbol=symbol_list, data_type=dataType)
        
    t = threading.Thread(target=subscribe_new_symbol, args=(symbol,))
    t.start()
    print("prosses spawned")
    
    pivot = tradedPrice - limitfactor
    t = "sl"
    while True:

        print(live_data)
        diff = live_data[usymbol]  - live_data[f'{usymbol}{-1}']
        if len(live_data) != 0:
            if live_data[usymbol]<pivot and  (diff*diff)**0.5 <100 :
                data = {
                        "symbol":usymbol,
                        "qty":filledQty,
                        "type":2, 
                        "side":-1,
                        "productType":"INTRADAY",
                        "limitPrice":0,
                        "stopPrice":0,
                        "validity":"DAY",
                        "disclosedQty":0,
                        "offlineOrder":"False",
                        "stopLoss":0,
                        "takeProfit":0
                        
                    }
                fyers.place_order(data)
               
                break
        sleep(1)


    


def custom_message(msg):
    global orderUpdateData
    res = json.loads(msg)
    obj = res['d']
    status,filledQty,tradedPrice,usymbol ,side= obj['status'] , obj['filledQty'] , obj['tradedPrice'] , obj['symbol'] ,obj['side']
    
    if status == 2 and side == 1 :  
        arr = usymbol.split(':')
        if arr[1].startswith('NIFTY'):
            
        if arr[1].startswith('BANKNIFTY'):
            
        orderUpdateData = {

        }
   


 






if __name__ == "__main__":
    
    while True:
        timestamp = strftime('%H:%M:%S').split(":")
        if int(timestamp[0]) == 9 and int(timestamp[1]) >= 15:
            break
        elif int(timestamp[0]) >9  :
            break       
    sleep(2)
    fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="C:\logs")
    fyersSocket.websocket_data = custom_message
    def Ws_Order_update():
        global fyersSocket, data_type
        fyersSocket.subscribe(data_type=data_type)

    threading.Thread(target=Ws_Order_update).start()
    print("broked")
    while True:
        if orderUpdateData != {} :            
            p = Process(target=trailSlBookProfit, args=(orderUpdateData[0],orderUpdateData[1],orderUpdateData[2],orderUpdateData[3],orderUpdateData[4],orderUpdateData[5],orderUpdateData[6],orderUpdateData[7],))
            p.start()
            print("process started")
            orderUpdateData = []
            sleep(2)

  
















