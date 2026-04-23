from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
   name = models.CharField(max_length=100)
   bio = models.TextField(blank=True)
   email = models.EmailField(unique=True)
   created_at = models.DateTimeField(auto_now_add=True)
   profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
   def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class ticket(models.Model):
    ticket_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ticket_images/', blank=True, null=True)

    def __str__(self):
        return self.ticket_name


