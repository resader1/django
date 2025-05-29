from django.db import models

# Create your models here.
class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name},{self.major}'
