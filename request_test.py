import requests
import json
tryout = requests.get('https://pokeapi.co/api/v2/pokemon/55')
result = json.loads(tryout.text)
result2 = result.get('abilities')
result3 = []
for a in result2:
    result3.append(a.get('ability').get('name'))
print(result3)
