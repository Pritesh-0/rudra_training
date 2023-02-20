import time
import serial
import keyboard

def run1(speed):
	sob.write(sp.to_bytes(speed,'big'))
	
def run2(speed):
	sob.write(sp.to_bytes(speed,'big'))

key_press_times = {'w': None, 'a': None, 's': None, 'd': None}

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
                
speed1,speed2=0,0

while True:
    for key in key_press_times.keys():
        if keyboard.is_pressed(key):
            if key_press_times[key] is None:
                key_press_times[key] = time.time()
        else:
            if key_press_times[key] is not None:
                duration = time.time() - key_press_times[key]
                if key=='w':
                	print(duration*1000)
                	if speed1<=127:
                		speed1+=int((1000*duration) % 156.666)
                print(speed1)	
                key_press_times[key] = None
    time.sleep(0.01)
    

