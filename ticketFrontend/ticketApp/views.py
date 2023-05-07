from django.shortcuts import render

def headerBase(request):
    return render(request, "base/headerBase.html")

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def detail(request):
    return render(request, "detail.html")

def register(request):
    return render(request, "register.html")
