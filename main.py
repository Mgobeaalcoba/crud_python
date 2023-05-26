clients = [
    {
        'name': 'Lautaro',
        'company': 'Google',
        'email': 'lautaro@google.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Nicole',
        'company': 'Facebook',
        'email': 'nicole@facebook.com',
        'position': 'Data engineer'
    }
]

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
    for idx, client in enumerate(clients):
        print(f'{idx}: {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')


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

def _get_client_field(field_name):
    return input(f'What is the client {field_name}? ')

# Entry point o punto de comienzo de nuestro codigo: 
if __name__ == '__main__':
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
    else:
        print('Invalid command')
