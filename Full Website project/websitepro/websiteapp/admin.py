from django.contrib import admin
from .models import Student

class AdminStudent(admin.ModelAdmin):
    list_display = ['fname','lname','username','password','email','mobile']

admin.site.register(Student,AdminStudent)
