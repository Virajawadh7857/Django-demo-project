from django.db import models

class Reg(models.Model):
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=20,unique=True)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
    def __str__(self):
        return self.username

