import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 5050  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    username = input("Enter your username: ")
    s.send(username.encode('utf-8'))

    while True:
        data = input()
        if data == 'quit':
            break
        s.send(f"{data}".encode('utf-8'))

        data = s.recv(1024).decode('utf-8')
        print(data)

print("Closing connection...")
