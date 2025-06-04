from django.db import models


class Member(models.Model):
    #중복X, nullX
    id = models.CharField(max_length=50,primary_key=True)
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    nickName = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.id}, {self.name}, {self.nickName}"