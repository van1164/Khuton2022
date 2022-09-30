from django.contrib import admin
from .models import User,Dahwe,TimeTable,subject_table,TEST2,everytime_table,everyinfo_table
# Register your models here.

admin.site.register(User)
admin.site.register(Dahwe)
admin.site.register(TimeTable)
admin.site.register(subject_table)
admin.site.register(TEST2)
admin.site.register(everytime_table)
admin.site.register(everyinfo_table)