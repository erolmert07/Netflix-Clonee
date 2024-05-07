from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profiles(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    isim = models.CharField(max_length=100)
    resim = models.FileField(upload_to='ProfilResmi',null=True,blank=True)
    def __str__(self):
        return self.isim