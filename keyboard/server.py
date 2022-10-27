from key import *
from pynput import keyboard

import socket
import pickle

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket()
server.bind((HOST, PORT))

print(f"Hosting server: {HOST}:{PORT}")
print("Waiting for client to connect...")

server.listen(100)
client, address = server.accept()
print(f"Client connected: {address}")

cb_controller = keyboard.Controller()

while True:
    data = client.recv(1024)
    object = pickle.loads(data)

    if object.action == KeyAction.PRESSED:
        cb_controller.press(object.key)
    elif object.action == KeyAction.RELEASED:
        cb_controller.release(object.key)

        if object.key == keyboard.Key.esc:
            break

server.close()
