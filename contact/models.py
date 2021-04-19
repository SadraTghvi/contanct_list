from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.full_name