from django.db import models

# Create your models here.
class Gadgets(models.Model):
    model_name= models.CharField(max_length=35)
    model_type = models.CharField(max_length=30)
    model_cost = models.IntegerField()
  
    
    def __str__(self):
        return f"{self.model_name}"