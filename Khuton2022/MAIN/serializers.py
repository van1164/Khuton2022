from rest_framework import serializers
from .models import TEST2,User


class SER_USER(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ('Professor','User_ID','User_password','User_name','User_email','Nick_Name','Hakgwa','score','Win','Hakbun')
        



class TESTING(serializers.ModelSerializer):
    class Meta:
        model = TEST2
        fields = ('id','test','content','updated_at')
