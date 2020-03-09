import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
ctr = 0
while True:
    print("LED on")
    GPIO.output(22,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(22,GPIO.LOW)
    ctr += 1
    if ctr >= 3:
        break
    time.sleep(1)