import time
import RPi.GPIO as GPIO
from datetime import datetime
import subprocess

GPIO.setmode(GPIO.BOARD)

pirPin = 11

GPIO.setup(pirPin, GPIO.IN)

def LOGS(pirPin):
    with open("LOGS.txt", 'a') as fa:
        fa.write(str(datetime.now()) +'\n')
        fa.close()

    with open("signal.txt", 'w') as fw:
        fw.write("1")
        fw.close()

    time.sleep(5)

    with open("signal.txt", 'w') as fw:
        fw.write("0")
        fw.close()

subprocess.Popen(["python3", 'bot.py'])
print("ready")

try:
    GPIO.add_event_detect(pirPin, GPIO.RISING, callback = LOGS)

    while(1):
         time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
