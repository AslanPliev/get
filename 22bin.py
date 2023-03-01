import time
import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1 , 0 , 1 , 0 , 1 , 0 , 1 , 0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()