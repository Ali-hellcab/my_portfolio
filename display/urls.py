from django.urls import path
from . import views

urlpatterns = [
    path('', views.displaypage, name='display_page'),
    path('send-message/', views.send_message, name='send_message'),
   
]