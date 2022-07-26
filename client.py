import threading
import socket

nickname = input('Choose an Nickname... ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 61000))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK?':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An Error occurred!')
            client.close()
            break


def client_send():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
