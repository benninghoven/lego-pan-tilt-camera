from robot import Robot
from pynput import keyboard
import time

class Inp:
    def __init__(self):
        self.debounce = False
        self.listener = keyboard.Listener(
        on_press=self.on_press,
        on_release=self.on_release)
        self.listener.start()

        self.rob = Robot()
        self.rob.x.run_to_position(0)

    def on_press(self,key):
        if self.debounce:
            return
        self.debounce = not self.debounce
        try:
            print(f"{key}")
            if key.char == 'a':
                print("GOING LEFT")
                self.rob.x.start(10)
            elif key.char == 'd':
                print("GOING RIGHT")
                self.rob.x.start(-10)
            elif key.char == 'w':
                print("GOING UP")
                self.rob.y.start(10)
            elif key.char == 's':
                print("GOING DOWN")
                self.rob.y.start(-10)
            print("normal")
        except AttributeError:
            print(f"{key}")
            print("not normal")


    def on_release(self,key):
        print(f"{key} released")
        self.rob.x.stop()
        self.rob.y.stop()
        if key == keyboard.Key.esc:
            return False
        print(self.rob.GetPositions())
        self.debounce = not self.debounce




# ...or, in a non-blocking fashion:

bob = Inp()
bob.rob.x.coast()
bob.rob.y.coast()
time.sleep(5)


while True:
    pass


"""

while True:
    print('Press s or n to continue:')
    with keyboard.Events() as events:
        # Block for as much as possible
        event = events.get(1e6)
        if event.key == keyboard.KeyCode.from_char('s'):
            print("YES")
            break
"""

"""
rob = Robot()

print(rob.GetPositions())
"""
