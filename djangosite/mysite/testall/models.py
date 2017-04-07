from django.db import models

# Create your models here.

class Person(models.Model):
    #first_name= models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(default='xiaoming', max_length=60)
    shirt_size = models.CharField(default='M', max_length=1, choices=SHIRT_SIZES)