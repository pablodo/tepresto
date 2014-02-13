from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=200)
    community = models.ManyToManyField(Community)
    
