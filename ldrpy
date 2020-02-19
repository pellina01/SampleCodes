import Adafruit_DHT
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#GPIO.setup(7,GPIO.IN)
#GPIO.setup(7, GPIO.OUT)
#GPIO.output(7, GPIO.LOW)
##GPIO.setup(7,GPIO.IN)
##GPIO.setup(12,GPIO.OUT)
##GPIO.setup(18,GPIO.IN)

GPIO.setup(7,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
GPIO.output(7, GPIO.LOW)
sensor = Adafruit_DHT.DHT11
pin = 24

while True:
    
    print(GPIO.input(7))
    print("read temp")
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    print(humidity,temperature)
    time.sleep(1)
    if (GPIO.input(7) == 0 or temperature != None or humidity != None) :
        GPIO.output(18,GPIO.HIGH)
##    else:
GPIO.output(7,GPIO.LOW)
    
    