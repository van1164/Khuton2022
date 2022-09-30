
# Create your views here.
from django.shortcuts import render,redirect
from django.http import Http404, JsonResponse
from django.utils import timezone
from django.contrib import messages
from requests import Response
from rest_framework.views import APIView
from .models import TEST2,subject_table,User
from .serializers import TESTING
from django.core import serializers
from rest_framework import generics
import pandas as pd

class MiseListCreate(generics.ListCreateAPIView):
    queryset = TEST2.objects.all()
    serializer_class = TESTING
    
class test(generics.ListCreateAPIView):
    queryset = TEST2.objects.all()
    serializer_class = TESTING

class login(generics.ListCreateAPIView):
    
    
    queryset = TEST2.objects.all()
    serializer_class = TESTING


def main_login(request):
    print(request.POST)
    if request.method =="POST":
        uid = request.POST.get("userid",None)
        pw = request.POST.get("password",None)
        if User.objects.filter(User_ID=uid).exists():
            n = User.objects.get(User_ID=uid)
            if n.User_password == pw:
                queryset = User.objects.filter(User_ID=uid)
                print(queryset)
                queryset_json = serializers.serialize('json',queryset,fields = ('Professor','User_ID','User_password','User_name','User_email','Nick_Name','Hakgwa','score','Win','Hakbun'))
                return JsonResponse(queryset_json,safe=False)
            else:
                return JsonResponse({'error':True})
        else:
            return JsonResponse({'error':True})
    else:
        return JsonResponse({'error':True})
    
"""
def making(request):
    subjects = pd.read_csv('subject.csv')

    for a,i in subjects.iterrows():
        subject = subject_table.objects.create()
        subject.물리학및실험1 = i[2]
        subject.미분적분학 = i[3]
        subject.선형대수 = i[4]
        subject.확률및랜덤변수 = i[5]
        subject.미분방정식 = i[6]
        subject.이산구조 = i[7]
        subject.디자인적사고 = i[8]
        subject.웹파이선프로그래밍 = i[9]
        subject.객체지향프로그래밍 = i[10]
        subject.논리회로 = i[11]
        subject.컴퓨터구조 = i[12]
        subject.자료구조 = i[13]
        subject.운영체제 = i[14]
        subject.컴퓨터네트워크 = i[15]
        subject.소프트웨어공학 = i[16]
        subject.알고리즘분석 = i[17]
        subject.데이터베이스 = i[18]
        subject.오픈소스SW개발 = i[19]
        subject.IT기술영어1 = i[20]
        subject.IT기술영어2 = i[21]
        subject.IT기술영어3 = i[22]
        subject.캡스톤디자인1 = i[23]
        subject.캡스톤디자인2 = i[24]
        subject.졸업논문 = i[25]
        subject.기계학습 = i[26]
        subject.신호와시스템 = i[27]
        subject.문제해결 = i[28]
        subject.형식언어및컴파일러 = i[29]
        subject.파일처리 = i[30]
        subject.멀티미디어시스템 = i[31]
        subject.시스템분석및설계 = i[32]
        subject.프로그래밍언어구조론 = i[33]
        subject.SW스타트업비즈니스 = i[34]
        subject.SW스타트업프로젝트 = i[35]
        subject.최신기술프로젝트1 = i[36]
        subject.최신기술프로젝트2 = i[37]
        subject.최신기술콜로키움1 = i[38]
        subject.최신기술콜로키움2 = i[39]
        subject.단기현장실습 = i[40]
        subject.장기현장실습 = i[41]
        subject.연구연수활동1 = i[42]
        subject.연구연수활동2 = i[43]
        subject.독립심화학습1 = i[44]
        subject.독립심화학습2 = i[45]
        subject.인공지능 = i[46]
        subject.빅데이터프로그래밍 = i[47]
        subject.클라우드컴퓨팅 = i[48]
        subject.데이터센터프로그래밍 = i[49]
        subject.정보보호 = i[50]
        subject.모바일프로그래밍 = i[51]
        subject.웹서비스프로그래밍 = i[52]
        subject.리눅스시스템프로그래밍 = i[53]
        subject.IoT디지털시스템 = i[54]
        subject.IoT소프트웨어 = i[55]
        subject.로봇스프트웨어 = i[56]
        subject.영상처리 = i[57]
        subject.컴퓨터그래픽스 = i[58]
        subject.멀티미디어처리 = i[59]
        subject.인간컴퓨터상호작용 = i[60]
        subject.UI_UX프로그래밍 = i[61]
        subject.컴퓨터비전 = i[62]
        subject.AI네트워킹 = i[63]
        subject.IoT네트워크 = i[64]
        subject.딥러닝 = i[65]
        subject.실전기계학습 = i[66]
        subject.save()
"""


