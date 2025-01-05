from django.db import models

# Create your models here.
class Trends(models.Model):
    Style= models.CharField(max_length=35)
    colors = models.CharField(max_length=30)
    number_of_pieces= models.IntegerField()
  
    
    