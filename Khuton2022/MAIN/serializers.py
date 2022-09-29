from rest_framework import serializers
from .models import TEST2

class TESTING(serializers.ModelSerializer):
    class Meta:
        model = TEST2
        fields = ('id','test','content','updated_at')
