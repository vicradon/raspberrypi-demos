import RPi.GPIO as GPIO
from time import sleep 

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

in1 = 26
in2 = 21
in3 = 20
in4 = 16
enA = 19
enB = 13

encoder1 = 14

GPIO.setup(in1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(in2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(enA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(in3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(in4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(enB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(encoder1, GPIO.IN)

speedControl1 = GPIO.PWM(enA, 1000)
speedControl2 = GPIO.PWM(enB, 1000)

speed = 90

last_read_speed_enc1_val = None
encoder_steps = 20
distance_per_step = 1/20

enc1_step_count = 0
total_enc1_step_count = 0


try:
    while True:
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
        speedControl1.start(50)
        speedControl2.start(100)

        current_speed_enc1_val = GPIO.input(encoder1)

        if last_read_speed_enc1_val != current_speed_enc1_val:
            last_read_speed_enc1_val = current_speed_enc1_val
            enc1_step_count += 1
            total_enc1_step_count += 1

        if enc1_step_count == encoder_steps:
            print(enc1_step_count, total_enc1_step_count)
            enc1_step_count = 0
            # print("One rev travelled")
            print(f"Total distance travelled = {total_enc1_step_count * distance_per_step}")


except KeyboardInterrupt:
    GPIO.cleanup()

