import argparse
import requests
import json
def poke_request_list(PH1):
    r=requests.get('https://pokeapi.co/api/v2/pokemon-species/{N}'.format(N=PH1))
    response=r.json()
    test=response.get('name')
    print(test)
    return test
parser = argparse.ArgumentParser()
parser.add_argument('list',type=str,
                    help='Display the list of all the Pokemon')
parser.add_argument('-n','--number',type=int,
                    help='Display the information of the given pokemon')
args=parser.parse_args()
given_pokemon=args.number
if args.number:
    print('You selected')
    print(args.number)
    print(poke_request_list(given_pokemon))
else:
    print('all pokemon')

#function to execute the API request depending of what if being pass
#TODO finish this function

    

