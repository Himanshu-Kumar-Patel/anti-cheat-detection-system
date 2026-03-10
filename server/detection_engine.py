import math

MAX_ALLOWED_SPEED = 5

player_history = {}

def detect_speed_cheat(player_id, x, y, timestamp):

    if player_id not in player_history:
        player_history[player_id] = (x, y, timestamp)
        return False

    last_x, last_y, last_time = player_history[player_id]

    distance = math.sqrt((x - last_x)**2 + (y - last_y)**2)

    time_diff = timestamp - last_time

    if time_diff == 0:
        return False

    speed = distance / time_diff

    player_history[player_id] = (x, y, timestamp)

    if speed > MAX_ALLOWED_SPEED:
        return True

    return False