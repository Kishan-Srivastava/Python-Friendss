from django.db import models
from datetime import date

gender_list = (('M', 'Male'), ('F', 'Female'))
class Person(models.Model):
    name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=1, null=True, blank=False, choices=gender_list)
    birthday = models.DateField(default=date.today)
    email = models.EmailField(max_length=70, blank=False, unique=True, null=True)
    desc = models.TextField(max_length=100, blank=True)
    photo = models.FileField(upload_to='images/',null=True, blank=True)


    def __str__(self):
        return '%s'%(self.name)