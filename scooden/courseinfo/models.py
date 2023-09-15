from django.db import models

# Create your models here.

class CourseInfoModel(models.Model):
    cname = models.CharField(max_length=25)
    cduration = models.FloatField()
    cfees = models.IntegerField()
    cmentor = models.CharField(max_length=20)


#Registration :

class StudRegistration(models.Model):
    sname = models.CharField(max_length=20)
    smobile = models.CharField(max_length=10)
    semail = models.EmailField()
    Saddress = models.TextField()

