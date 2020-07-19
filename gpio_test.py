import RPi.GPIO as GPIO
import time

SW_1 = 25
SW_2 = 8
SW_3 = 7
SW_4 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SW_1,GPIO.OUT)
GPIO.setup(SW_2,GPIO.OUT)
GPIO.setup(SW_3,GPIO.OUT)
GPIO.setup(SW_4,GPIO.OUT)

for i in range(3):
	GPIO.output(SW_1,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(SW_1,GPIO.LOW)
	time.sleep(1)

for i in range(3):
	GPIO.output(SW_2,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(SW_2,GPIO.LOW)
	time.sleep(1)

for i in range(3):
	GPIO.output(SW_3,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(SW_3,GPIO.LOW)
	time.sleep(1)
	
for i in range(3):
	GPIO.output(SW_4,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(SW_4,GPIO.LOW)
	time.sleep(1)
