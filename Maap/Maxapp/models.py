from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

class Fileupload(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="File has no description")
    file = models.FileField(upload_to='documents/')
    cover_image = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.name