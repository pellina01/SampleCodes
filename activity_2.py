import time
import RPi.GPIO as GPIO
import _thread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT, initial = 1)
GPIO.setup(6,GPIO.OUT, initial = 0)
GPIO.setup(13,GPIO.OUT, initial = 0)
GPIO.setup(19,GPIO.OUT, initial = 0)
GPIO.setup(26,GPIO.OUT, initial = 0)


    

pins = [5,6,13,19,26]
control = True
counter = 0
delay = 0.5
tuple_input = ()

def user_input():
    global delay
    while True:
        delay = float(input('enter delay time: '))

def light(delay):
    global control
    global counter
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    if control == 1:
        GPIO.output(pins[counter],GPIO.HIGH)
        time.sleep(delay)
        counter += 1
        if counter == 5:
            counter = 4
            control = False
    else:
        counter -= 1
        GPIO.output(pins[counter],GPIO.HIGH)
        time.sleep(delay)
        if counter == 1:
            counter = 0
            control = True
        
user_input_thread = _thread.start_new_thread(user_input, tuple_input)

while True:
    light(delay)
    
        