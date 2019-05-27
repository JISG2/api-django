from django.db import models

# Create your models here.

class CampeonM(models.Model):
    nombre = models.CharField(max_length=40)
    cantVida = models.IntegerField()
    cantArmadura = models.IntegerField()
    cantMR = models.IntegerField()
    carril = models.CharField(max_length=40)
    cantDamageI = models.IntegerField()

