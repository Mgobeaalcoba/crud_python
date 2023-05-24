clients = ['pablo', 'ricardo']

def create_client(client_name):
    # Para usar una variable global dentro de una función debo declararla como global
    # global clients
    # Los operadores de pertenencia funcionan igual en las listas que en los strings: 
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list.')


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client}')


def update_client(client_name, updated_client_name):
    # global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
        list_clients()
    else:
        print('Client is not in clients list.')
        list_clients()


def delete_client(client_name):
    # global clients
    if client_name in clients:
        clients.remove(client_name)
        list_clients()
    else:
        print('Client is not in clients list.')
        list_clients()


def search_client(client_name):
    # global clients
    for client in clients:
        if client != client_name:
            continue
        else:
            print(True)


def _print_welcome():
    print('WELCOME TO GOBEA VENTAS')
    print('*' * 50)
    print('What would toy like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')


def _get_client_name():
    return input('What is the client name? ')

# Entry point o punto de comienzo de nuestro codigo: 
if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'R':
        client_name = _get_client_name()
        search_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the new client name? ')
        update_client(client_name, updated_client_name)
    else:
        print('Invalid command')
