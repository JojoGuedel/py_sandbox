from pynput import keyboard
from key import *

import socket
import pickle

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

# HOST = socket.gethostname()
# HOST = "192.168.120.108"
HOST = "192.168.178.44"
PORT = 9999

print(f"Connecting to: {HOST}:{PORT}")
client = socket.socket()
client.connect((HOST, PORT))

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

client.close()