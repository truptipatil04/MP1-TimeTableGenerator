from django.db import models
import uuid
# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return f"{self.subject}"

class Room(models.Model):
    roomName = models.CharField(max_length=20,unique=True)
    roomCapacity = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.roomName}"

class Batch(models.Model):
    batchName = models.CharField(max_length=4,unique=True)
    batchCapacity = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.batchName}"

class Time(models.Model):
    timePeriod = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return f"{self.timePeriod}"
