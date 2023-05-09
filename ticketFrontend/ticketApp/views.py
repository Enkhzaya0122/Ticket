from django.shortcuts import render,redirect
import requests
import json

def headerBase(request):
    return render(request, "base/headerBase.html")

def index(request):
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
    return render(request, "index.html",context=context)

def login(request):
    if request.method == "GET":
        email = request.GET.get('email')
        password = request.GET.get('password')
        if email == None and password == None:
            return render(request, 'login.html')
        requestJSON = {
            "action" : "login",
            "email" : email,
            "password" : password
        }
        
    
        response = requests.get('http://127.0.0.1:8080/user/',
                                data=json.dumps(requestJSON),
                                headers={'Content-Type' : 'application/json'})
        resp = json.loads(response.text)
        context = {
            'data' : resp['data']
        }
    if resp['data']!= 'user not found':
        return redirect('index')
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
    return render(request, "register.html")

def registerTicket(request,id):
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
        context = {
            'data' : resp['data']
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
            return redirect('index')
    return render(request, "registerTicket.html", context=context)

def ticketAdmin(request):
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

