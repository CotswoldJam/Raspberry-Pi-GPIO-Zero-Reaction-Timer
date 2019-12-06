from gpiozero import Button, LED
from signal import pause

def press():
  print ( "Button PRESSED!" )
  led.on()

def unpress():
  print ( "Button unpressed!" )
  led.off()

led=LED(23)
led.off()
button=Button(24)
button.when_released=unpress
button.when_pressed=press

pause()
