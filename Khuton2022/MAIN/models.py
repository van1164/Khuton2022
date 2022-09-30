from datetime import datetime
from tabnanny import verbose
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
import joblib

# Create your models here.



class User(models.Model):
    SorP = models.BooleanField()
    User_ID = models.CharField(max_length=20,unique=True,verbose_name='아이디')
    User_password=  models.CharField(max_length=20)
    User_name = models.CharField(max_length=16,verbose_name='이름')
    User_email = models.EmailField(max_length=128, unique=True,verbose_name='이메일')
    Nick_Name = models.CharField(max_length=20,unique=True,verbose_name='닉네임')
    Hakgwa = models.CharField(max_length=20,unique=True,verbose_name='학과')
    score = models.DecimalField(max_digits=3,decimal_places=2)
    Win = models.ForeignKey('Dahwe',on_delete=models.CASCADE)
    Hakbun = models.IntegerField(default = 0)
    





class Dahwe(models.Model):
    name =models.CharField(max_length = 30,verbose_name = '대회명')
    start_Date = models.DateField(default=datetime.now, blank=True)
    end_Date = models.DateField(default=datetime.now, blank=True)
    
    
class TimeTable(models.Model):
    subject_table = models.ForeignKey('subject_table',on_delete=models.CASCADE)
    job = models.CharField(max_length = 30)
    category = models.IntegerField(default = 0)
    company   = models.IntegerField(default = 0)
    
class subject_table(models.Model):
    subject_code = models.IntegerField(default = 0)

class TEST2(models.Model):
    test= models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.CharField(max_length=50)