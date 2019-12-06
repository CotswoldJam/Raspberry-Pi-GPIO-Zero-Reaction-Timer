from gpiozero import LED, Button
from signal import pause
from random import uniform
from time import time, sleep
timestarted=None

def press():
  global timestarted,led,button
  print ( "Reaction time: %.3f" % (time()-timestarted) )
  led.off()
  sleep(2)
  reset()

def reset():
  global timestarted,led
  sleep(uniform(0.5,3))
  led.blink(0.1,0.4,4,False)
  led.on()
  timestarted=time()

led=LED(23)
led.off()
button=Button(24)
button.when_pressed=press
reset()

pause()
