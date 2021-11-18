
# Poke CLI

## Descripción
Escribir un CLI (Command Line Interface) utilizando **Argparse** capaz de obtener datos de una RESTful API https://pokeapi.co/

Crear un repositorio git.

Manejo de errores.

# Uso
pokedex list [-n --number int]

-n --number     número de pokemones a listar (solo primera generación)
                default todos

pokedex evolution {pokemon_name|pokemon_id} [-t --table]

-t --table      mostrar en formato tabla, si no un mensaje personalizado es deplegado
                "Pikachu ha evolucionado a Raichu"

pokedex info {pokemon_name|pokemon_id} [-a --ability|-ha --habitat|-b --both]

-a --ability    desplegar el nombre de las habilidades del pokemon
-ha --habitat   desplegar el nombre del hábitat
-b --both       desplegar habilidades y hábitat (default)

# Tests
Crear test para los tres comandos

# Detalles
|ID|Pokemon name|Random move|Type|
|----|----|----|----|
|25|Pikachu|Mega-Punch|Electric|

|ID|Pokemon name|Pokemon evolution name|
|----|----|----|
|25|Pikachu|Raichu|

|ID|Pokemon name|Abilities|Habitat|
|----|----|----|----|
|25|Pikachu|[static, lightning-rod]|forest|

# Tools
- Argparse
- Requests
- Urllib3*
- Pytest

## Docs
[Command Line Interfaces](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df)  
[RealPython - Command Line Interfaces](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)  
[Format string](https://pyformat.info/)
[Pytest](https://realpython.com/pytest-python-testing/)