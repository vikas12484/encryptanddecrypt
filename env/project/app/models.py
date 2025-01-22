from django.db import models



class register(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=11)
    Address=models.CharField(max_length=50)
    Location= models.CharField(max_length=50)

class Login(models.Model):
    Code=models.CharField(max_length=30)
   