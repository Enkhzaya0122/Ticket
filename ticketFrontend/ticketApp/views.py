from django.shortcuts import render
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
    return render(request, "login.html")

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
