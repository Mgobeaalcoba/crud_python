# Arquitectura: archivo de interface // commands.py maneja la interacción con el usuario.

import click

# Importo mi modelo y mis servicios para poder interactuar con ellos:
from clients.services import ClientService
from clients.models import Client

# Funcion que vamos a usar para definir el grupo al cual pertenece
# cada una de nuestras funciones:
@click.group() # Al definirlo como un grupo, puedo usar client como un decorador...
def clients():
    # Descripción de lo que hace este grupo de funciones:
    """Manages the clients lifecycles"""
    pass

# Definimos nuestras funciones/comandos basicos:
@clients.command()
@click.option('-n', '--name',
                type=str,
                prompt=True,
                help='The client name')
@click.option('-c', '--company',
                type=str,
                prompt=True,
                help='The client company')
@click.option('-e', '--email',
                type=str,
                prompt=True,
                help='The client email')
@click.option('-p', '--position',
                type=str,
                prompt=True,
                help='The client position')
@click.pass_context
def create(ctx, name, company, email, position): # Estos parametros se los voy a pedir al usuario con Click.option()
    # Los docstrings en click se usan para mostrar en nuestra interface de linea de comandos:
    """Creates a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx): # contexto o ctx es el contexto que inicializamos en pv.py como un dict vacio
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()

    # click.echo() es un metodo de click para reemplazar a print() que garantiza que va a imprimir igual en 
    # la consola de todos los sistemas operativos:
    click.echo(' ID  |  NAME  |  COMPANY  |  EMAIL  | POSITION')
    click.echo('*'*100)

    for client in clients_list:
        click.echo(f'{client["uid"]} | {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')

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
