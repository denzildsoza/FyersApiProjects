from fyers_api import fyersModel
from datetime import timedelta,date
import calendar,threading
from fyers_api.Websocket import ws
from multiprocessing import Process
from datetime import timedelta,date
from time import sleep,strftime
from math import ceil

base  = 25000   #<------------------------------------------------------------------------------------------------------Base Level
hd    = -2
processes = {}

def get_ITM_BNF_CE(support_level):
    Level =  (int(ceil(support_level / 100.0)) * 100)-200
    return f"NSE:BANKNIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}CE"
def get_ITM_BNF_PE(resistance_level):
    Level =  (int(ceil(resistance_level / 100.0)) * 100)+100
    return f"NSE:BANKNIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}PE"
def get_ITM_NF_CE(support_level):
    Level =  (int(ceil(support_level / 50.0)) * 50)-100
    return f"NSE:NIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}CE"   
def get_ITM_NF_PE(resistance_level):
    Level =  (int(ceil(resistance_level / 50.0)) * 50)+50
    return f"NSE:NIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}PE" 




#           <   --  Global Variable Declerations        --    >

access_token_file = open("access_token.txt", "r")
access_token = access_token_file.read()
client_id = '3H021OQ8ZI-100'
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="/f/Logs") # /f/Logs


ws_access_token = f"3H021OQ8ZI-100:{access_token}"
data_type = "symbolData"
run_background = False


fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="/f/Logs")

base  = 25000   #<------------------------------------------------------------------------------------------------------Base Level
hd    = -2






# <--------------------Take Input for the levels--------------------->

            
      







def thread_Rapper(objc):
    
    usymbol,highl,lowl,UNdl_ToKen,qty =  [objc[k] for k in ('symbol','h_LeVel','l_LeVel','UNdl_ToKen','qty')]
    
    
    def onCrossing(msg): 
        if  msg[0]['ltp'] <= highl and msg[0]['ltp'] >= lowl :
                data = {
                            "symbol":usymbol,
                            "qty":qty,
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
                fyers.place_order(data)
                
                fyersSocket.websocket_data = None
                
                


   

    
    fyersSocket.websocket_data = onCrossing

    def subscribe_new_symbol(symbol_list):        
        global fyersSocket, data_type
        fyersSocket.subscribe(symbol=symbol_list, data_type=data_type)
        
    t = threading.Thread(target=subscribe_new_symbol, args=([UNdl_ToKen],))
    t.start()
    while True:
        
        sleep(20)     

        
 



if __name__ == "__main__":
    for i in range(8):
        my_date = date.today()+timedelta(i)
        a = calendar.day_name[my_date.weekday()]
        if a == 'Thursday':
            expiry_date = my_date
            break

    level = input("Enter the Level: ")        
    expiryDate = (str(expiry_date).split('-'))
        
            
    temparray = level.split()
    
    if  temparray[1].lower() == 's' and  eval(temparray[0]) <= base:
        ITM = get_ITM_NF_CE( eval(temparray[0]))
        UNdl_ToKen = 'NSE:NIFTY50-INDEX'
        h_LeVel =  eval(temparray[0])+3
        l_LeVel =  eval(temparray[0])-3
        qty = int(temparray[2])
    elif  temparray[1].lower() == 's' and  eval(temparray[0]) >= base:
        ITM = get_ITM_BNF_CE( eval(temparray[0]))
        UNdl_ToKen = 'NSE:NIFTYBANK-INDEX'
        h_LeVel =  eval(temparray[0])+6
        l_LeVel =  eval(temparray[0])-6
        qty = int(temparray[2])
    elif  temparray[1].lower() == 'r' and  eval(temparray[0]) <= base:
        ITM = get_ITM_NF_PE( eval(temparray[0]))
        UNdl_ToKen = 'NSE:NIFTY50-INDEX'
        h_LeVel =  eval(temparray[0])+3
        l_LeVel =  eval(temparray[0])-3
        qty = int(temparray[2])
    elif  temparray[1].lower() == 'r' and  eval(temparray[0]) >= base:
        ITM = get_ITM_BNF_PE( eval(temparray[0]))
        UNdl_ToKen = 'NSE:NIFTYBANK-INDEX'
        h_LeVel =  eval(temparray[0])+6
        l_LeVel =  eval(temparray[0])-6 
        qty = int(temparray[2])
    tempobj = { 'symbol' : ITM , 'h_LeVel' : h_LeVel , 'l_LeVel' : l_LeVel ,'UNdl_ToKen':UNdl_ToKen,'qty':qty}
    p = Process(target=thread_Rapper, args=(tempobj,))
    while True:
        timestamp = strftime('%H:%M:%S').split(":")
        if int(timestamp[0]) == 9 and int(timestamp[1]) >= 15:
            break
        elif int(timestamp[0]) >9  :
            break   
    p.start()
           
        
            
        
































































































































































