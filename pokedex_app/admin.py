from django.contrib import admin

# Register your models here.
from .models import Pokemonsearch 
class pokemonAdmin(admin.ModelAdmin):
    list_display = ('name','height','moves','sprites','level')
admin.site.register(Pokemonsearch, pokemonAdmin)
