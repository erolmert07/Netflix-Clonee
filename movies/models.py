from django.db import models

# Create your models here.


class Kategori(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Tur(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movies(models.Model):
    filmismi=models.CharField(max_length=100)
    tur=models.ManyToManyField('Tur',null=True)
    aciklama=models.TextField(max_length=500)
    resim=models.FileField(upload_to='afis',null=True,blank=True)
    kategori=models.ForeignKey(Kategori,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.filmismi