# Script to send paths to run in blender:
#   blender_client.py script1.py script2.py

import socket
import sys

PORT = 8081
HOST = "localhost"


def send_commands(commands: list[str], host: str = "localhost", port: int = 8081):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host, port))

    for cmd in commands:
        clientsocket.sendall(cmd.encode("utf-8") + b'\x00')
