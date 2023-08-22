from pyexpat import model
from django.db import models

# Create your models here.
# class Members(models.Model):
    # name=models.CharField(max_length=255)

class Tourism(models.Model):
    fromm =models.CharField(max_length=50)
    to=models.CharField(max_length=50)
    departure=models.DateField()
    returnn=models.DateField()
    adult=models.IntegerField()
    child=models.IntegerField() 
    email=models.EmailField()
    image_x=models.ImageField(upload_to="images")