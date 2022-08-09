from key import *
from pynput import keyboard

import socket
import pickle

HOST = socket.gethostname()
PORT = 9999

def on_press(key):
    net_key = KeyEvent(key, KeyAction.PRESSED)
    data_str = pickle.dumps(net_key)
    client.send(data_str)

def on_release(key):
    net_key = KeyEvent(key, KeyAction.RELEASED)
    data_str = pickle.dumps(net_key)
    client.send(data_str)

    if key == keyboard.Key.esc:
        return False

server = socket.socket()
server.bind((HOST, PORT))

print(f"Hosting server: {HOST}:{PORT}")
print("Waiting for client to connect...")

server.listen(5)
client, address = server.accept()
print(f"Client connected: {address}")

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

server.close()
