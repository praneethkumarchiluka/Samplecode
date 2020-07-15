from django.db import models
from django.contrib.auth.models import User

class Details(models.Model):
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    owner=models.ForeignKey(User, on_delete=models.CASCADE)