from django.db import models

class student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20)
    sloc = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    profile = models.FileField(upload_to='files')
    def __str__(self):
        return self.sname

