from django.contrib import admin

from teacher.models import Marks,Subjects
from .models import studentData

admin.site.register(Subjects)
admin.site.register(studentData)
admin.site.register(Marks)