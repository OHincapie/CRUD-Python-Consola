from http import client
import sys
import os
from typing import List

#El global funciona para que cuando yo quiera asignarle nuevo valor a una variable global no lo tome como una variable de 
#de funcion


clients = [
    {
        'id': 1,
        'name': 'Lionel Messi',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Sofware Engineer'
    },
    {
        'id':2,
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer'
    }
]


def _print_clients(client):
    print('{id} | {name} | {company} | {email} | {position}'.format(id=client['id'],
        name=client['name'],
        company=client['company'], 
        email=client['email'],
        position=client['position']))

def list_clients():
    global clients
    for client in clients:
        _print_clients(client)
        
 

def create_client(client):
    global clients
    clients.append(client)



def update_client(client_id):
    global clients
    aux = False
    for i in clients:
        if client_id == i['id']:
            aux = True
            newClient = ingress_client_data(client_id)
            clients[clients.index(i)] = newClient
    if aux == False:
        print('Client is not in clients list')


def delete_clients(client_id):
    global clients
    aux = False
    for i in clients:
        if int(client_id) == i['id']:
            aux = True
            clients.pop(clients.index(i))
    if aux == False:
        print('Client is not in clients list')
    

def _print_welcome():
    print('WELCOME TO FUSION')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[E]xit')    


def search_client(client_id):
    global clients
    aux=False
    for i in clients:
        if int(client_id) == i['id']:
            aux=True
            index=clients.index(i)
            _print_clients(clients[index])
    if aux == False:
        print("The client: {} is not in our client\'s list".format(client_id))


def ingress_client_data(id=0):
    global clients
    clients_id: List[int] = []
    for i in clients:
        clients_id.append(i['id'])

    clients_id.sort()
    newId = clients_id[-1]+1
    if id != 0 :
        newId = id

    client={
        "id": newId,
        "name": _get_client_field('name'),
        "company": _get_client_field('company'),
        "email": _get_client_field('email'),
        "position": _get_client_field('position'),
    }
    return client


def _get_client_field(field_name):
    field=None
    while not field:
        field=input('What is the client {}? \n'.format(field_name))
    return field


def _get_client_name():
    client_name=None
    while not client_name:
        client_name=str(input('What is the client name? \n'))
        
    if client_name.lower() == 'exit':
        sys.exit()
    else:    
        return client_name.title()


def _get_client_by_id():
    client_id = None
    while not client_id:
        client_id=int(input('What is the client id? \n'))
    return client_id


if __name__ == "__main__":
    os.system('CLS')
    while True:
        _print_welcome()

        command = input()
        command=command.upper()
        os.system('CLS')
        if command == 'C':
            clientObj=ingress_client_data()
            create_client(clientObj)
            list_clients()
        elif command == 'L':
            list_clients()    
        elif command == 'D':
            client_id=_get_client_by_id()
            print(client_id)
            delete_clients(client_id)
            list_clients()
        elif command == 'U':
            client_id=_get_client_by_id()
            print(client_id)
            update_client(client_id)
            list_clients()
        elif command == 'S':
            client_ID = _get_client_by_id()
            search_client(client_ID)
        elif command == 'E':
            sys.exit()
            break
        else:
            print('INVALID COMMAND')    
        input()
        os.system("CLS")    
        