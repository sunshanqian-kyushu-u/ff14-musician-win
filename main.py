# from pymouse import PyMouse
from pykeyboard import PyKeyboard

import time

keyboard = PyKeyboard()

for i in range(5, 0, -1):
    print("[INFO] Count down: " + str(i))
    time.sleep(1)

print("[INFO] Playing...")
keyboard.tap_key('a', n=5, interval=2)

