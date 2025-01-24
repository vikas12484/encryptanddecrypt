from django.db import models



class register(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=11)
    Address=models.CharField(max_length=50)
    Location= models.CharField(max_length=50)
    Code = models.CharField(max_length=6, blank=True, null=True) 

class Login(models.Model):
    Code=models.CharField(max_length=30)
   