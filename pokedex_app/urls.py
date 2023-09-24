from django.urls import path
from . import views
from pokedex_app.views import dashboard

urlpatterns = [
    path('dashboard/',dashboard, name="dashboard"),
    path('types',views.pokemon_types),
    path('display',views.pokemon_display),
    path('fight', views.pokemon_fight),
    path('show', views.pokemon_detail),
    path('select',views.pokemon_by_type),
    path('search',views.pokemon_search),
]
