import requests

tryout=requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
result=tryout.json()
id_tryout=result.get('id')
print(id_tryout)