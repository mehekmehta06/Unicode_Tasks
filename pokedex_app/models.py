
from django.db import models

class Pokemonsearch(models.Model): 
    name = models.CharField(max_length=20, null= True)
    height = models.IntegerField(null= True)
    moves = models.JSONField(max_length=20, null= True)
    sprites = models.URLField(null= True)
    level = models.IntegerField(default=0)

def __str__(self):
    return self.name 