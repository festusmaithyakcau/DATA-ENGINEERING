import socket
import threading
import logging

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 5050  # Port to listen on (non-privileged ports are > 1023)

clients = []
client_lock = threading.Lock()
messages = []  # List to store messages

# Configure logging
logging.basicConfig(filename='server_log.log', level=logging.INFO, format='%(asctime)s %(message)s')


def handle_client(conn, addr):
    """
    Handles communication with a single client. Receives messages and broadcasts them to all other clients.
    """
    print(f"[CONNECTED] {addr} connected.")
    username = conn.recv(1024).decode('utf-8')
    logging.info(f"Client connected: {username} ({addr})")

    # Send past messages upon connection
    past_messages = "\n".join(messages)  # Join messages with newline
    conn.sendall(past_messages.encode('utf-8'))

    with client_lock:
        clients.append((conn, username))
        broadcast(f"{username} has joined the chat!".encode('utf-8'))

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            with client_lock:
                messages.append(f"{username}: {data.decode('utf-8')}")  # Store message
                broadcast(f"{username}: {data}".encode('utf-8'), conn)
        except:
            break

    with client_lock:
        clients.remove((conn, username))
        broadcast(f"{username} has left the chat!".encode('utf-8'))
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")


def broadcast(message, sender=None):
    """
    Broadcasts a message to all connected clients except the sender (if provided).
    """
    for client, _ in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                client.close()
                with client_lock:
                    clients.remove(client)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
