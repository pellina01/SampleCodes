import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT, initial = 0)
led = GPIO.PWM(26, 5000)
led.start(1)
while True:
    try:
        duty_cycle = float(input('enter duty cycle percentage(0 to 100): '))
    except:
        print('Enter integer/float values only! ')
    led.ChangeDutyCycle(duty_cycle)
