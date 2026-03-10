# Security Concepts

## Security Principle: Never trust the client

In multiplayer games, the client (player's computer) can be modified by hackers.
Because of this, the server must always verify player actions.

## Example Cheats

- Speed hacks
- Teleport hacks
- Packet manipulation

## Server-Side Validation

To prevent cheating, the server should validate:

- Player movement speed
- Impossible position jumps
- Suspicious behavior patterns

This project simulates a cheat detection system where the server analyzes player data and detects abnormal movement.

Client-server communication is the foundation of multiplayer security.

The server receives player movement data and must validate it.

If the client is modified, it may send impossible values such as:

- extremely high speed
- instant teleport
- unrealistic actions

The anti-cheat system must detect such anomalies.

## Speed Hack Detection

The server calculates the player's movement speed using the formula:

speed = distance / time

If the calculated speed exceeds the maximum allowed threshold,
the system flags the player as suspicious.

This prevents clients from sending manipulated movement data.