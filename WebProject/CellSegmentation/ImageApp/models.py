from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.TextField()
    description = models.TextField()