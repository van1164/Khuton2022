from datetime import datetime
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.


class Dahwe(models.Model):
    name =models.CharField(max_length = 30,verbose_name = '대회명')
    start_Date = models.DateField(default=datetime.now, blank=True)
    end_Date = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self) -> str:
        return self.name
    

class User(models.Model):
    Professor = models.BooleanField()
    User_ID = models.CharField(max_length=20,unique=True,verbose_name='아이디')
    User_password=  models.CharField(max_length=20)
    User_name = models.CharField(max_length=16,verbose_name='이름')
    User_email = models.EmailField(max_length=128, unique=True,verbose_name='이메일')
    Nick_Name = models.CharField(max_length=20,unique=True,verbose_name='닉네임')
    Hakgwa = models.CharField(max_length=20,unique=True,verbose_name='학과')
    score = models.DecimalField(max_digits=3,decimal_places=2)
    Win = models.ManyToManyField(Dahwe)
    Hakbun = models.IntegerField(default = 0)
    
    def __str__(self) -> str:
        return str(self.Hakbun) + self.User_name





class subject_table(models.Model):
    subject_code = models.IntegerField(default = 0)
    
class TimeTable(models.Model):
    subject_table = models.ManyToManyField(subject_table)
    job = models.CharField(max_length = 30)
    category = models.IntegerField(default = 0)
    company   = models.IntegerField(default = 0)
    


class TEST2(models.Model):
    test= models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.CharField(max_length=50)