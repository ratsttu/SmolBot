import pygame

pygame.init()

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)  # Use 0 to select the first connected controller
joystick.init()

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
    

while True:
    for event in pygame.event.get():

        if event.type == pygame.JOYBUTTONDOWN:
            button_pressed = event.button  # Get the button that was pressed
            print(f"Button {button_pressed} pressed")
            if (button_pressed == 0):
                exit()

        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 4:  # Y-axis of left joystick
                y_axis_value = event.value
                if (-1.01 < y_axis_value < -0.1):
                    pwm_width = abs(0.9*y_axis_value+1.44)
                    if (pwm_width < 0.55):
                        pwm_width = 0.55
                       
                    print(f"Left Y-axis value: {y_axis_value}")
            
                    print(pwm_width)
                    pwm18.start(PWMControls(pwm_width))
                    pwm19.start(PWMControls(pwm_width))

                elif (0.1 < y_axis_value < 1.1):
                    pwm_width = abs(0.64888888889 *y_axis_value+1.3951111111)
                    if (pwm_width > 2.044):
                        pwm_width = 2.044
                    print(f"Left Y-axis value: {y_axis_value}")
            
                    print(pwm_width)
                    pwm18.start(PWMControls(pwm_width))
                    pwm19.start(PWMControls(pwm_width))
                else:
                    pwm18.start(0)
                    pwm19.start(0)

            
            elif event.axis == 1:  # Y-axis of right joystick
                
                yr_axis_value = event.value
                if (-1.01 < yr_axis_value < -0.1):
                    pwm_width2 = abs(-0.6*yr_axis_value+1.4)
                    if (pwm_width2 > 2.044):
                        pwm_width2 = 2.044
                    print(f"Left Y-axis value: {yr_axis_value}")
            
                    print(pwm_width2)
                    pwm12.start(PWMControls(pwm_width2))
                    pwm13.start(PWMControls(pwm_width2))

                elif (0.1 < yr_axis_value < 1.1):
                    pwm_width2 = abs(-0.9 *yr_axis_value+1.44)
                    if (pwm_width2 < 0.55):
                        pwm_width2 = 0.55
                    print(f"Left Y-axis value: {yr_axis_value}")
            
                    print(pwm_width2)
                    pwm12.start(PWMControls(pwm_width2))
                    pwm13.start(PWMControls(pwm_width2))
                else:
                    pwm12.start(0)
                    pwm13.start(0)


                #print(f"Right Y-axis value: {yr_axis_value}")
        
        # Handle other events as needed (e.g., JOYBUTTONUP, JOYHATMOTION, etc.)
pwm18.stop()
pwm19.stop()
pwm12.stop()
pwm13.stop()
GPIO.cleanup()

pygame.quit()