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