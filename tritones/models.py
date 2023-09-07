from django.db import models

# Create your models here.

class exampleModel(models.Model): 
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)