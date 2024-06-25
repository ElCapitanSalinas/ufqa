from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class TextosBase(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)

class Estadisticas(models.Model):
    engagement = models.CharField("engagement", max_length=200)
    compartidos = models.CharField("compartidos", max_length=200)
    obj = models.CharField("Recaudo objetivo", max_length=200)
    rec = models.CharField("Recaudo", max_length=200)
    visitantes = models.CharField("Visitantes nuevos", max_length=200)

class Casos(models.Model):
    titulo = models.CharField(max_length=200)
    descb = models.CharField(max_length=200)
    descl = models.CharField(max_length=200, null=True)
    meta = models.IntegerField()
    recolectado = models.IntegerField()
    beneficiados = models.CharField(max_length=200, default='')
    ubicacion = models.CharField(max_length=200, default='')
    update = models.CharField(max_length=1000, null=True)
    last_update = models.DateField(blank=True, null=True)
    tiktok_url = models.CharField(max_length=200, null=True)
    directDonation = models.BooleanField()
    accNumber = models.CharField(max_length=200, null=True)
    accBank = models.CharField(max_length=200, null=True)

    def get_percentage(self):
        perc = self.recolectado * 100 / self.meta
        return perc
    
class Images(models.Model):
    project = models.ForeignKey(Casos, on_delete=models.CASCADE)
    image = models.ImageField()

class Donadores(models.Model):
    project = models.ForeignKey(Casos, on_delete=models.CASCADE)
    donatorName = models.CharField(max_length=200, null=True)
    amount = models.IntegerField()
    
class AdminUser(AbstractBaseUser, models.Model):
    # id = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)
