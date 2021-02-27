from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import keyboard

import time

word = input("Please type in a sentence: ")
times = input("Type in the amount of messages to be sent: ")

print("Now select your textbox and wait for the spam to start.")
print("Initiating spam in 5 seconds.")
print("Press CTRL+C to cancel.")

counter = 0

time.sleep(5)

keyboard2 = KeyboardController()

while int(counter) < int(times):
    for x in word:
        keyboard2.press(x)
    keyboard.press_and_release('enter')
    counter = counter+1