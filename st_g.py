import serial
import pygame
import time
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

sob=serial.Serial(
		port='/dev/ttyUSB0',
		baudrate=9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
		)      

left_motor_speed = 64
right_motor_speed = 192

def update_speeds():
	global left_motor_speed, right_motor_speed,b1,b2,b3
	pygame.event.get()
	joystick=joysticks[0]
	b1,b2,b3,b4 = joystick.get_button(0),joystick.get_button(2),joystick.get_button(4),joystick.get_button(5)
	if b3:
		if b1 and right_motor_speed<255:
			right_motor_speed += 1
		elif b2 and right_motor_speed>128:
			right_motor_speed -= 1
	elif not b3:
		if b1 and left_motor_speed<127:
			left_motor_speed += 1
		elif b2 and left_motor_speed>1:
			left_motor_speed -= 1
	if b4:
		left_motor_speed =64
		right_motor_speed =192
	#command = chr(left_motor_speed) + chr(right_motor_speed)
	#cmd=command.encode()
	#print(cmd)
	#sob.write(command.encode())
	#breakpoint()
	print(left_motor_speed,right_motor_speed)
	sob.write(left_motor_speed.to_bytes(1,'big'))
	sob.write(right_motor_speed.to_bytes(1,'big'))    
	#sob.write(bytes(command,encoding='utf-8'))

while True :
	update_speeds()
	
	time.sleep(0.1)
	
	
	if ((not b1) or (b1 or b2) and b3) and left_motor_speed > 64:
		left_motor_speed -= 1
	if not b1 and right_motor_speed > 192:
		right_motor_speed -= 1
	if ((not b2) or (b1 or b2) and b3)and left_motor_speed < 64:
		left_motor_speed += 1
	if not b2 and right_motor_speed < 192:
		right_motor_speed += 1
		
	#print(left_motor_speed,right_motor_speed)

