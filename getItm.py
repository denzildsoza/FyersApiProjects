url = "https://public.fyers.in/sym_details/NSE_FO.csv"
import requests

res = requests.get(url)
print(res.text) 