import click
from clients import commands as clients_commands

# Definir nuestro punto de entrada, a click se lo informamos así:
@click.group() 
@click.pass_context # nos devuelve un objeto contexto que inicializamos en la funcion
def cli(ctx):
    ctx.obj = {} 

# Registro los comandos que importe de mi archivo commands.py:
cli.add_command(clients_commands.all) # Para eso usamos el alias al final de commands.py

# Con setup.py voy a poder ejecutar mi programa sin tener que llamar
# al interprete de python. Es decir. Lo voy a ejecutar directamente desde
# mi linea de comandos. A configurarlo así...
