from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hospital(models.Model):
    state=models.CharField(max_length=100)
    name=models.CharField(max_length=100,unique=True)
    city=models.CharField(max_length=100)
    admissionCapacity=models.IntegerField()
    TotalBeds=models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def NO_USER():
        if user is None:
            admissionCapacity=admissionCapacity+1