# external module imports
import RPi.GPIO as GPIO
import time

# pin definitions
redLED = 18
blueLED = 23
yellowLED = 24
button = 26
count = 0

# pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(blueLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

# initial state for LEDs:
GPIO.output(redLED, GPIO.LOW)
GPIO.output(blueLED, GPIO.LOW)
GPIO.output(yellowLED, GPIO.LOW)

# blink loop
while count < 10:
	button_state = GPIO.input(button)
	if button_state == GPIO.LOW:
		GPIO.output(redLED, GPIO.HIGH)
		count = count + 1
		time.sleep(0.2)
	else:
		GPIO.output(redLED, GPIO.LOW)
	GPIO.output(redLED, GPIO.LOW)

for i in range(10, 0, -1):
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
