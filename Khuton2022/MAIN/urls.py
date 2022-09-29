from django.contrib import admin
from django.urls import path,include
from MAIN import views

urlpatterns = [
    path('',views.test_main, name = ''),
    path("test",views.select,name='test')
    
    
]