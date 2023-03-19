from fyers_api import fyersModel
from datetime import timedelta,date
import email,imaplib,calendar,threading,calendar
from fyers_api.Websocket import ws
from multiprocessing import Process
from datetime import timedelta,date
from time import sleep
from json import load,dumps
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

def check_mail():
    
    
    username = "fiftyfifty.tradingalgo@gmail.com"
    password = "vkiebhsxopoeuakv"
    host =  'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select('inbox')
    key = 'FROM'
    value = 'denzildsouza3661@gmail.com'
    _,searchdata = mail.search(None,key,value,'UNSEEN')
    my_message = {}
    for num in searchdata[0].split():
        email_data = {}
        _,data = mail.fetch(num , '(RFC822)')
        _,b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject','to','from','date','body']:   
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message= email_data
    
    return(my_message)



#           <   --  Global Variable Declerations        --    >

access_token_file = open("access_token.txt", "r")
access_token = access_token_file.read()
client_id = '3H021OQ8ZI-100'
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="/myApp/Logs") # D:\Python Projects\hello_api\Logs


ws_access_token = f"3H021OQ8ZI-100:{access_token}"
data_type = "symbolData"
run_background = False


fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="/myApp/Logs")

base  = 25000   #<------------------------------------------------------------------------------------------------------Base Level
hd    = -2






# <--------------------Take Input for the levels--------------------->

            
      







def thread_Rapper(objc):
    live_data = {}
    
    _,usymbol,highl,lowl,UNdl_ToKen,qty,target =  [objc[k] for k in ('level','symbol','h_LeVel','l_LeVel','UNdl_ToKen','qty','target')]

    def custom_message_Thread(msg): 
        
        live_data['ltp'] = msg[0]['ltp']
        
            
    fyersSocket.websocket_data = custom_message_Thread

    def subscribe_new_symbol(symbol_list):        
        global fyersSocket, data_type
        fyersSocket.subscribe(symbol=symbol_list, data_type=data_type)
        
    t = threading.Thread(target=subscribe_new_symbol, args=([UNdl_ToKen],))
    t.start()
    print(usymbol)
    while True:
        
        if live_data:
            
            if  live_data['ltp'] <= highl and live_data['ltp'] >= lowl :
            
                print("Satisfied")
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
                x = fyers.place_order(data)
                print(x)
                orderId = x['id']
                
                with open('Positions.json', 'r') as openfile:
                    json_object = load(openfile)
                # Writing to sample.json
                
                JsonObj =  {
                    "orderId":orderId,
                    "target" :target,
                }
                
                json_object.append(JsonObj)
                with open("Positions.json", "w") as outfile:
                    outfile.write(dumps(json_object,indent=4))
                
                break
            sleep(0.2)
        
 



if __name__ == "__main__":
    for i in range(8):
        my_date = date.today()+timedelta(i)
        a = calendar.day_name[my_date.weekday()]
        if a == 'Thursday':
            expiry_date = my_date
            break

    expiryDate = (str(expiry_date).split('-'))
    i = 0
    with open("Positions.json", "w") as outfile:
        outfile.write(dumps([], indent=4))
    while True:
       
        Level = check_mail()
        if(Level):
            
            temparray = Level['body'].split()
            if len(temparray) == 2 and temparray[1] == 'c':
                pinstance = processes[temparray[0]]
                print(processes)
                pinstance.terminate()
            else:
                if  temparray[1].lower() == 's' and  eval(temparray[0]) <= base:
                    ITM = get_ITM_NF_CE( int(temparray[0]))
                    UNdl_ToKen = 'NSE:NIFTY50-INDEX'
                    h_LeVel =  int(temparray[0])+3
                    l_LeVel =  int(temparray[0])-3
                    qty = int(temparray[2])
                    target = int(temparray[3])
                    target = int(temparray[3])
                elif  temparray[1].lower() == 's' and  int(temparray[0]) >= base:
                    ITM = get_ITM_BNF_CE( int(temparray[0]))
                    UNdl_ToKen = 'NSE:NIFTYBANK-INDEX'
                    h_LeVel =  int(temparray[0])+6
                    l_LeVel =  int(temparray[0])-6
                    qty = int(temparray[2])
                    target = int(temparray[3])
                elif  temparray[1].lower() == 'r' and  int(temparray[0]) <= base:
                    ITM = get_ITM_NF_PE( int(temparray[0]))
                    UNdl_ToKen = 'NSE:NIFTY50-INDEX'
                    h_LeVel =  int(temparray[0])+3
                    l_LeVel =  int(temparray[0])-3
                    qty = int(temparray[2])
                    target = int(temparray[3])
                elif  temparray[1].lower() == 'r' and  int(temparray[0]) >= base:
                    ITM = get_ITM_BNF_PE( int(temparray[0]))
                    UNdl_ToKen = 'NSE:NIFTYBANK-INDEX'
                    h_LeVel =  int(temparray[0])+6
                    l_LeVel =  int(temparray[0])-6 
                    qty = int(temparray[2])
                    target = int(temparray[3])
                tempobj = { 'level':int(temparray[0]) , 'symbol' : ITM , 'h_LeVel' : h_LeVel , 'l_LeVel' : l_LeVel ,'UNdl_ToKen':UNdl_ToKen,'qty':qty,'target':target}
                p = Process(target=thread_Rapper, args=(tempobj,))
                p.start()
                processes[f'{i}']=p
                i+=1
           
        
            
        
































































































































































