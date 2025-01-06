from django.db import models

# Create your models here.
class Student(models.Model):
    first_name= models.CharField(max_length=35)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=254)
    DOB= models.DateField()
    grade = models.CharField(max_length=30)
    adress = models.TextField(max_length=300)
    
    def __str__(self):
        return f"{self.first_name}-{self.last_name}"