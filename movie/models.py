from django.db import models
from django.db.models.aggregates import Max
from users.models import Profile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    des = models.TextField(blank=True)
    image = models.ImageField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    director = models.ManyToManyField(Director)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    


class Comment(models.Model):
    
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    movie_comment = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE, related_name='commentMovie')
    name = models.CharField(max_length=100, null=True, blank=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body



    