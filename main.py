import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            # Agrego cada cliente desde el csv como si fuera un diccionario:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp' # Convención para registro de tablas temporales
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        # Remueve la tabla original
        os.remove(CLIENT_TABLE)
        # Reescribe la tabla temporal como tabla original
        os.rename(tmp_table_name, CLIENT_TABLE)


# Va a recibir el diccionario de cliente
def create_client(client):
    # Para usar una variable global dentro de una función debo declararla como global
    # global clients
    # Los operadores de pertenencia funcionan igual en las listas que en los strings: 
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list.')


def list_clients():
    print('id | name | company | email | position')
    print('*'*50)
    for idx, client in enumerate(clients):
        print(f'{idx} | {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')


def update_client(client_id, new_client):
    # global clients
    # print(f"client_id: {client_id} | enumerate(clients): {enumerate(clients)} | new_client: {new_client}")
    if client_id < len(clients):
        clients[client_id] = new_client
        list_clients()
    else:
        print('Client is not in clients list.')
        list_clients()


def delete_client(client_id):
    # global clients
    if client_id < len(clients):
        clients.pop(client_id)
        list_clients()
    else:
        print('Client is not in clients list.')
        list_clients()


def search_client(client_id):
    # global clients
    find_id = False
    for idx, client in enumerate(clients):
        if idx != client_id:
            continue
        else:
            find_id = True
            print(find_id)
            print(f'{idx}: {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')
    if not find_id:
        print(f"Don't find the client id: {client_id}")

def _print_welcome():
    print('WELCOME TO GOBEA VENTAS')
    print('*' * 50)
    print('What would toy like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[L]ist all clients')

def _get_client_field(field_name):
    return input(f'What is the client {field_name}? ')

# Entry point o punto de comienzo de nuestro codigo: 
if __name__ == '__main__':
    _initialize_clients_from_storage()

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }

        create_client(client)
        list_clients()
    elif command == 'R':
        client_id = int(_get_client_field("id"))
        search_client(client_id)
    elif command == 'D':
        client_id = int(_get_client_field("id"))
        delete_client(client_id)
    elif command == 'U':
        client_id = int(_get_client_field("id"))
        new_client = {
            "name": _get_client_field("name"),
            "company": _get_client_field("company"),
            "email": _get_client_field("email"),
            "position": _get_client_field("position")
        }
        update_client(client_id, new_client)
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')

    _save_clients_to_storage()
