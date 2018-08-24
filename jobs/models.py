from django.db import models

# Create your models here.

class Job(models.Model):

    title = models.CharField(max_length=250)
    company = models.CharField(max_length=200)
    city = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
