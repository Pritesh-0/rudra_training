import time
import serial
import keyboard

def ups():
	global speed1,speed2
	if keyboard.is_pressed('w'):
		speed1+=127

sob=serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
        
speed1,speed2=0,0


