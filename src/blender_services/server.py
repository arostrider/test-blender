# Script to run from blender:
#   blender --python blender_server.py

import os
import socket
import traceback

PORT = 8081
HOST = "localhost"
PATH_MAX = 4096


def _execfile(filepath):
    global_namespace = {
        "__file__": filepath,
        "__name__": "__main__",
    }
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), global_namespace)


def run_server(host: str = "localhost", port: int = 8081, path_max_size: int = 4096):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((host, port))
    serversocket.listen(1)

    print(f"Listening on {host}:{port}")
    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(path_max_size)

        for filepath in buf.split(b'\x00'):
            if filepath:
                print(f"Executing: {filepath}")
                try:
                    _execfile(filepath)
                except:
                    traceback.print_exc()


if __name__ == "__main__":
    print("Server starting...")
    run_server()
    print("Server shutdown.")
