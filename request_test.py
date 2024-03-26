import requests
# import json 
tryout = requests.get('https://pokeapi.co/api/v2/evolution-chain/2')
result2 = tryout.json()
# result = json.loads(tryout.text)
result3 = list(result2.items())[1][1]
result4 = result3.get('evolves_to')
result5 = result4[0]
result6 = result5.get('species')
result7 = result6.get('name')
sub1 = result3.get('species')
sub2 = sub1.get('name')
print('{evolves_from}, ha evolucionado ha {evolves_to}'
      .format(evolves_from=sub2, evolves_to=result7))