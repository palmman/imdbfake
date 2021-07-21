from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


