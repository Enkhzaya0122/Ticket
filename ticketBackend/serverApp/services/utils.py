import psycopg2
import datetime
import json
import hashlib

def connectDB():
    con = psycopg2.connect(
        dbname = "qrcodegenerator", 
        user = "qruser", 
        host = "202.131.254.138", 
        password = "qrcode1234", 
        port = "5938")
    return con

def disconnectDB(con):
    if(con):
        con.close()
    
def sendResponse(data,action):
    response = {}
    response['action'] = action
    response['data'] = data
    response['date'] = datetime.datetime.now()
    response['size'] = len(data)
    return json.dumps(response, sort_keys= True, default=str)

def passHash(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()
#   passHash

def checkreg(request):
    try:
        jsons = json.loads(request.body)
    except Exception as e:
        return e
    return jsons
#   checkreg




