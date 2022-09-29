from rest_framework import serializers
from .models import TEST

class TESTING(serializers.ModelSerializer):
    class Meta:
        model = TEST
        fields = ('id','test','content','updated_at')
