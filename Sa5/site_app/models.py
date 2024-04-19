from django.db import models

# Create your models here.

class Pessoa (models.Model):
    """ class Pessoa
    -
    Fields:
    - `nome` = String
    - `email` = String
    - `ani` = Int
    - `pais` = String
    
    """

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    ani = models.IntegerField()
    pais = models.CharField(max_length=100)
