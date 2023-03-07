from django.db import models
from datetime import datetime

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    book_img = models.ImageField(null=True, blank=True, upload_to="images/")

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=2000000)
    blog_image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_at = models.DateTimeField(default=datetime.now, blank=True)