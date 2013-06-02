import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#x = [0, 1, 4, 17, 18, 21, 22, 23, 24, 10, 9, 25, 11, 8, 7]
x = [21, 22, 23, 24, 10, 9, 25, 11, 8, 7]

for i in x:
  GPIO.setup(i, GPIO.OUT)

for j in range(0,10):
  for i in x:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(i, GPIO.LOW)

