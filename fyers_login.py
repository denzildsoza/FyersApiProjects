
from fyers_api import accessToken
client_id = "3H021OQ8ZI-100"
secret_key = "PPEJLUL3HA"
redirect_uri = "http://127.0.0.1/:5000/login"
session=accessToken.SessionModel(client_id=client_id,secret_key=secret_key,redirect_uri=redirect_uri,response_type="code", grant_type="authorization_code")
response = session.generate_authcode()  
print(response)
auth_code = input("Enter auth code: ")
session.set_token(auth_code)
response = session.generate_token()
access_token = response["access_token"]
print(access_token)


















