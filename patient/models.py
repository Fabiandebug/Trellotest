from django.db import models

# Create your models here.

class p_users(models.Model):
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=11)
    



    def __str__(self) :
       return  self.first_name

    
