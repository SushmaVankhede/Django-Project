from django.db import models

# Create your models here.
#models define the database

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
