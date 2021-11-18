import argparse
import sys
prueba_parser = argparse.ArgumentParser(description='suma de dos numeros')
prueba_parser.add_argument('enteros', metavar='int', nargs='+', type=int,
                           help='debes de ingresar numeros enteros para poder realizar la suma')
prueba_parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('W'),
                           help='archivo donde la suma sera escrita')
argumentos = prueba_parser.parse_args()
argumentos.log.write('%s' % sum(argumentos.enteros))
argumentos.log.close()
