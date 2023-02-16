from django.db import models

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length = 254)
    LastName = models.CharField(max_length = 254)
    Email = models.CharField(max_length = 254)

    def __str__(self):
        return self.FirstName
