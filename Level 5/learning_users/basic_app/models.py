from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class UserProfileInfo(models.Model):
    # this class extends fields to a pre-existing model
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank = True)
    
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)

    def __str__(self):
        return self.user.username

