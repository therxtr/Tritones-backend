from django.db import models

# Create your models here.

class Member(models.Model): 
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10) # has special chars so have to use charField
    voicePart = models.CharField(max_length=30)

    def __str__(self): 
        return self.name

class boardMember(models.Model): 
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10) # has special chars so have to use charField
    voicePart = models.CharField(max_length=30)
    board = models.CharField(max_length=50)

    def __str__(self): 
        return self.name
    
class contactModel(models.Model): 
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField(default='')
    message = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name


