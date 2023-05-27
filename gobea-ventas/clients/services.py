# Lógica del negocio: ¿Cual es lo lógica especifica de nuestro programa? 

import csv
import os

from clients.models import Client

class ClientService():

    # Recibe como parametro el nombre del archivo donde vamos a guardar la info:
    def __init__(self, table_name) -> None:
        self.table_name = table_name

    def create_client(self, client):
        # Abrimos el archivo en modo "append"
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    # Tenemos ya los servicios y las clases... Solo nos queda indicarle
    # a los comandos como interactuar con los mismos.

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            
            return list(reader)
        
    def update_client(self, updated_client):
        clients = self.list_clients()

        updated_clients = []
        for client in clients:
            if client['uid'] == updated_client.uid:
                # Los elementos de mi lista deben ser diccionarios para poder escribirlos en mi csv. Por eso uso to_dict()
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)

    def delete_client(self, delete_client):
        clients = self.list_clients()

        updated_clients = []
        for client in clients:
            if client['uid'] == delete_client.uid:
                continue
            else:
                updated_clients.append(client)
        
        self._save_to_disk(updated_clients)

    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            writter = csv.DictWriter(f, fieldnames=Client.schema())
            writter.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
            
