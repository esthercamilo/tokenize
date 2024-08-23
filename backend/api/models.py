"""
Aqui será feita a modelagem de funcionário, rh dentre outras necessárias para o registro em blockchain.
Usaremos banco de dados relacional.
"""

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    tokens = models.IntegerField(default=0)
    badges = models.JSONField(default=list)
