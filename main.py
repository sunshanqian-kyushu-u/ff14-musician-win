# from pymouse import PyMouse
from pynput.keyboard import Key, Controller

import time

keyboard = Controller()

for i in range(5, 0, -1):
    print("[INFO] Count down: " + str(i))
    time.sleep(1)

print("[INFO] Playing...")

keyboard.press('a')

time.sleep(5)

keyboard.release('a')

with keyboard.pressed(Key.shift, 's'):          # can't work without with
    pass

# keyboard.pressed(Key.shift, 's')

time.sleep(5)

with keyboard.pressed('a'):
    pass

# keyboard.pressed('a')


