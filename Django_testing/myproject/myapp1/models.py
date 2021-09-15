from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    likes = models.ManyToManyField(User,related_name="like",default=None,blank=True)
    

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name=models.CharField(max_length=100,null=False)
    description=models.TextField()
    quantity=models.IntegerField()
    price_per_item = models.IntegerField()
    

    def __str__(self) -> str:
        return self.title