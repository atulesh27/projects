from django.db import models

class form_model(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    Employeement_type = [
        ('UNEMPLOYEED','unemployeed'),
        ('EMPLOYEED','employeed'),
        ('SERVING','serving')
    ]
    Employeement_type = models.CharField(
        max_length=15,
        choices=Employeement_type,
        default='EMPLOYEED'
    )