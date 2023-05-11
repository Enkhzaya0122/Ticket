from django.shortcuts import render,redirect
import requests
from django.contrib.auth import logout
import json

def headerBase(request):
    return render(request, "base/headerBase.html")

def index(request):
    if request.session.get('email'):
        if request.method == 'GET':
            type = 'All'
            if request.GET.get('All'):
                type = "All"
            if request.GET.get('jujig'):
                type = "jujig"
            if request.GET.get('bujig'):
                type = "bujig"
            if request.GET.get('concert'):
                type = "concert"
            if request.GET.get('duuri'):
                type = "duuri"
            if request.GET.get('ballet'):
                type = "ballet"
            requestJSON = {
                "action" : "getTickets",
                "type" : f"{type}"
            }
            response = requests.get('http://127.0.0.1:8080/ticket/',
                                    data=json.dumps(requestJSON),
                                    headers={'Content-Type' : 'application/json'})
            resp = json.loads(response.text)
            context = {
                'data' : 
                resp['data'],
                'email' : request.session.get('email'),
                'login' : 1
            }
        if request.method == 'POST':
            type = 'All'
            if request.POST.get('All'):
                type = "All"
            if request.POST.get('jujig'):
                type = "jujig"
            if request.POST.get('bujig'):
                type = "bujig"
            if request.POST.get('concert'):
                type = "concert"
            if request.POST.get('duuri'):
                type = "duuri"
            if request.POST.get('ballet'):
                type = "ballet"
            requestJSON = {
                "action" : "getTickets",
                "type" : f"{type}"
            }
            response = requests.get('http://127.0.0.1:8080/ticket/',
                                    data=json.dumps(requestJSON),
                                    headers={'Content-Type' : 'application/json'})
            resp = json.loads(response.text)
            context = {
                'data' : resp['data'],
                'email' : request.session.get('email'),
                'login' : 1
            }
        print(context.keys())
        return render(request, "index.html",context=context)
    else:
        return redirect('login',context)

def login(request):
    if request.session.get('email'):
        return redirect('index')
    else:
        
        if request.method == "GET":
            email = request.GET.get('email')
            password = request.GET.get('password')
            if email == None and password == None:
                context = {
                'login' : 2
            }
                return render(request, 'login.html',context=context)
            requestJSON = {
                "action" : "login",
                "email" : email,
                "password" : password
            }
            
            response = requests.get('http://127.0.0.1:8080/user/',
                                    data=json.dumps(requestJSON),
                                    headers={'Content-Type' : 'application/json'})
            resp = json.loads(response.text)
            
            if resp['data'] != 'user not found':
                # Create a session for the user
                request.session['email'] = email
                request.session['password'] = password
                
                return redirect('index')
            
            context = {
                'data' : resp['data'],
                'login' : 2
            }
        print(context)
        return render(request, "login.html",context=context)


def detail(request,id):
    context = {}
    if request.method == 'GET':
        requestJSON = {
            "action" : "getTicketInfo",
            "tnum" : f"{id}"
        }
        response = requests.get('http://127.0.0.1:8080/ticket/',
                                data=json.dumps(requestJSON),
                                headers={'Content-Type' : 'application/json'})
        resp = json.loads(response.text)
        context = {
            'data' : 
            resp['data']
        }
    if request.method == 'POST':
        print('post')
    return render(request, "detail.html",context=context)

def register(request):
    context = {
        'login' : 2
    }
    return render(request, "register.html",context=context)

def registerTicket(request,id):
    if request.session.get('email'):
        context = {}
        if request.method == 'GET':
            requestJSON = {
                "action" : "getTicketInfo",
                "tnum" : id
            }
            response = requests.post('http://127.0.0.1:8080/ticket/',
                                    data=json.dumps(requestJSON),
                                    headers={'Content-Type' : 'application/json'})
            resp = json.loads(response.text)
            requestJSON = {
                "action" : "lookupCategory"
            }
            response = requests.post('http://127.0.0.1:8080/ticket/',
                                    data=json.dumps(requestJSON),
                                    headers={'Content-Type' : 'application/json'})
            cate = json.loads(response.text)
            context = {
                'data' : resp['data'],
                'cate' : cate['data']
            }
        if request.method == 'POST':
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            date = request.POST.get('date')
            location = request.POST.get('location')
            price = request.POST.get('price')
            catname = request.POST['catname']
            requestJSON = {
                "action" : "registerTicket",
                "title" : title,
                "desc" : desc,
                "date" : date,
                "location" : location,
                "price" : price,
                "catname" : catname,
                "tnum" : id
            }
            response = requests.post('http://127.0.0.1:8080/ticket/',
                                    data=json.dumps(requestJSON),
                                    headers={'Content-Type' : 'application/json'})
            resp = json.loads(response.text)
            context = {
                'data' : resp['data']
            }
            if resp['data'] == 'success':
                return redirect('ticketAdmin')
        return render(request, "registerTicket.html", context=context)
    else:
        return redirect('login')

def ticketAdmin(request):
    if request.session.get('email'):
        context = {}
        if request.method == 'GET':
            
            type = 'All'
            if request.GET.get('All'):
                type = "All"
            if request.GET.get('jujig'):
                type = "jujig"
            if request.GET.get('bujig'):
                type = "bujig"
            if request.GET.get('concert'):
                type = "concert"
            if request.GET.get('duuri'):
                type = "duuri"
            if request.GET.get('ballet'):
                type = "ballet"
            requestJSON = {
                "action" : "getTickets",
                "type" : f"{type}"
            }
            response = requests.get('http://127.0.0.1:8080/ticket/',
                                    data=json.dumps(requestJSON),
                                    headers={'Content-Type' : 'application/json'})
            resp = json.loads(response.text)
            context = {
                'data' : 
                resp['data']
            }
        if request.method == 'POST':
            type = 'All'
            if request.POST.get('All'):
                type = "All"
            if request.POST.get('jujig'):
                type = "jujig"
            if request.POST.get('bujig'):
                type = "bujig"
            if request.POST.get('concert'):
                type = "concert"
            if request.POST.get('duuri'):
                type = "duuri"
            if request.POST.get('ballet'):
                type = "ballet"
            requestJSON = {
                "action" : "getTickets",
                "type" : f"{type}"
            }
            response = requests.get('http://127.0.0.1:8080/ticket/',
                                    data=json.dumps(requestJSON),
                                    headers={'Content-Type' : 'application/json'})
            resp = json.loads(response.text)
            context = {
                'data' : 
                resp['data']
            }
        print(resp)
        return render(request, "ticketAdmin.html",context=context)
    else:
        return redirect('login')

def delete(request,id):
    if request.method == "POST":
        requestJSON = {
            "action" : "deleteTicket",
            "tnum" : id
        }
        response = requests.get('http://127.0.0.1:8080/ticket/',
                                data=json.dumps(requestJSON),
                                headers={'Content-Type' : 'application/json'})
        resp = json.loads(response.text)
        context = {
            'data' : 
            resp['data']
        }
        if resp['data'] == 'success':
            return redirect('ticketAdmin')
    if request.method == "GET":
        requestJSON = {
            "action" : "getTicketInfo",
            "tnum" : id
        }
        response = requests.get('http://127.0.0.1:8080/ticket/',
                                data=json.dumps(requestJSON),
                                headers={'Content-Type' : 'application/json'})
        resp = json.loads(response.text)
        context = {
            'data' : 
            resp['data']
        }
    return render(request, "delete.html",context=context)

def log_out(request):
    del request.session['email']
    logout(request)

    return redirect('login')


