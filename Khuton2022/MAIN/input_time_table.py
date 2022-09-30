import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()
import pandas as pd
from models import everytime_table


subjects = pd.read_excel('subject.xls',encoding = 'utf-8')

for a,i in subjects.iterrows():
    subject = everytime_table.objects.create()
    subject.code = i[0]
    subject.name = i[1]
    subject.professor = i[2]
    subject.time = i[3]
    subject.distribution = i[4]
    subject.save()