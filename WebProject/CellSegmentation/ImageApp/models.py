from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.TextField()
    description = models.TextField()
    imageField = models.ImageField(default='defaul.png',blank=True)