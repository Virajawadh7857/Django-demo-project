from django.db import models

class Reg(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    def __str__(self):
       return self.username