import socket
import json
from detection_engine import detect_speed_cheat

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started...")

conn, addr = server.accept()

print("Client connected:", addr)

while True:

    data = conn.recv(1024)

    if not data:
        break

    message = data.decode()

    player_data = json.loads(message)

    player_id = player_data["player_id"]
    x = player_data["x"]
    y = player_data["y"]
    timestamp = player_data["timestamp"]

    cheat = detect_speed_cheat(player_id, x, y, timestamp)

    if cheat:
     print("Speed hack detected")

    with open("logs/cheat_log.txt", "a") as log:
        log.write(f"Speed cheat detected for player {player_id}\n")