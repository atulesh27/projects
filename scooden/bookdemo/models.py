from django.db import models

# Create your models here.

class BookDemoModel(models.Model):
    name = models.CharField(max_length=25)
    course = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)


