from django.http import HttpResponse
from .utils import *
from rest_framework.decorators import api_view


def getTickets(request):
    jsons = json.loads(request.body)
    type = jsons['type']
    dummy = ""
    if type != "All":
        dummy = 'WHERE LOWER(t_ticketcategory.catname) = LOWER(' + f"'{type}'" + ')'
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f'SELECT "tnum", "desc","location","title","price", "catname", "date" FROM t_ticket INNER jOIN t_ticketcategory ON t_ticket.catnum = t_ticketcategory.catnum '+ dummy)
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

def registerTicket(request):
    jsons = json.loads(request.body)
    title = jsons['title']
    desc = jsons['desc']
    date = jsons['date']
    location = jsons['location']
    price = jsons['price']
    catname = jsons['catname']
    tnum = jsons['tnum']
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT catnum from t_ticketcategory WHERE LOWER(catname) = LOWER('{catname}')")
        catnum = cursor.fetchone()
        if tnum != 0:
            cursor.execute("UPDATE public.t_ticket "
                            f"SET location='{location}', price='{price}', title='{title}', " + '"desc"' + f"='{desc}', date='{date}', catnum='{catnum[0]}' "
                            f"WHERE tnum = '{tnum}';")
        else:
            cursor.execute('INSERT INTO t_ticket('
	                    'tnum, location, price, title, "desc", date, catnum) ' 
	                    f"VALUES (DEFAULT, '{location}', '{price}', '{title}', '{desc}', '{date}', '{catnum[0]}');")
        con.commit()
        resp = sendResponse('success',jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # registerTicket

def deleteTicket(request):
    jsons = json.loads(request.body)
    tnum = jsons['tnum']
    try:
        con = connectDB()
        cursor = con.cursor()
        print(f"DELETE FROM t_ticket WHERE tnum = '{tnum}';")
        cursor.execute(f"DELETE FROM t_ticket WHERE tnum = '{tnum}';")
        con.commit()
        resp = sendResponse('success',jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # registerTicket

def lookupCategory(request):
    jsons = json.loads(request.body)
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT catname FROM t_ticketcategory;")
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # registerTicket

@api_view(['POST','GET'])
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
            if json['action'] == 'registerTicket':
                resp = registerTicket(reqeust)
            if json['action'] == 'deleteTicket':
                resp = deleteTicket(reqeust)
            if json['action'] == 'lookupCategory':
                resp = lookupCategory(reqeust)
        except Exception as e:
            resp = str(e)
    print(resp)
    return HttpResponse(resp, content_type="application/json")
