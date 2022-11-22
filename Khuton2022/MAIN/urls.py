from django.contrib import admin
from django.urls import path,include
from MAIN import views

urlpatterns = [
    path('',views.new_main, name = ''),
    path("test",views.test.as_view(),name='test'),
    path('app01/map_main', views.MiseListCreate.as_view()),
    path('app02/map_main', views.MiseListCreate),
    path('making',views.making),
    path('making_subject',views.making_subject_table),
    path('login', views.main_login),
    path('user',views.user_get),
    path('soge',views.create_soge),
    path('time_table',views.create_timetable)
]