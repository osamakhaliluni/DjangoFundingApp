from django.db import models
from datetime import date

# Create your models here.

class user(models.Model):
    x = [("Creator", "Creator"), ("Donor", "Donor")]
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=16)
    mobilenum = models.CharField(max_length=11)
    utype = models.CharField(max_length=7, choices=x)
    def __str__(self) -> str:
        return self.email
    
class project(models.Model):
    title = models.CharField(max_length=30)
    details = models.TextField()
    target = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    creator = models.ForeignKey(user, on_delete=models.PROTECT, blank=False)
    def __str__(self) -> str:
        return self.title