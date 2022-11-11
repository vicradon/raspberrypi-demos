import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep 

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

LED_PIN = 5
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()


