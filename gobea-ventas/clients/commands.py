import click

# Funcion que vamos a usar para definir el grupo al cual pertenece
# cada una de nuestras funciones:
@click.group() # Al definirlo como un grupo, puedo usar client como un decorador...
def clients():
    # Descripción de lo que hace este grupo de funciones:
    """Manages the clients lifecycles"""
    pass

# Definimos nuestras funciones/comandos basicos:
@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    # Los docstrings en click se usan para mostrar en nuestra interface de linea de comandos:
    """Creates a new client"""

@clients.command()
@click.pass_context
def list(ctx): # contexto o ctx es el contexto que inicializamos en pv.py como un dict vacio
    """List all clients"""
    pass

@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    pass

@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    "Deletes a client"
    pass

# Por último voy a declarar un alias de clients:
all = clients
