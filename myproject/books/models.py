from django.db import models

# Create your models here.

class Books(models.Model):
  title = models.CharField(max_length=50)
  content = models.CharField(max_length=4000)

  def __str__(self):
    return '<Book:id=' + str(self.id) + ',' + self.title +')>'