import time
import RPi.GPIO as GPIO
leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
i = 1
for i in range(1,8,1):
    GPIO.output(leds[i], 1)
    time.sleep(0.2)
    GPIO.output(leds[i], 0)
    i = i + 1
time.sleep(15)
GPIO.output(leds, 0)
GPIO.cleanup()