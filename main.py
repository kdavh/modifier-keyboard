import time

import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board

# the keyboard object!
kbd = Keyboard()


class Button():
    def __init__(self, name, pin, key):
        # make pin object, make it input w/pullup
        self._io = digitalio.DigitalInOut(pin)
        self._io.direction = digitalio.Direction.INPUT
        self._io.pull = digitalio.Pull.UP
        self._name = name
        self._pin = pin
        self._key = key
        self._kbd_pressed = False
    
    @property
    def pressed(self):
        return not self._io.value
    
    def update_keyboard(self, kbd):
        if self.pressed:
            if not self._kbd_pressed:
                print("{} key pressed".format(self._name))
                self._kbd_pressed = True
                kbd.press(self._key)
        else:
            if self._kbd_pressed:
                print("{} key released".format(self._name))
                self._kbd_pressed = False
                kbd.release(self._key)
        
        
# our array of button objects
# The button pins we'll use, each will have an internal pullup
buttons = [
    Button('left ctrl', board.D12, Keycode.LEFT_CONTROL),
    Button('left gui', board.D11, Keycode.LEFT_GUI),
    Button('left alt', board.D10, Keycode.LEFT_ALT),
    Button('left shift', board.D9, Keycode.LEFT_SHIFT),
]


print("Waiting for button presses")

while True:
    # check each button
    for button in buttons:
        button.update_keyboard(kbd)

    time.sleep(0.01)
