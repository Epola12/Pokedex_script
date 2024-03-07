import argparse
import requests
import json

#TODO: investigate list comprehension 

#setting of the requests funtion according to the data nedeed 
def poke_request_list(PH1):
    if PH1==True: 
        r=requests.get('https://pokeapi.co/api/v2/pokemon-species/{N}'.format(N=args.number))
        response=r.json()
        poke_name=response.get('name')
        return poke_name
    elif PH1==False:
        r2=requests.get('https://pokeapi.co/api/v2/pokemon-species',params={'limit':151})
        response2=r2.json()
        poke_list=response2.get('results')
        list=[]
        for i in poke_list:
            list.append(i['name'])
        return list
    
def poke_list_ID(pokemon_name):
    id_request=requests.get('https://pokeapi.co/api/v2/pokemon/{poke_name}'.format(poke_name=pokemon_name))
    id_response=id_request.json()
    id=id_response.get('id')
    return id

#setting the main function to run according of the commmand 
def poke_list():
    print('aqui')
    if args.number>151:
        print('You can only select pokemon from 1st generation')
        print('Try again')
    elif args.number:
        print('------You selected------')
        print('Pokemon Name: {Name} --- Pokemon ID: {ID}'.format(Name=poke_request_list(True),ID=args.number))
    elif args.number==None:
        pokemon_list=poke_request_list(False)
        print('------all 1st Gen pokemon------')
        print('ID---------NAME')
        for i in pokemon_list:
            pokemon_id=poke_list_ID(i)
            id_str=str(pokemon_id)
            print(id_str.zfill(3),i)


def poke_evolution():
    if args.table ==None:
        print('You are missing the pokemon ID and the argument -t or --table')

    
#Parsers - part of the code where the parser are set 
#main parser set 
parser = argparse.ArgumentParser(prog='Pokedex CLI', description='CLI por getting pokemon data', epilog='Thanks see  you next time')
parser.add_argument('pokedex',type=str,
                    help='Command to access pokedex information')
#setting subparsers
subparser=parser.add_subparsers(help='sub-command help')
sub_list=subparser.add_parser('list',help='Display a list of all the 1rs gen Pokemon')
sub_list.add_argument('-n','--number',type=int, help='Display the given pokemon')
sub_list.set_defaults(func=poke_list)
sub_evo=subparser.add_parser('evolution',help='Show the given pokemon evolution in a table')
sub_evo.add_argument('-t','--table', help='Show the given pokemon evolution in a table')
args=parser.parse_args()

#def main(): 
        
              
#if __name__== '__main__':
 #   main()    

