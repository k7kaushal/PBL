from django.db import models
from django.contrib.auth.models import User
from django.http import request
import datetime 


class Profile(models.Model):
    year_choices = [('FE','FE') , ('SE','SE'),('TE','TE'), ('BE','BE')]
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNo = models.PositiveIntegerField(default=0)
    city = models.CharField(default='', max_length=30)
    year = models.CharField(default='FE', max_length=2, choices=year_choices)
    gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f', 'Female'), ('o', 'Other')), blank=True,null=True)                          
    def __str__(self):
        return str(self.pk)

class Post(models.Model):
    type_choices = [('Stationary','Stationary') , ('Notes','Notes'),('Help in Project','Help in Project'), ('Other','Other')]
    # author_fname = models.ForeignKey(Profile.lname, on_delete=models.CASCADE)
    author = models.ManyToManyField(User)
    request1 = models.CharField(default='', max_length=100, null=True)
    type = models.CharField(default='', max_length=20,null=True, choices=type_choices)
    date_posted = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.pk) 