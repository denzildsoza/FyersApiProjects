from fyers_api import fyersModel
from time import sleep
from fyers_api.Websocket import ws
import threading
from multiprocessing import Process


access_token_file = open("/f/Logs/access_token.txt", "r")
access_token = access_token_file.read()
client_id = '3H021OQ8ZI-100'
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="/f/Logs/logs")
ws_access_token = f"3H021OQ8ZI-100:{access_token}"
fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="/f/Logs/logs")
orderUpdateData = []
data_type = "orderUpdate"  
run_background  = False

def fetchOrderData(orderData):
    orderId = ""    
    for i in orderData:
        if i == "+":
            break
        orderId = orderId+i  
    print(orderId)
    target = int(orderData[len(orderId)+1:])
    data = {"id":orderId}
    response = fyers.orderbook(data=data)
    print(response)
    obj = response["orderBook"][0]
    status , filledQty , tradedPrice , usymbol , side =  [obj[k] for k in ('status','filledQty','tradedPrice','symbol','side')]
    print(status , filledQty , tradedPrice , usymbol , side)
    fyers_object = open("/f/Logs/orderId.txt", "w")
    fyers_object.write("")
    fyers_object.close()
    return  {
                "status"      :     status , 
                "filledQty"   :     filledQty , 
                "tradedPrice" :     tradedPrice , 
                "usymbol"     :     usymbol, 
                "side"        :     side
            }
    
def trailSlBookProfit(orderData):
    def doNothing(msg):
        pass
    print("here")
    filledQty,tradedPrice,usymbol,limitfactor,triggerlimit,bookProfit,trailToBreakevenL,trailToBreakevenF = [orderData[k] for k in ('filledQty','tradedPrice','usymbol','limitfactor','triggerlimit','bookProfit','trailToBreakevenL','trailToBreakevenF')]
    sleep(1)
    orderData = {}
    data = {
                "symbol":usymbol,
                "qty":filledQty,
                "type":4, 
                "side":-1,
                "productType":"INTRADAY",
                "limitPrice":limitfactor,
                "stopPrice":triggerlimit,
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
            fyersSocket.websocket_data = doNothing
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
    fyersSocket.websocket_data = OnPriceUpdateBookProfit

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
        orderIdf = open("/f/Logs/orderId.txt", "r").read()
        if orderIdf:
            OrderData = fetchOrderData(orderIdf)
            if OrderData["status"] == 2 and OrderData["side"] == 1 :  
                arr = OrderData["usymbol"].split(':')
                if arr[1].startswith('NIFTY'):
                    OrderData["limitfactor"] =OrderData["tradedPrice"]+ 6
                    OrderData["triggerlimit"] =OrderData["tradedPrice"]+ 5
                    OrderData["bookProfit"] = OrderData["tradedPrice"] + 12
                    OrderData["trailToBreakevenL"] = OrderData["tradedPrice"]+1
                    OrderData["trailToBreakevenF"] = OrderData["tradedPrice"]+2
                if arr[1].startswith('BANKNIFTY'):
                    OrderData["limitfactor"] = OrderData["tradedPrice"]+12
                    OrderData["triggerlimit"] =OrderData["tradedPrice"]+ 10
                    OrderData["bookProfit"] = OrderData["tradedPrice"] + 50
                    OrderData["trailToBreakevenL"] =OrderData["tradedPrice"]+2
                    OrderData["trailToBreakevenF"] =OrderData["tradedPrice"]+4               
                p = Process(target=trailSlBookProfit, args=(OrderData,))
                p.start()
                print("spawned")
                print(p)
        sleep(1)        

        









































