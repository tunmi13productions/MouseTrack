
# MIT License
# 
# Copyright (c) 2024 tunmi13productions
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

import time
from accessible_output2.outputs.auto import *
from pynput.mouse import Controller, Listener as MouseListener
from pynput import mouse
from math import sqrt

speech = Auto()
mouse_controller = Controller()
last_x, last_y = (0, 0)

# Function to notify when a mouse button is pressed
def on_click(x, y, button, pressed):
    if pressed:
        # Convert button to string.
        button_str = str(button).split(".")[-1]
        speech.speak(f"{button_str.capitalize()} click at {x}, {y}", True)

# Gets the 2D distance. This may be used in the future.
def get_distance(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return sqrt(x * x + y * y)

# Start mouse listener for click events
mouse_listener = MouseListener(on_click=on_click)
mouse_listener.start()

try:
    while True:
        time.sleep(0.05)
        x, y = mouse_controller.position
        if (last_x, last_y) == (x, y):
            continue
        else:
            last_x, last_y = x, y
            speech.speak(f"{last_x}, {last_y}", True)
except KeyboardInterrupt:
    print(f"Terminating.")
