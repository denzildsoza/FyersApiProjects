from fyers_api import fyersModel
from datetime import timedelta,date
import email,imaplib,calendar,threading,calendar
from fyers_api.Websocket import ws
from multiprocessing import Process
from datetime import timedelta,date,datetime
from time import sleep
import  pandas as pd

base  = 25000   #<------------------------------------------------------------------------------------------------------Base Level
processes = {}
sym_details = pd.read_csv("https://public.fyers.in/sym_details/NSE_FO.csv")
sym_details.columns =  ['epoch_time','symbol_name','o','h','c','l','exg_time','date','expiry_date','symbol','10','11','underlying_price','underlying_name','underlying','strike_price','call_put','abc','None']
access_token_file = open("/f/Logs/access_token.txt", "r")
access_token = access_token_file.read()
client_id = '3H021OQ8ZI-100'
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="/f/Logs/logs" )
# /f/Logs D:\Python Projects\hello_api\Logs
ws_access_token = f"3H021OQ8ZI-100:{access_token}"
data_type = "symbolData"
run_background = False
fyersSocket = ws.FyersSocket(access_token=ws_access_token,run_background=False,log_path="/f/Logs/logs")

def filterWeeklyexpiry():
    for i in range(8):
            my_date = date.today()+timedelta(i)
            a = calendar.day_name[my_date.weekday()]
            if a == 'Thursday':
                expiry_date = my_date
                break
    for i in range(10):
        expiry_date = expiry_date - timedelta(i)
        expiry_date_epoch =  int((datetime.strptime(f'{expiry_date} 20:00:00', '%Y-%m-%d %H:%M:%S')).timestamp())
        sym_details_temp = sym_details.loc[sym_details['expiry_date'] == expiry_date_epoch]
        if  len(sym_details_temp) != 0 :
            return sym_details_temp

def get_ITM(sym_details,level,UnDL,CP,bool):   
    optionsData = sym_details
    optionsData = optionsData.loc[optionsData['underlying_name'] == UnDL]
    optionsData = optionsData.loc[optionsData['call_put'] == CP]
    optionsData = optionsData.sort_values('strike_price', ascending= bool)
    if CP == 'CE':
        optionsData = optionsData.loc[optionsData['strike_price'] < int(level)]
    else:
        optionsData = optionsData.loc[optionsData['strike_price'] > int(level)]   
    return optionsData["symbol"].tolist()[0]


def check_mail():
    try:
        username = "niftyfifty3661@gmail.com"
        password = "exhxzazbmkwsrrzv"
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
    except:
        my_message = {}
    return(my_message)


def thread_Rapper(objc):
    def doNothing(msg):
        pass

    level,usymbol,highl,lowl,UNdl_ToKen,qty,target,typ,dir =  [objc[k] for k in ('level','symbol','h_LeVel','l_LeVel','UNdl_ToKen','qty','target','typ',"dir")]
    def onCrossing(msg): 
        if  msg[0]['ltp'] <= highl and msg[0]['ltp'] >= lowl :
                fyersSocket.websocket_data = doNothing
                data = {
                            "symbol":usymbol,
                            "qty":qty,
                            "type":2, 
                            "side":1,
                            "productType":"MARGIN",
                            "limitPrice":0,
                            "stopPrice":0,
                            "validity":"DAY",
                            "disclosedQty":0,
                            "offlineOrder":"False",
                            "stopLoss":0,
                            "takeProfit":0
                        }
                x = fyers.place_order(data)
                print("placed")
                OrderId = x['id']
                fyers_object = open("/f/Logs/orderId.txt", "w")
                fyers_object.write(f'{OrderId}+{target}')
                fyers_object.close()
                 


    def onCloseCall(msg):
        if (msg[0]["timestamp"] % 3600 // 60) % 15 == 0 and msg[0]["ltp"] >= level:
            fyersSocket.websocket_data = onCrossing
            print("closed call")
                
    def onClosePut(msg):
        if (msg[0]["timestamp"] % 3600 // 60) % 15 == 0 and msg[0]["ltp"] <= level:
            fyersSocket.websocket_data = onCrossing
            print("closed put")

    if typ == "o" and dir == "s":
        fyersSocket.websocket_data = onCloseCall
    if typ == "o" and dir == "r":
        fyersSocket.websocket_data = onClosePut
    if typ == "c" :
        fyersSocket.websocket_data = onCrossing
    def subscribe_new_symbol(symbol_list):        
        global fyersSocket, data_type
        fyersSocket.subscribe(symbol=symbol_list, data_type=data_type)  
    t = threading.Thread(target=subscribe_new_symbol, args=([UNdl_ToKen],))
    t.start()
    while True:   
        sleep(20)     





if __name__ == "__main__":
    k = 0
    sym_details = filterWeeklyexpiry()
    while True:     
        Level = check_mail()
        if(Level):
            temparray = Level['body'].split()
            if len(temparray) == 6:
                entrylevel = eval(temparray[5])
            else:
                entrylevel = eval(temparray[0])
            if len(temparray) == 2 and temparray[1] == 'c':
                pinstance = processes[temparray[0]]
                print("processes")
                pinstance.terminate()
            else:
                if  temparray[1].lower() == 's' and  eval(temparray[0]) <= base:
                    ITM = get_ITM(sym_details,eval(temparray[0]),'NIFTY','CE',False)
                    UNdl_ToKen = 'NSE:NIFTY50-INDEX'
                    h_LeVel = entrylevel+1
                    l_LeVel = entrylevel-5
                    qty = int(temparray[2])
                    target = int(temparray[3])
                elif  temparray[1].lower() == 's' and  eval(temparray[0]) >= base:
                    ITM = get_ITM(sym_details,eval(temparray[0]),'BANKNIFTY','CE',False)
                    UNdl_ToKen = 'NSE:NIFTYBANK-INDEX'
                    h_LeVel =  entrylevel+2
                    l_LeVel =  entrylevel-10
                    qty = int(temparray[2])
                    target = int(temparray[3])
                elif  temparray[1].lower() == 'r' and  eval(temparray[0]) <= base:
                    ITM = get_ITM(sym_details,eval(temparray[0]),'NIFTY','PE',True)
                    UNdl_ToKen = 'NSE:NIFTY50-INDEX'
                    h_LeVel =  entrylevel+5
                    l_LeVel =  entrylevel-1
                    qty = int(temparray[2])
                    target = int(temparray[3])
                elif  temparray[1].lower() == 'r' and  eval(temparray[0]) >= base:
                    ITM = get_ITM(sym_details,eval(temparray[0]),'BANKNIFTY','PE',True)
                    UNdl_ToKen = 'NSE:NIFTYBANK-INDEX'
                    h_LeVel =  entrylevel+10
                    l_LeVel =  entrylevel-2
                    qty = int(temparray[2])
                    target = int(temparray[3])
                tempobj = { 'level':eval(temparray[0]) ,  'symbol' : ITM , 'h_LeVel' : h_LeVel , 'l_LeVel' : l_LeVel ,'UNdl_ToKen':UNdl_ToKen,'qty':qty,'target':target,"typ":temparray[4].lower(),"dir":temparray[1].lower()}
                p = Process(target=thread_Rapper, args=(tempobj,))
                p.start()
                processes[f'{k}']=p
                k+=1
                print(processes)
        
            
        
































































































































































