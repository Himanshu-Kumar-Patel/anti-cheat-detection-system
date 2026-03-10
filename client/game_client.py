import socket
import json
import time

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

player = {
    "player_id": 1,
    "x": 0,
    "y": 0
}

def move_player(direction):
    if direction == "up":
        player["y"] += 1
    elif direction == "down":
        player["y"] -= 1
    elif direction == "left":
        player["x"] -= 1
    elif direction == "right":
        player["x"] += 1

while True:

    command = input("Move (up/down/left/right): ")

    move_player(command)

    player["timestamp"] = time.time()

    message = json.dumps(player)

    client.send(message.encode())

    print("Sent data:", player)