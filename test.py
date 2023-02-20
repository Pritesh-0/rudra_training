import serial
import keyboard
import time

'''
sob=serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )      
'''
left_motor_speed = 64
right_motor_speed = 192

def update_speeds():
    global left_motor_speed, right_motor_speed
    if keyboard.is_pressed('w') and left_motor_speed<127:
        left_motor_speed += 1
        #right_motor_speed += 1
    elif keyboard.is_pressed('a') and right_motor_speed<255:
        #left_motor_speed -= 1
        right_motor_speed += 1
    elif keyboard.is_pressed('s') and left_motor_speed>1:
        left_motor_speed -= 1
        #right_motor_speed -= 1
    elif keyboard.is_pressed('d') and right_motor_speed>128:
        #left_motor_speed += 1
        right_motor_speed -= 1
    elif keyboard.is_pressed('x'):
    	left_motor_speed =64
    	right_motor_speed =192

    #command = chr(left_motor_speed) + chr(right_motor_speed)
    #ser.write(command.encode())
    #sob.write(sp.to_bytes(1,'big'))
    

while True :
    update_speeds()
    time.sleep(0.1)

    # Decrease motor speeds when keys are released
    if not keyboard.is_pressed('w') and left_motor_speed > 64:
        left_motor_speed -= 1
    if not keyboard.is_pressed('a') and right_motor_speed > 192:
        right_motor_speed -= 1
    if not keyboard.is_pressed('s') and left_motor_speed < 64:
        left_motor_speed += 1
    if not keyboard.is_pressed('d') and right_motor_speed < 192:
        right_motor_speed += 1
        
    #print(left_motor_speed,right_motor_speed)

