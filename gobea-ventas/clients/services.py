# Lógica del negocio: ¿Cual es lo lógica especifica de nuestro programa? 

import csv

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
            
