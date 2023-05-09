
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('headerBase/', views.headerBase, name="headerBase"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('ticketAdmin/', views.ticketAdmin, name="ticketAdmin"),
    path('registerTicket/<int:id>', views.registerTicket, name="registerTicket"),
    path('delete/<int:id>', views.delete, name="delete"),
    
]
