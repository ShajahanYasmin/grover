from django.db import models

# Create your models here.
class cspModel(models.Model):
    statement=models.CharField(max_length=128)
