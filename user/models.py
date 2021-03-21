from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(User):
    age=models.IntegerField()
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

class ChosenHospital(models.Model):
    state=models.CharField(max_length=100)
    name=models.CharField(max_length=100,unique=True)
    city=models.CharField(max_length=100)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)

class Developer(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='profile_pics')
    desc=models.TextField()

    def __str__(self):
        return f'{self.name} Bio'
