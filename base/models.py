from tkinter import CASCADE
from django.db import models
# User Model is prewritten in Django
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name




# child of Topic
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200, null=True, blank=True)
    #participants = 
    #takes a snapshot every time
    updated = models.DateTimeField(auto_now=True)
    #takes only one time
    created = models.DateTimeField(auto_now_add=True)

    
    # newest updated item will come first
    class Meta:
        ordering =['-updated', '-created',]

    def __str__(self):
        return self.name




#child of User and Room
class Message(models.Model):
    # relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # relationShiop
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    


