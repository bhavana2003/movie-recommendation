from django.db import models

# Create your models here.

class Movie(models.Model):
  title = models.CharField(max_length=100)
  overview = models.CharField(max_length=1000)
  img = models.ImageField(upload_to='pics')
  age = models.IntegerField()
  runtime = models.IntegerField()
  rating = models.FloatField()
  genre1 = models.CharField(max_length=20)
  genre2 = models.CharField(max_length=20)
  genre3 = models.CharField(max_length=20)