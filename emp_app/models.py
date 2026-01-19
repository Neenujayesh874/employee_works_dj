from django.db import models

class Employee(models.Model):

    name=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    location=models.CharField(max_length=200)

    experience=models.PositiveIntegerField()

    age=models.PositiveIntegerField()

    email=models.CharField(max_length=200,unique=True)

    phone=models.CharField(max_length=200,unique=True)