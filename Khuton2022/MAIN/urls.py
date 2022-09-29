from django.contrib import admin
from django.urls import path,include
from MAIN import views

urlpatterns = [
    path('',views.main_page, name = ''),
    path("test",views.select,name='test')
    
    
]