import serial
import keyboard
'''
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change the port as per your system
left_motor_speed = 0
right_motor_speed = 0
'''
def update_speeds():
    global left_motor_speed, right_motor_speed
    if keyboard.is_pressed('w'):
        left_motor_speed = 127
        right_motor_speed = 127
    elif keyboard.is_pressed('a'):
        left_motor_speed = -127
        right_motor_speed = 127
    elif keyboard.is_pressed('s'):
        left_motor_speed = -127
        right_motor_speed = -127
    elif keyboard.is_pressed('d'):
        left_motor_speed = 127
        right_motor_speed = -127
    else:
        left_motor_speed = 0
        right_motor_speed = 0
    print(left_motor_speed, right_motor_speed)

while True:
    update_speeds()


