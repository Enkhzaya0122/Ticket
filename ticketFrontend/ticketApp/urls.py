
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('headerBase/', views.headerBase, name="headerBase"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('ticketAdmin/', views.ticketAdmin, name="ticketAdmin"),
    
]
