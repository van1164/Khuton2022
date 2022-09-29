from django.contrib import admin
from django.urls import path,include
from MAIN import views

urlpatterns = [
    path('',views.test_main, name = ''),
    path("test",views.test,name='test'),
    path('app01/map_main', views.MiseListCreate.as_view()),
    path('app02/map_main', views.MiseListCreate),
    
    
]