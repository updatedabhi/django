from django.db import models

class Employee(models.Model):
  firstname = models.CharField(max_length = 200)
  lastname = models.CharField(max_length = 50)
  salary = models.IntegerField()
