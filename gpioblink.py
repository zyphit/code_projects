# external module imports
import RPi.GPIO as GPIO
import time

# pin definitions
redLED = 18
blueLED = 23
yellowLED = 24

# pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(blueLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)

# initial state for LEDs:
GPIO.output(redLED, GPIO.LOW)
GPIO.output(blueLED, GPIO.LOW)
GPIO.output(yellowLED, GPIO.LOW)

# blink loop
for i in range(150, 0, -1):
	GPIO.output(redLED, GPIO.HIGH)
	time.sleep(i*0.002)
	GPIO.output(redLED, GPIO.LOW)
	GPIO.output(yellowLED, GPIO.HIGH)
	time.sleep(i*0.002)
	GPIO.output(yellowLED, GPIO.LOW)
	GPIO.output(blueLED,GPIO.HIGH)
	time.sleep(i*0.002)
	GPIO.output(redLED, GPIO.LOW)
	GPIO.output(blueLED, GPIO.LOW)
	GPIO.output(yellowLED, GPIO.LOW)
GPIO.cleanup()

