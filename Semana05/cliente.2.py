import sys
import socket
import select
import errno

HEADER_LENGTH = 10

ip = sys.argv[1]
porta = sys.argv[2]
user  = sys.argv[3]

porta = int(porta)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)


username = user.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    messages = input(f'{user} > ')
    if messages:
        messages = messages.encode('utf-8')
        messages_header = f"{len(messages):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(messages_header + messages)

    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('encerrada pelo server...')
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f'{username} > {messages}')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue

    except Exception as e: #encerra cso apresente algum erro 
        print('Reading error: '.format(str(e)))
        sys.exit()