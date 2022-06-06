from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'media/images')
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name[0:50] 
        
class Evente(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    eventdate = models.DateField(auto_now_add=False, auto_now=False ,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'media/images')
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name[0:50]  