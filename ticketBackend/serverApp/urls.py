from django.urls import path
from .views import *
from .services import user,ticket

urlpatterns = [
    path('index/', index),
    path('user/', user.mainFunction),
    path('ticket/', ticket.index),
]
