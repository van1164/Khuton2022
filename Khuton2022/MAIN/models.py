from datetime import datetime
from email.policy import default
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
    point = models.IntegerField(default = 0)
    etc = models.TextField(default = '')
    def __str__(self) -> str:
        return str(self.Hakbun) + self.User_name


class everytime_table(models.Model):
    code = models.CharField(max_length = 30)
    name = models.CharField(max_length = 40)
    professor  = models.CharField(max_length = 30)
    time = models.CharField(max_length = 70)
    distribution = models.CharField(max_length = 30)    


class subject_table(models.Model):
    Student_ID = models.IntegerField(default = -1)
    물리학및실험1 = models.IntegerField(default = 0)
    미분적분학 = models.IntegerField(default = 0)
    선형대수 = models.IntegerField(default = 0)
    확률및랜덤변수 = models.IntegerField(default = 0)
    미분방정식 = models.IntegerField(default = 0)
    이산구조 = models.IntegerField(default = 0)
    디자인적사고 = models.IntegerField(default = 0)
    웹파이선프로그래밍 = models.IntegerField(default = 0)
    객체지향프로그래밍 = models.IntegerField(default = 0)
    논리회로 = models.IntegerField(default = 0)
    컴퓨터구조 = models.IntegerField(default = 0)
    자료구조 = models.IntegerField(default = 0)
    운영체제 = models.IntegerField(default = 0)
    컴퓨터네트워크 = models.IntegerField(default = 0)
    소프트웨어공학 = models.IntegerField(default = 0)
    알고리즘분석 = models.IntegerField(default = 0)
    데이터베이스 = models.IntegerField(default = 0)
    오픈소스SW개발 = models.IntegerField(default = 0)
    IT기술영어1 = models.IntegerField(default = 0)
    IT기술영어2 = models.IntegerField(default = 0)
    IT기술영어3 = models.IntegerField(default = 0)
    캡스톤디자인1 = models.IntegerField(default = 0)
    캡스톤디자인2 = models.IntegerField(default = 0)
    졸업논문 = models.IntegerField(default = 0)
    기계학습 = models.IntegerField(default = 0)
    신호와시스템 = models.IntegerField(default = 0)
    문제해결 = models.IntegerField(default = 0)
    형식언어및컴파일러 = models.IntegerField(default = 0)
    파일처리 = models.IntegerField(default = 0)
    멀티미디어시스템 = models.IntegerField(default = 0)
    시스템분석및설계 = models.IntegerField(default = 0)
    프로그래밍언어구조론 = models.IntegerField(default = 0)
    SW스타트업비즈니스 = models.IntegerField(default = 0)
    SW스타트업프로젝트 = models.IntegerField(default = 0)
    최신기술프로젝트1 = models.IntegerField(default = 0)
    최신기술프로젝트2 = models.IntegerField(default = 0)
    최신기술콜로키움1 = models.IntegerField(default = 0)
    최신기술콜로키움2 = models.IntegerField(default = 0)
    단기현장실습 = models.IntegerField(default = 0)
    장기현장실습 = models.IntegerField(default = 0)
    연구연수활동1 = models.IntegerField(default = 0)
    연구연수활동2 = models.IntegerField(default = 0)
    독립심화학습1 = models.IntegerField(default = 0)
    독립심화학습2 = models.IntegerField(default = 0)
    인공지능 = models.IntegerField(default = 0)
    빅데이터프로그래밍 = models.IntegerField(default = 0)
    클라우드컴퓨팅 = models.IntegerField(default = 0)
    데이터센터프로그래밍 = models.IntegerField(default = 0)
    정보보호 = models.IntegerField(default = 0)
    모바일프로그래밍 = models.IntegerField(default = 0)
    웹서비스프로그래밍 = models.IntegerField(default = 0)
    리눅스시스템프로그래밍 = models.IntegerField(default = 0)
    IoT디지털시스템 = models.IntegerField(default = 0)
    IoT소프트웨어 = models.IntegerField(default = 0)
    로봇스프트웨어 = models.IntegerField(default = 0)
    영상처리 = models.IntegerField(default = 0)
    컴퓨터그래픽스 = models.IntegerField(default = 0)
    멀티미디어처리 = models.IntegerField(default = 0)
    인간컴퓨터상호작용 = models.IntegerField(default = 0)
    UI_UX프로그래밍 = models.IntegerField(default = 0)
    컴퓨터비전 = models.IntegerField(default = 0)
    AI네트워킹 = models.IntegerField(default = 0)
    IoT네트워크 = models.IntegerField(default = 0)
    딥러닝 = models.IntegerField(default = 0)
    실전기계학습 = models.IntegerField(default = 0)
    
    
class TimeTable(models.Model):
    subject_table = models.ManyToManyField(subject_table)
    job = models.CharField(max_length = 30)
    category = models.IntegerField(default = 0)
    company   = models.IntegerField(default = 0)
    


class TEST2(models.Model):
    test= models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.CharField(max_length=50)