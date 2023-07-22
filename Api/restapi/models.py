from django.db import models

class student(models.Model):
    roll=models.IntegerField()
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    father=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    std=models.CharField(max_length=20)
    # division=models.Choices()
    addmision_dt=models.DateTimeField(auto_now=True)



