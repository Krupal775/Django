from django.db import models

# Create your models here.
class contact(models.Model):
    Name = models.CharField(max_length=122)
    Phone = models.CharField(max_length=12)
    Email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()