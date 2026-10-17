import requests
# import json
tryout = requests.get('https://pokeapi.co/api/v2/evolution-chain/380')
result2 = tryout.json()
# result = json.loads(tryout.text)
result3 = list(result2.items())[2][1]
result4 = result3.get('species')
# when there is no evo here is where you can pick up the name of the pokemon
result5 = result4.get('name')
result6 = result5.get('species')
result7 = result6.get('name')
sub1 = result3.get('species')
sub2 = sub1.get('name')
print('{evolves_from}, ha evolucionado ha {evolves_to}'
      .format(evolves_from=sub2, evolves_to=result7))
