import threading
import socket

host = '127.0.0.1'
port = 61000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


# Function to handle clients' connections


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except client.DoesNotExist:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat room!'.encode('ascii'))
            nicknames.remove(nickname)
            break


# Main function to receive the clients connection


def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f"connection is established with {str(address)}")
        client.send('NICK?'.encode('ascii'))
        nickname = client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        print(f'The Nicknames of this client is {nickname}'.encode('ascii'))
        broadcast(f"{nickname} has connected to the chat room".encode('ascii'))
        client.send("connected to the server!".encode('ascii'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


print("server is listening")
receive()
