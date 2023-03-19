from fyers_api import accessToken

client_id="3H021OQ8ZI-100"
secret_key="PPEJLUL3HA"
redirect_uri="http://127.0.0.1/:5000/login"
response_type="code"
grant_type="authorization_code"
state="abcdef"

session=accessToken.SessionModel(client_id=client_id,secret_key=secret_key,redirect_uri=redirect_uri, response_type=response_type, grant_type=grant_type,state=state)

response = session.generate_authcode()  
print(response)
auth_code = input("enter auth code")

session.set_token(auth_code)
response = session.generate_token()

access_token = response["access_token"]
print(access_token)
fyers_object = open("access_token.txt", "w")
fyers_object.write(access_token)
fyers_object.close()


# """[{'symbol': 'MCX:GOLD23FEBFUT', 'timestamp': 1675444834, 'fyCode': 7208, 'fyFlag': 2, 'pktLen': 200, 'ltp': 57700.0, 'open_price': 57865.0, 'high_price': 58000.0, 'low_price': 56801.0, 'close_price': 58114.0, 'min_open_price': 57700.0, 'min_high_price': 57700.0, 'min_low_price': 57700.0, 'min_close_price': 57700.0, 'min_volume': 0, 'last_traded_qty': 1, 'last_traded_time': 1675444239, 'avg_trade_price': 5769312, 'vol_traded_today': 40, 'tot_buy_qty': 2, 'tot_sell_qty': 5, 'market_pic': [{'price': 56401.0, 'qty': 1, 'num_orders': 1}, {'price': 56375.0, 'qty': 1, 'num_orders': 1}, {'price': 0.0, 'qty': 0, 'num_orders': 0}, {'price': 0.0, 'qty': 0, 'num_orders': 0}, {'price': 0.0, 'qty': 0, 'num_orders': 0}, {'price': 57699.0, 'qty': 1, 'num_orders': 1}, {'price': 57700.0, 'qty': 1, 'num_orders': 1}, {'price': 58000.0, 'qty': 1, 'num_orders': 1}, {'price': 58300.0, 'qty': 1, 'num_orders': 1}, {'price': 58400.0, 'qty': 1, 'num_orders': 1}]}]"""


