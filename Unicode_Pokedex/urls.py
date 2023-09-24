from django.urls import path
from django.urls import include
from pokedex_app import views
from django.contrib import admin

urlpatterns = [
    path('', include('pokedex_app.urls')),
    path('admin/',admin.site.urls),
    path('pokedex/', include('pokedex_app.urls')),
    path('pokemon_form/',include('pokedex_app.urls')),
]
