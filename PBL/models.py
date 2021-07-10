from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    year_choices = [('FE','FE') , ('SE','SE'),('TE','TE'), ('BE','BE')]
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNo = models.PositiveIntegerField(default=0)
    city = models.CharField(default='', max_length=30)
    year = models.CharField(default='FE', max_length=2, choices=year_choices)
    fname = models.CharField(default='',max_length=20)
    lname = models.CharField(default='',max_length=20)
    email = models.EmailField(default='',max_length=20)
    gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f', 'Female'), ('o', 'Other')), blank=True,null=True)
                              
     
    def __str__(self):
        return self.userId

