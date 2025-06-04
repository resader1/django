from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    pw = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    nickName = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.id},{self.name},{self.nickName}'
    