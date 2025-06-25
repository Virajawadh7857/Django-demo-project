from django.contrib import admin
from .models import student

class Adminstudent(admin.ModelAdmin):
    list_display = ['sno','sname','sloc','image','profile']

admin.site.register(student,Adminstudent)
