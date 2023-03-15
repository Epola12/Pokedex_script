import argparse
import urllib3
http=urllib3.PoolManager()
parser = argparse.ArgumentParser()
parser.add_argument('list',type=str,
                    help='Display the list of all the Pokemon')
parser.add_argument('-n','--number',type=int,
                    help='Display the information of the given pokemon')
args=parser.parse_args()
given_pokemon=args.number
if args.number:
    print('given pokemon')
    print(args.number)
else:
    print('all pokemon')

#function to execute the API request depending of what if being pass
#TODO finish this function
def poke_request():

    pass
#no se si vas a ver el mensaje del commit pero si no lo pongo aqui gracias por ser
#ese maravilloso amigo y mentor de esto que es mi sueño lograrlo, eres mi idolo hermano
#sin duda un ejemplo a seguir gracias por tu apoyo ya no dejare este pedo
#XOXO
