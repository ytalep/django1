from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Auto(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    año = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    numerodepuertas = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    precio = models.CharField(max_length=200)
   
    

