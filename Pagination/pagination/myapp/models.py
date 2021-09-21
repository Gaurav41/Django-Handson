from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)