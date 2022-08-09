class KeyAction:
    PRESSED = 0
    RELEASED = 1

class KeyEvent:
    def __init__(self, key, action):
        self.key = key
        self.action = action