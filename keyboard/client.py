from pynput import keyboard
from key import *

import socket
import pickle

HOST = socket.gethostname()
PORT = 9999

client = socket.socket()
client.connect((HOST, PORT))

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

client.close()