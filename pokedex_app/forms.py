

from django import forms
from .models import Pokemonsearch

class PokemonTypeForm(forms.Form):
    type_choices = [
        ('grass', 'Grass'),
        ('fire', 'Fire'),
        ('water', 'Water'),
         ('normal','Normal'),
          ('fighting','Fighting'),
           ('flying','Flying'),
           ('shadow','Shadow')
        ]
        
    type = forms.ChoiceField(choices=type_choices, label='Select a Pokémon Type') 
        
class PokemonsearchForm(forms.Form):
         type1 = forms.CharField(label='Enter Pokemon', max_length=20 )

class PokemonfightForm(forms.Form):
       name1 = forms.CharField(max_length=20, label='Pokemon1')
       name2 = forms.CharField(max_length=20, label='Pokemon2')       
       
 
    


        
    

   
