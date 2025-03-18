import requests
import json
from time import sleep


url = "https://pokeapi.co/api/v2/pokemon/"
pokemonList = []
page = 0

print("Start\n")

while url != None:
    payload = {}
    headers = {}
    response = json.loads(requests.get(
        url, headers=headers, data=payload).text)
    page += 1
    url = response["next"]

    for item in response["results"]:
        pokemonName = item['name']
        pokemonUrl = f"https://pokeapi.co/api/v2/pokemon/{pokemonName}"

        pokemonResponse = response = json.loads(requests.get(
            pokemonUrl, headers=headers, data=payload).text)

        pokemonId = pokemonResponse["id"]
        pokemonHeight = pokemonResponse["height"]
        pokemonWeight = pokemonResponse["weight"]
        pokemonIsDefault = pokemonResponse["is_default"]

        info = {
            "name": pokemonName,
            "id": pokemonId,
            "height": pokemonHeight,
            "weight": pokemonWeight,
            "is_default": pokemonIsDefault
        }
        print(pokemonName)
        pokemonList.append(info)

    filePath = f"pokemonFiles\PokemonList_{page}.json"
    with open(filePath, "w") as outfile:
        print(f"Saving in: {filePath}")
        json.dump(pokemonList, outfile)

    outfile.close()


print("\nEnd")
print(pokemonList)
