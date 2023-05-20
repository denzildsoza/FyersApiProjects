"NSE:NIFTY2320217600CE"
"NSE:BANKNIFTY2320240200CE"


import calendar
from datetime import date, timedelta,datetime
import  pandas as pd

sym_details = pd.read_csv("https://public.fyers.in/sym_details/NSE_FO.csv")
sym_details.columns =  ['epoch_time','symbol_name','o','h','c','l','exg_time','date','expiry_date','symbol','10','11','underlying_price','underlying_name','underlying','strike_price','call_put','abc']

for i in range(8):
        my_date = date.today()+timedelta(i)
        a = calendar.day_name[my_date.weekday()]
        if a == 'Thursday':
            expiry_date = my_date
            break

for i in range(3):
    expiry_date = expiry_date - timedelta(i)
    expiry_date_epoch =  int((datetime.strptime(f'{expiry_date} 20:00:00', '%Y-%m-%d %H:%M:%S')).timestamp())
    sym_details_temp = sym_details.loc[sym_details['expiry_date'] == expiry_date_epoch]
    if  len(sym_details_temp) != 0 :
        sym_details = sym_details_temp
        break

# for i in range(8):
#     my_date = date.today()+timedelta(i)
#     a = calendar.day_name[my_date.weekday()]
#     if a == 'Thursday':
#         expiry_date = my_date
#         break

# expiryDate = (str(expiry_date).split('-'))
 

# def get_ITM_BNF_CE(support_level):
#     Level =  (int(math.ceil(support_level / 100.0)) * 100)-200
#     print(f"NSE:BANKNIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}CE")
# def get_ITM_BNF_PE(resistance_level):
#     Level =  (int(math.ceil(resistance_level / 100.0)) * 100)+100
#     print(f"NSE:BANKNIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}PE")
# def get_ITM_NF_CE(support_level):
#     Level =  (int(math.ceil(support_level / 50.0)) * 50)-100
#     print(f"NSE:NIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}CE")    
# def get_ITM_NF_PE(resistance_level):
#     Level =  (int(math.ceil(resistance_level / 50.0)) * 50)+50
#     print(f"NSE:NIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}PE") 
    

# get_ITM_BNF_CE(40387)
# get_ITM_BNF_PE(40387)
# get_ITM_NF_CE()
# get_ITM_NF_PE()




def get_ITM(level,UnDL,CP,bool):   
    global sym_details 
    optionsData = sym_details
    optionsData = optionsData.loc[optionsData['underlying_name'] == UnDL]
    optionsData = optionsData.loc[optionsData['call_put'] == CP]
    optionsData = optionsData.sort_values('strike_price', ascending= bool)
    if CP == 'CE':
        optionsData = optionsData.loc[optionsData['strike_price'] < int(level)]
    else:
        optionsData = optionsData.loc[optionsData['strike_price'] > int(level)]   
    return optionsData["symbol"].tolist()[0]




print(get_ITM(39400,'BANKNIFTY','CE',False))
print(get_ITM(39400,'BANKNIFTY','PE',True))


print(get_ITM(18900,'NIFTY','CE',False))
print(get_ITM(18900,'NIFTY','PE',True))