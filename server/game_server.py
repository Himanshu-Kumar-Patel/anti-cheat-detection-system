import socket
import json

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started. Waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024)

    if not data:
        break

    message = data.decode()

    try:
        player_data = json.loads(message)
        print("Received player data:", player_data)
    except:
        print("Invalid data received")