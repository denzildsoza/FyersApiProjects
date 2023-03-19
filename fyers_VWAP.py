
from fyers_api import fyersModel,accessToken
from fyers_api.Websocket import ws
from datetime import datetime,timedelta
import pandas_ta as pd

client_id = '3H021OQ8ZI-100'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NjAyNzY2MzMsImV4cCI6MTY2MDM1MDYxMywibmJmIjoxNjYwMjc2NjMzLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaTljLVpRYkw0bkVwOXRMVnA4S2pSdkhYd0d6ME5lT0x5UnVTZDQxN3oxd3hjUmZ0RGVpTWhxMmVvWWREdzhnb0JhYjF4TEY0OEZ3SFBWaUdOMTNMZG1kSzVGRHF1VDNCMGxDcEdpT1QxSVhQcUtpQT0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwiZnlfaWQiOiJYRDA4Njg1IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.PovVWcr9e36tvdeJGAOWTJV7r4Y1FeFx9xxSZTPZRbM'
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="")
from datetime import datetime,timedelta
#current date - 100 days in format yyyy-mm-dd
from_date = datetime.strftime(datetime.now()-timedelta(0),'%Y-%m-%d')
#todays date
to_date = datetime.today().strftime('%Y-%m-%d')
print(from_date)
print(to_date)
data = {"symbol":"NSE:SBIN-EQ","resolution":"15","date_format":"1","range_from":from_date,"range_to":to_date,"cont_flag":"0"}
historical_data = fyers.history(data)
cols = ['DateTime(epochs)','Open','High','Low','Close','Volume']
df = pd.DataFrame.from_dict(historical_data['candles'])
df.columns = cols
close = df['Close'].values

print(df)
ema = df['Close'].ewm(span = 9,adjust=False).mean()
print(ema)
df['Cum_Vol'] = df['Volume'].cumsum()
df['Cum_Vol_Price'] = (df['Volume'] * (df['High'] + df['Low'] + df['Close'] ) /3).cumsum()
df['VWAP'] = df['Cum_Vol_Price'] / df['Cum_Vol']


print(df)



