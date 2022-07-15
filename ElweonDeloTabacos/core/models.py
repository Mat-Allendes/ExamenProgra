from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class registro(models.Model):
    id_Reg=models.OneToOneField(User,on_delete=models.CASCADE)
    rut=models.TextField(max_length=12)
    fecha=models.DateField()
    num=models.IntegerField()
    direccion=models.TextField()
    def __str__(self):
        return self.rut
    