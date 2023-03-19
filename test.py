"NSE:NIFTY2320217600CE"
"NSE:BANKNIFTY2320240200CE"


import calendar
from datetime import date, timedelta
import math



   
for i in range(8):
    my_date = date.today()+timedelta(i)
    a = calendar.day_name[my_date.weekday()]
    if a == 'Thursday':
        expiry_date = my_date
        break

expiryDate = (str(expiry_date).split('-'))
 

def get_ITM_BNF_CE(support_level):
    Level =  (int(math.ceil(support_level / 100.0)) * 100)-200
    print(f"NSE:BANKNIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}CE")
def get_ITM_BNF_PE(resistance_level):
    Level =  (int(math.ceil(resistance_level / 100.0)) * 100)+100
    print(f"NSE:BANKNIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}PE")
def get_ITM_NF_CE(support_level):
    Level =  (int(math.ceil(support_level / 50.0)) * 50)-100
    print(f"NSE:NIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}CE")    
def get_ITM_NF_PE(resistance_level):
    Level =  (int(math.ceil(resistance_level / 50.0)) * 50)+50
    print(f"NSE:NIFTY{expiryDate[0][2:]}{int(expiryDate[1])}{expiryDate[2]}{Level}PE") 
    

get_ITM_BNF_CE(40387)
get_ITM_BNF_PE(40387)
get_ITM_NF_CE()
get_ITM_NF_PE()


