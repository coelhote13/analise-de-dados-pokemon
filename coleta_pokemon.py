import pandas as pd
import requests

url = "https://pokeapi.co/api/v2/pokemon/?limit=151"

resposta = requests.get(url)

dados = resposta.json()

pokemon = dados["results"]

dados_pokemon_lista = []

for p in pokemon:
    resposta_pokemon = requests.get(p["url"])
    dados_pokemon = resposta_pokemon.json()

    pokemon_info = {
        "id": dados_pokemon["id"],
        "name": dados_pokemon["name"],
        "weight": dados_pokemon["weight"],
        "height": dados_pokemon["height"]
    }

    dados_pokemon_lista.append(pokemon_info)

print(dados_pokemon_lista[0])

df = pd.DataFrame(dados_pokemon_lista)

df.to_csv("pokemon.csv", index=False)
