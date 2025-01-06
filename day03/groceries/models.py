from django.db import models

# Create your models here.
class Items(models.Model):
    Name= models.CharField(max_length=35)
    Brand = models.CharField(max_length=30)
    cost= models.IntegerField()
  
    
    