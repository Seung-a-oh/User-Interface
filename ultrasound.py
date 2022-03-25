from threading import Thread
import RPi.GPIO as GPIO
import time

from TTS import *
from button import *

GPIO.setmode(GPIO.BCM)

out = 25
range = 8

GPIO.setup(out, GPIO.IN)
GPIO.setup(range, GPIO.OUT)

# range pin
# 1m - False / 3m - True
GPIO.output(range, False)

while True:
    ADCValue = GPIO.input(out)
    print(ADCValue)
    time.sleep(0.2)

# 출력
# 감지 - 0 / 미감지 - 1