from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class TEST(models.Model):
    test= models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now =True)