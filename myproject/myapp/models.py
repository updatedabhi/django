from django.db import models

class Employee(models.Model):
  firstname = models.CharField(max_length = 200)
  lastname = models.CharField(max_length = 50)
  salary = models.IntegerField()
  def __str__(self):
    return self.firstname + " " + self.lastname + " " + str(self.salary)
  
class Author(models.Model):
  name = models.CharField(max_length = 200)
  email = models.EmailField()
  description = models.TextField()
  def __str__(self):
    return self.name
  
class Book(models.Model):
  title = models.CharField(max_length = 200)
  author = models.ForeignKey(Author, on_delete = models.CASCADE)
  published_date = models.DateField()
  def __str__(self):
    return self.title
  
# class Signup(models.Model):
#   username = models.CharField(max_length=200)
#   email = models.EmailField()
#   password = models.CharField(max_length=200)
#   def __str__(self):
#     return self.username
  
  
# class Blogpost(models.Model):
#   title = models.CharField(max_length=200)
#   post = models.CharField(max_length=200)
#   thumbnail = models.ImageField(upload_to="images/", blank=True, null=True)