def test_main(request):
    queryset = TEST2.objects.all()
    queryset_json = serializers.serialize('json',queryset,fields = ('id','test','content','updated_at'))
    return JsonResponse(queryset_json,safe=False)


def main_page(request):
    user_id = request.session.get('user')
    data = {'login':False} 
    if user_id:
        data['login'] = True
        n = Account.objects.get(user_id=user_id)
        data['name'] = n.name
        data['id'] = n.user_id
        data['star_address'] = n.star_address.split(',')
        inte = interior.objects.all()
        data['interior'] = inte
        lst = interior.objects.filter(user_id = user_id)
        data['my_interior'] = lst
        go_lst =[]
        idx = n.interior.split(',')
        user_inte = []
        for i in idx:
            if i =='' or i ==' ':
                continue
            go_lst.append(interior.objects.get(id = i))
            user_inte.append(int(i))
        data['go_interior'] = go_lst
        data['user_inte'] = user_inte
        return render(request,'chaeum_app/main.html',data)
    else:
        return render(request,'chaeum_app/login.html',{'error':False})


def verify(request):
    if request.method =="POST":
        uid = request.POST.get("userid",None)
        pw = request.POST.get("password",None)
        if Account.objects.filter(user_id=uid).exists():
            n = Account.objects.get(user_id=uid)
            if n.password == pw:
                request.session['user'] = uid
                return redirect('')
            else:
                return render(request,'chaeum_app/login.html',{'error':True})
        else:
            return render(request,'chaeum_app/login.html',{'error':True})
    else:
        return render(request,'chaeum_app/login.html',{'error':True})

def login(request):
    return render(request, 'chaeum_app/login.html',{'error':False})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/Main')

def go_to_create_interior(request):
    return render(request,'chaeum_app/create_interior.html',{})


def create_interior(request):
    if request.method =="POST":
        user_id = request.session['user']
        title = request.POST.get("title",None)
        start_date = request.POST.get("start",None)
        end_date = request.POST.get("end",None)
        address = request.POST.get("address",None)
        job_list = [request.POST.get("job_1",''), request.POST.get("job_2",''), request.POST.get("job_3",''), request.POST.get("job_4",'')]
        job =[]
        for i in job_list:
            if i =='':
                continue
            else:
                job.append(i)
                
        job =",".join(job)
        interior.objects.create(user_id = user_id,interior_name = title,start_date=start_date,end_date=end_date, address=address,job =job)

        
    return redirect('/Main')
def register(request):
    return render(request,'chaeum_app/register.html',{'perror':True,'ierror':True})
#회원가입 확인
def create_account(request):
    data = {"perror":True, "ierror":True}
    if request.method =="POST":
        if request.POST.get("InputPassword") != request.POST.get("RepeatPassword"):
            data["perror"] = False
            return render(request,'chaeum_app/register.html',data)
        if Account.objects.filter(user_id=request.POST.get("Inputid")).exists():
            data["ierror"]=False
            return render(request,'chaeum_app/register.html',data)
        name= request.POST.get("FirstName") +request.POST.get("LastName")
        email = request.POST.get("InputEmail")
        id =request.POST.get("Inputid")
        password = request.POST.get("InputPassword")
        Account.objects.create(user_id=id,password = password,email=email,name =name)
        return redirect('/login')

def admit(request):
    if request.method =="GET":
        user_id = request.GET.get("user_id")
        inte_id = request.GET.get("inte_id")
        acc = Account.objects.get(user_id=user_id)
        acc.interior = acc.interior+inte_id+", "
        acc.save()
        inte =interior.objects.get(id =inte_id)
        inte.admit_user = user_id
        inte.save()
        messages.warning(request, "신청되었습니다.")
        return redirect('/Main')

def show_profile(request):
    data = dict()
    if request.method =="GET":
        print(request.GET)
        user_id = request.GET.get("user_id")
        inte_id = request.GET.get("inte_id")
        print(user_id)
        user =Account.objects.get(user_id = user_id)
        data['user'] = user
        data['time'] = str(len(user.interior.split(',')))
        data['inte_id'] = inte_id
    return render(request,'chaeum_app/show_profile.html',data)

def select(request):
    if request.method =="GET":
        print(request.GET)
        user_id = request.GET.get("user_id")
        inte_id = request.GET.get("inte_id")
        inte =interior.objects.get(id = inte_id)
        inte.matching = True
        inte.save()
    return redirect('/Main')

def send_to_mobile(request):
    data = []
    lst = interior.objects.all()
    for item in lst:
        dic = dict()
        dic['location']=item.address
        dic['jobGroup']=item.job
        dic['endDate']=item.end_date
        dic['startDate']=item.start_date
        data.append(dic)

    return JsonResponse(data,safe=False)