from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.

class TEST(models.Model):
    test= models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.CharField(max_length=50)
    
class TEST2(models.Model):
    test= models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.CharField(max_length=50)