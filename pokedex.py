import argparse
import requests
# import json

# TODO: investigate list comprehension

# setting of the requests funtion according to the data needed


def poke_request_list(PH1):
    if PH1 is True:
        r = requests.get(
            'https://pokeapi.co/api/v2/pokemon-species/{N}'
            .format(N=args.number))
        response = r.json()
        poke_name = response.get('name')
        return poke_name
    elif PH1 is False:
        r2 = requests.get(
            'https://pokeapi.co/api/v2/pokemon-species', params={'limit': 151})
        response2 = r2.json()
        poke_list = response2.get('results')
        list = []
        for i in poke_list:
            list.append(i['name'])
        return list


def poke_list_ID(pokemon_name):
    id_request = requests.get(
        'https://pokeapi.co/api/v2/pokemon/{poke_name}'
        .format(poke_name=pokemon_name))
    id_response = id_request.json()
    id = id_response.get('id')
    return id


def poke_R_evolution(pokemon_ID):
    try:
        evo_request = requests.get(
                    'https://pokeapi.co/api/v2/evolution-chain/{poke_id}'
                    .format(poke_id=pokemon_ID))
        evo_response = evo_request.json()
        substrat1 = list(evo_response.items())[2][1]
        substrat2 = substrat1.get('evolves_to')
        substrat3 = substrat2[0]
        substrat4 = substrat3.get('species')
        evolution = substrat4.get('name')
        substrat5 = substrat1.get('species')
        evolves_from = substrat5.get('name')
        return evolves_from.title(), evolution.title()
    except Exception as e:
        error = [e]
        print(error)
        evo_request = requests.get(
                    'https://pokeapi.co/api/v2/evolution-chain/{poke_id}'
                    .format(poke_id=pokemon_ID))
        evo_response = evo_request.json()
        substrat1 = list(evo_response.items())[2][1]
        substrat2 = substrat1.get('species')
        pre_evo = substrat2.get('name')
        poke_name = False
        return pre_evo.title(), poke_name


# build up of other functions that will be need it to finisht the program


# setting the main function to run according of the commmand


def poke_list():
    print(args)
    if args.number is None:
        pokemon_list = poke_request_list(False)
        print('------all 1st Gen pokemon------')
        print('ID---------NAME')
        for i in pokemon_list:
            pokemon_id = poke_list_ID(i)
            id_str = str(pokemon_id)
            print(id_str.zfill(3), i)
    elif args.number > 151:
        print('You can only select pokemon from 1st generation')
        print('Try again')
    elif args.number:
        print('------You selected------')
        print('Pokemon Name: {Name} --- Pokemon ID: {ID}'.format(
            Name=poke_request_list(True), ID=args.number))


def poke_evolution():
    # print(args)
    if args.table is False:
        poke_ID = args.evo_ID
        pre_evo, evo_name = poke_R_evolution(poke_ID)
        if evo_name:
            print('{evolves_from} has evolved to {evolves_to}'
                  .format(evolves_from=pre_evo, evolves_to=evo_name))
        else:
            print(f'The Pokemon {pre_evo} that you selected has no evolution')
    elif args.table:
        poke_ID = args.evo_ID
        pre_evo, evo_name = poke_R_evolution(poke_ID)
        if evo_name:
            headers = ['ID', 'PokeName', 'EvoName']
            data = [poke_ID, pre_evo, evo_name]
            table_header = '|' + '|'. join(f'{h.center(len(str(c))+2)}'
                                           for h, c in
                                           zip(headers, data)) + '|'
            table_separation = '|' + '|'.join('-' * (len(str(c))+2)
                                              for c in data) + '|'
            table = '|' + '|'.join(str(d).center(len(str(d))+2)for
                                   d, h in zip(data, headers)) + '|'
            print(table_header)
            print(table_separation)
            print(table)
        else:
            print(f'The Pokemon {pre_evo} that you selected has no evolution')


# Parsers - part of the code where the parser are set
# main parser set
parser = argparse.ArgumentParser(
    prog='Pokedex CLI', description='CLI for getting pokemon data',
    epilog='Thanks see  you next time')
parser.add_argument('pokedex', type=str,
                    help='Command to access pokedex information')
# setting subparsers
subparser = parser.add_subparsers(dest='command')
sub_list = subparser.add_parser('list', help='list 1st gen pokemon')
sub_list.add_argument('-n', '--number', type=int, help='Display the pokemon')
sub_evo = subparser.add_parser(
    'evolution', help='Show the given pokemon evolution in a table')
sub_evo.add_argument(
    '-t', '--table', action='store_true',
    help='Show the given pokemon evolution in a table')
sub_evo.add_argument(
                    'evo_ID',
                    type=int,
                    help='ID of the pokemon you need its evolution')
args = parser.parse_args()


def main():
    # print(args.command)
    if args.command == 'list':
        poke_list()
    elif args.command == 'evolution':
        poke_evolution()


if __name__ == '__main__':
    main()
