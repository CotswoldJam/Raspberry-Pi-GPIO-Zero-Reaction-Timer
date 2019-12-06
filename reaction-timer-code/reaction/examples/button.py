from gpiozero import Button
from signal import pause

def press():
  print ( "Button PRESSED!" )

def unpress():
  print ( "Button unpressed!" )

button = Button(24)
button.when_released = unpress
button.when_pressed = press

pause()
