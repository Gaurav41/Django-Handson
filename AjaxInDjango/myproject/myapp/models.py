from django.db import models


# Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=150)
#     desc = models.TextField()
#     publish_date = models.DateTimeField(null=True)


class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)