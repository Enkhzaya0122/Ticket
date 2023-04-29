from django.http import HttpResponse
from .utils import *


def getUsers(request):
    jsons = json.loads(request.body)
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute("SELECT username FROM t_ticketuser")
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # getUsers

def getUserInfo(request):
    jsons = json.loads(request.body)
    usernum = jsons['usernum']
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM t_ticketuser WHERE usernum = {usernum}")
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # getUserInfo

def mainFunction(reqeust):
    json = checkreg(reqeust)
    if json == False:
        resp = sendResponse('Json болгоход алдаа гарлаа',json)
        return HttpResponse(resp, content_type="application/json")
    else:
        try:
            if json['action'] == 'getUsers':
                resp = getUsers(reqeust)
            if json['action'] == 'getUserInfo':
                resp = getUserInfo(reqeust)
        except Exception as e:
            resp = str(e)
    return HttpResponse(resp, content_type="application/json")
