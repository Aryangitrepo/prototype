from django.db import models

# Create your models here.
class hlo(models.Model):
     username=models.CharField(max_length=120,null=True,blank=True)
     password=models.CharField(max_length=250,null=True,blank=True)
    
    