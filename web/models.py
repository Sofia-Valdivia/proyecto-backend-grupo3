
from django.db import models

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Tours(models.Model):
    region = models.ForeignKey(Region,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='tours',blank=True)
    
    def __str__(self):
        return self.nombre
