from django.http import HttpResponse
from .utils import *


def getTickets(request):
    jsons = json.loads(request.body)
    type = jsons['type']
    dummy = ""
    if type != "All":
        dummy = 'WHERE LOWER(t_ticketcategory.catname) = LOWER(' + f"'{type}'" + ')'
    try:
        con = connectDB()
        cursor = con.cursor()
        print(f'SELECT "tnum", "desc","location","title","price", "catname" FROM t_ticket INNER jOIN t_ticketcategory ON t_ticket.catnum = t_ticketcategory.catnum '+ dummy)
        cursor.execute(f'SELECT "tnum", "desc","location","title","price", "catname" FROM t_ticket INNER jOIN t_ticketcategory ON t_ticket.catnum = t_ticketcategory.catnum '+ dummy)
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(e,jsons["action"])
    finally:
        disconnectDB(con)
    print(resp)
    return resp
    # getUsers

def getTicketInfo(request):
    jsons = json.loads(request.body)
    tnum = jsons['tnum']
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM t_ticket INNER JOIN t_ticketcategory ON t_ticket.catnum = t_ticketcategory.catnum WHERE tnum = {tnum}")
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
            if json['action'] == 'getTickets':
                resp = getTickets(reqeust)
            if json['action'] == 'getTicketInfo':
                resp = getTicketInfo(reqeust)
        except Exception as e:
            resp = str(e)
    print(resp)
    return HttpResponse(resp, content_type="application/json")
