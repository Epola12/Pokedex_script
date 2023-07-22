import requests

tryout=requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
result=tryout.json()
id_tryout=result.get('id')
id_str=str(id_tryout)
id_str_len=len(id_str)
print((id_str_len))
print(id_tryout)

