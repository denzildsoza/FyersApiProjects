# from fyers_api import fyersModel
# from fyers_api import accessToken
# from fyers_api.Websocket import ws
# # import fyers_login

# client_id = "3H021OQ8ZI-100"
# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NjAxMjQwNDEsImV4cCI6MTY2MDE3NzgwMSwibmJmIjoxNjYwMTI0MDQxLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaTgzdUp3Zmt1WDFyUlY0WldUazN3M3gwN0x4QmE3LTFpaDFzbHU4aFhYZTN4MWEtdEc2VExKQmFBOE9CT2VLWmoxOFo2TE9TdEdPTGZXR201REhGREZpbkhQLUpsUkZreXZyM19IZUd2d2VCM3Z1dz0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwiZnlfaWQiOiJYRDA4Njg1IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.l-6LfjatfoMY3ms38tAAYHzpjyIgPYYJl5PMUcmc0Xs"
# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2Nzc4MTUwNDQsImV4cCI6MTY3Nzg4OTgwNCwibmJmIjoxNjc3ODE1MDQ0LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa0FXMEVqbWQ2SW1WSDBhMktONTFVR3k4N2lmNTctVl9ycXQ0LXJZc3VRWTVzRHhrWl9wUDFSZTEyNVJscGNnYnY1SkJDaEtEcWh6dVM4V0tyaFpaUTNrX19yWl9DcksyVHBIUFg2WHJ0MHEzMVdMVT0iLCJkaXNwbGF5X25hbWUiOiJERU5aSUwgRFNPVVpBIiwib21zIjpudWxsLCJmeV9pZCI6IlhEMDg2ODUiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.cTOMkWkIXOZL5YQKPozZ2_KDqllxiy1kSUb2QY4buns"

# fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="/home/Desktop/apiV2")

# # data = {"symbol":"NSE:SBIN-EQ","resolution":"15","date_format":"0","range_from":"1622097600","range_to":"1622097685","cont_flag":"1"}
# # data = {"symbols":"NSE:SBIN-EQ"}
# # print(fyers.quotes(data))


# data = {
#             "id":"12303039291", 
#             "type":4, 
#             "limitPrice":207.5+0.3,
#             "stopPrice":207.5+0.4,
#                     }

# response = fyers.modify_order(data)
# print(response)
from json import load

id = 123457
json_object = [{'id':123456,'target':69},{'id':123457,'target':9}]
# with open('Positions.json', 'r') as openfile:
#             json_object = load(openfile)
for i in json_object:
    if i['id'] == id :
        bookProfit =  i['target']
print(bookProfit)