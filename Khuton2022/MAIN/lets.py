import numpy as np

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from .models import subject_table



sunwu = [1,1,1,4,3,3,2,1,2,3,4,3,4,4,0,0,4,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
current_semester = 5

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))

print(subject_table.objects.all())

max = 0
index = 0
for a,i in data2.iterrows():
  sim = cosine_similarity(sunwu, data2.loc[a][2:])
  if sim > max:
    max = sim 
    index = a

for a, i in enumerate(zip(data2.iloc[index][2:], sunwu)):
  if i[0] <= current_semester and i[0] > 0 and i[1] == 0:
    print(subjects[a])