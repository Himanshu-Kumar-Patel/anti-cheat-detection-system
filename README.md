# Anti-Cheat Detection System

This project demonstrates a basic server-authoritative anti-cheat architecture.

Features planned:
- Client movement simulation
- Server-side validation
- Speed hack detection
- Teleport detection
- Logging system
- Anti-cheat detection engine

Architecture:

Client -> Network -> Server Validator -> Detection Engine -> Logs

## Day 2 Progress

Implemented basic client-server communication using Python sockets.

The client sends player movement data in JSON format to the server.

The server receives and processes the player state.

This establishes the foundation for server-side anti-cheat validation.

## Day 3 Progress

Implemented the first anti-cheat detection module.

Features:
- Player movement history tracking
- Speed calculation
- Speed hack detection
- Logging suspicious events