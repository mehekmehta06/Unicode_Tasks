
import requests
from django.http import JsonResponse
from django.shortcuts import render
from .forms import PokemonsearchForm
from .forms import  PokemonTypeForm
from .models import Pokemonsearch



def pokemon_types(request):

    api_url1 = 'https://pokeapi.co/api/v2/type/'
    api_url2 = 'https://pokeapi.co/api/v2/ability'
    api_url3 = 'https://pokeapi.co/api/v2/egg-group'
    api_url4 = 'https://pokeapi.co/api/v2/nature'

    try:
        #pokemon types
        response1 = requests.get(api_url1)
        
        if response1.status_code == 200:
            data1 = response1.json()
            types = [entry['name'] for entry in data1['results']]
            response_data1 = {'types': types}
        else:
            response_data1 = {'error': 'Failed to fetch data from PokeAPI'}
        #pokemon abilities
        response2 = requests.get(api_url2)
        
        if response2.status_code == 200:
            data2 = response2.json()
            abilities = [entry['name'] for entry in data2['results']]
            response_data2 = {'ability': abilities}
        else:
            response_data2 = {'error': 'Failed to fetch data from the second API'}
        #pokemon eggGroup
        response3 = requests.get(api_url3)
       
        if response3.status_code == 200:
            data3 = response3.json()
            eggGroups = [entry['name'] for entry in data3['results']]
            response_data3 = {'EggGroup': eggGroups}
        else:
            response_data3 = {'error': 'Failed to fetch data from PokeAPI'}
        #pokemon natures
        response4 = requests.get(api_url4)
        
        if response4.status_code == 200:
            data4 = response4.json()
            natures = [entry['name'] for entry in data4['results']]
            response_data4 = {'Nature': natures}
        else:
            response_data4 = {'error': 'Failed to fetch data from PokeAPI'}
        #json response method
        #combined_response_data = [response_data1,response_data2,response_data3,response_data4]
         #return JsonResponse(combined_response_data, safe=False)
        #template method
        return render(request, 'pokedex_app/pokemon_types.html',{'types': types,'abilities': abilities,'eggGroups': eggGroups,'natures':natures})

    except Exception as e:
        #return JsonResponse({'error': str(e)})
        error_message = str(e)
        return render(request, 'pokedex_app/error.html', {'error_message': error_message})

   
def pokemon_by_type(request):
    if request.method == 'POST':
        form = PokemonTypeForm(request.POST)
        if form.is_valid():
            selected_type = form.cleaned_data['type']

            api_url = f'https://pokeapi.co/api/v2/type/{selected_type}'
           
            try:
                response= requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()

                    pokemon_list = [entry['pokemon']['name'] for entry in data['pokemon']]

                    return render(request, 'pokedex_app/pokemon_list.html', {'pokemon_list': pokemon_list})
                else:
                    return render(request, 'pokedex_app/error.html', {'error_message': error_message})
                
            except Exception as e:
                error_message = str(e)
                return render(request, 'pokedex_app/error.html', {'error_message': error_message})

    else:
        form = PokemonTypeForm()

    return render(request, 'pokedex_app/type_selection.html', {'form': form})

def dashboard(request):
    return render(request, "pokedex_app/dashboard.html")

"""
def pokemon_search(request):
    if request.method == 'POST':
        form1 = PokemonsearchForm(request.POST)

        if form1.is_valid():
            selected_name = form1.cleaned_data['type1']
            
            api_url1 = f'https://pokeapi.co/api/v2/pokemon/{selected_name}'
            
            
            try:
                response= requests.get(api_url1)
                if response.status_code == 200:
                    data = response.json()
                  
                    pokemon_list0 = selected_name
                    pokemon_list1 = data['height']
                    pokemon_list2 = [entry['move']['name'] for entry in data['moves']]
                    pokemon_list3 = data['sprites']['front_default']
                    pokemon = Pokemonsearch(
                        name=selected_name,
                        height=data['height'],
                        moves=[entry['move']['name'] for entry in data['moves']],  # You can store the entire moves data as JSON
                        sprites=data['sprites']['front_default']                       
                    )
                    pokemon.save()
                    pokemon = Pokemonsearch.objects.get(name=selected_name)
                
                    pokemon.level += 1
                    pokemon.save()
                    return render(request, 'pokedex_app/main.html', {'pokemon_height': pokemon_list1,'pokemon_moves': pokemon_list2, 'pokemon_name': pokemon_list0, 'pokemon_sprites': pokemon_list3})
                else:
                    return render(request, 'pokedex_app/error.html', {'error_message': error_message})
                
            except Exception as e:
                error_message = str(e)
                return render(request, 'pokedex_app/error.html', {'error_message': error_message})
    else:
        form1 = PokemonsearchForm()
    return render(request, 'pokedex_app/pokemon_search.html', {'form1': form1} )
"""


def pokemon_search(request):
    if request.method == 'POST':
        form1 = PokemonsearchForm(request.POST)
        if form1.is_valid():
            selected_name = form1.cleaned_data['type1']
            
            try:
                pokemon = Pokemonsearch.objects.get(name=selected_name)               
                pokemon.level += 1
                pokemon.save()
            except Pokemonsearch.DoesNotExist:
                
                pokemon_data = fetch_pokemon_data(selected_name)
                
                pokemon = Pokemonsearch(
                    name=selected_name,
                    height=pokemon_data.get('height', None),
                    moves=', '.join(pokemon_data.get('moves',[])),
                    sprites =pokemon_data.get('sprites', None),
                )
                pokemon.save()
                
                
    else:
        form1 = PokemonsearchForm()
    
    return render(request, 'pokedex_app/pokemon_search.html', {'form1': form1})

def fetch_pokemon_data(selected_name):
    
    api_url1 = f'https://pokeapi.co/api/v2/pokemon/{selected_name.lower()}/'
    
    response = requests.get(api_url1)
    if response.status_code == 200:
        data = response.json()
        return {
            'name':data['name'],
            'height': data['height'],
            'moves':[entry['move']['name'] for entry in data['moves']],
            'sprites': data['sprites']['front_default']
        }
    return {}

def pokemon_detail(request):
    display_all = Pokemonsearch.objects.all()
    return render(request, 'pokedex_app/display_pokemon.html', {'display': display_all})

def pokemon_fight(request):
    return render(request, 'pokedex_app/')
