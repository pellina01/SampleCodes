#from Adafruit_Python_DHT import Adafruit_DHT
#install adafruit sudo pip3 install Adafruit_DHT
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import mysql.connector

from mysql.connector import Error
GPIO.setmode(GPIO.BCM)
##GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(22,GPIO.IN)
##GPIO.setup(15,GPIO.IN)

pin = 22
sensor = Adafruit_DHT.DHT11

sound_pin = GPIO.setup(24,GPIO.OUT)
connection = mysql.connector.connect(host='localhost',database='db_py',
            user='admin',password='password',buffered=True)

GPIO.output(24,GPIO.LOW)
    
while True:
    print("read temp")
    GPIO.output(24,GPIO.LOW)
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    print(humidity,temperature)
##    GPIO.output(24,GPIO.HIGH)
    if ((temperature != None) or (humidity != None)):
        val = (temperature,humidity)
##        print (val[1])
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        if connection.is_connected():
            mySql_insert_query = """INSERT INTO temp_hum(temp, hum)VALUES (%s, %s)"""
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query,val)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into temp humidity table")
    else:
        GPIO.output(24,GPIO.HIGH)
        print("no reading")
    time.sleep(1)
GPIO.output(24,GPIO.LOW) 
    #answer = input('do you want to continue Y/N')
    #if answer == 'Y' or answer == 'y':
     #   GPIO.output(23,GPIO.LOW)
   
    #else:
     #   break

    
        
    

    





