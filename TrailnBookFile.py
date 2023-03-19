from fyers_api import fyersModel
from time import sleep,strftime
from fyers_api.Websocket import ws
import threading
from multiprocessing import Process
from json import load, loads



# access_token_file = open("access_token.txt", "r")
# access_token = access_token_file.read()
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2Nzg2Nzk1NzUsImV4cCI6MTY3ODc1Mzg1NSwibmJmIjoxNjc4Njc5NTc1LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa0RwNFhLenlNWXJROU1GUVlQcWZpaVc4alNaT3NMUW1UWlhaazk5eVRFT0x6MmViWGp1YVVuV05MR2o4cjBKM3pIY1k2dlZKeXd1Si16U1Rub2FVZVJRNFZVRG1JcHlnQWxGMTY1MFN1SXdiSHlsdz0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwib21zIjoiSzEiLCJmeV9pZCI6IlhEMDg2ODUiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.RewFNpL6alj3lbSYSrXIafgPzsUE2eNHM-AVopE6HU0'
client_id = '3H021OQ8ZI-100'
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="D:\Python Projects\hello_api\Logs")
ws_access_token = f"3H021OQ8ZI-100:{access_token}"
fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="D:\Python Projects\hello_api\Logs")

orderUpdateData = []
data_type = "orderUpdate"  
run_background  = False

def fetchOrderData():
    orderId = ""    
    orderIdf = open("orderId.txt", "r").read()
    for i in orderIdf:
        if i == "+":
            break
        orderId = orderId+i  
    target = int(orderIdf[len(orderId)+1:])
    data = {"id":orderId}
    a = fyers.orderbook(data=data)
    obj = a["orderBook"][0]
    status , filledQty , tradedPrice , usymbol , side =  [obj[k] for k in ('status','filledQty','tradedPrice','symbol','side')]
    print(status , filledQty , tradedPrice , usymbol , side)
    return  {
                "status"      :     status , 
                "filledQty"   :     filledQty , 
                "tradedPrice" :     tradedPrice , 
                "usymbol"     :     usymbol, 
                "side"        :     side
            }
    

def trailSlBookProfit(orderData):
    print("here")
    filledQty,tradedPrice,usymbol,limitfactor,triggerlimit,bookProfit,trailToBreakevenL,trailToBreakevenF = [orderData[k] for k in ('filledQty','tradedPrice','usymbol','limitfactor','triggerlimit','bookProfit','trailToBreakevenL','trailToBreakevenF')]


    orderData = {}
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

    response = fyers.place_order(data)
    print(response)
    orderData["id"] = response["id"]
    
    symbol = [str(usymbol)]
    dataType = "symbolData"

    def OnPriceUpdateTrailSL(msg):
        if  msg[0]['ltp'] >=  tradedPrice + (2 * limitfactor):
            data = {
                        "id":orderData["id"], 
                        "type":4, 
                        "limitPrice":tradedPrice+trailToBreakevenL,
                        "stopPrice":tradedPrice+trailToBreakevenF,
                    }

            response = fyers.modify_order(data)
            orderData["id"] = response["id"]
            fyersSocket.websocket_data = OnPriceUpdateBookProfit


    def OnPriceUpdateBookProfit(msg): 
        if  msg[0]['ltp'] >= bookProfit :
            fyers.cancel_order(orderData)
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
            sleep(0.2)
            fyers.place_order(data)
            fyersSocket.websocket_data = None
            

    fyersSocket.websocket_data = OnPriceUpdateTrailSL

    def subscribe_new_symbol(symbol_list):        
        global fyersSocket, data_type
        fyersSocket.subscribe(symbol=symbol_list, data_type=dataType)
        
    t = threading.Thread(target=subscribe_new_symbol, args=(symbol,))
    t.start()
    print("prosses spawned")
    
    while True:
        sleep(30)
                
              


    



 





if __name__ == "__main__":
    while True:
    
        orderIdf = open("orderId.txt", "r").read()
        if orderIdf:
            OrderData = fetchOrderData()
            if OrderData["status"] == 2 and OrderData["side"] == 1 :  
                arr = OrderData["usymbol"].split(':')
                
                if arr[1].startswith('NIFTY'):
                    OrderData["limitfactor"] = 8
                    OrderData["triggerlimit"] = 7
                    OrderData["bookProfit"] = OrderData["tradedPrice"] + 60
                    OrderData["trailToBreakevenL"] = 1
                    OrderData["trailToBreakevenF"] = 2
                
                if arr[1].startswith('BANKNIFTY'):
                    OrderData["limitfactor"] = 20
                    OrderData["triggerlimit"] = 18
                    OrderData["bookProfit"] = OrderData["tradedPrice"] + 120
                    OrderData["trailToBreakevenL"] = 2
                    OrderData["trailToBreakevenF"] = 4

                if arr[1].startswith('TATA'):
                    OrderData["limitfactor"] = 3
                    OrderData["triggerlimit"] = 2
                    OrderData["bookProfit"] = OrderData["tradedPrice"] + 3
                    OrderData["trailToBreakevenL"] = 0.5
                    OrderData["trailToBreakevenF"] = 0.1
                
                p = Process(target=trailSlBookProfit, args=(OrderData,))
                p.start()
                print("spawned")
                print(p)
                fyers_object = open("orderId.txt", "w")
                fyers_object.write("")
                fyers_object.close()
                

        









































