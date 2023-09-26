import RPi.GPIO as GPIO
import time

# Set GPIO pin number for PWM output
pwm_pin18 = 18  # Use the appropriate GPIO pin
pwm_pin19 = 19  # Use the appropriate GPIO pin
pwm_pin12 = 12  # Use the appropriate GPIO pin
pwm_pin13 = 13  # Use the appropriate GPIO pin

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin18, GPIO.OUT)
GPIO.setup(pwm_pin19, GPIO.OUT)
GPIO.setup(pwm_pin12, GPIO.OUT)
GPIO.setup(pwm_pin13, GPIO.OUT)

# Create PWM instance with the desired frequency (e.g., 50 Hz)
pwm_frequency = 50  # 50 Hz
pwm18 = GPIO.PWM(pwm_pin18, pwm_frequency)
pwm19 = GPIO.PWM(pwm_pin19, pwm_frequency)
pwm12 = GPIO.PWM(pwm_pin12, pwm_frequency)
pwm13 = GPIO.PWM(pwm_pin13, pwm_frequency)

def PWMControls(pulse_width_ms):
    duty_cycle = (pulse_width_ms / (1000.0 / pwm_frequency)) * 100.0
    # Start PWM with the specified duty cycle
    return duty_cycle
    

pwm12.start(PWMControls(.5))
pwm13.start(PWMControls(.5))
pwm18.start(PWMControls(.5))
pwm19.start(PWMControls(.5))
               
time.sleep(7)
               
pwm18.stop()
pwm19.stop()
pwm12.stop()
pwm13.stop()
GPIO.cleanup()
