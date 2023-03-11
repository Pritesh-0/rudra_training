import tkinter as tk
import serial
import pygame
import time
pygame.init()
m1,m2,m3,m4=64,192,64,192
#joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
root=tk.Tk()
root.geometry("600x600")

send_box=tk.Entry(root,width=50)
send_box.grid(row=6,column=2)

def fwd():
	if (m1<127 and m2<127 and m3<127 and m4<127):
		m1+=1
		m2+=1
		m3+=1
		m4+=1
	
	
def bwd():
	if (m1>1 and m2>1 and m3>1 and m4>1):
		m1-=1
		m2-=1
		m3-=1
		m4-=1
	
def lt():
	pass
	
def rt():
	pass

def stp():
	pass


def send():
	msg=send_box.get()
	#ser.write(msg.encode())
	send_box.delete(0,tk.END)
	print(f"Sent: {msg}")
	
	

btn=tk.Button(root,text='Send',command=send)
btn.grid(row=7,column=2)


rcv_box=tk.Text(root,width=50,height=20)
rcv_box.grid(row=8,column=2)

msg='1'
def read():
	t=1500
	#msg=ser.readline().decode()
	if msg:
		rcv_box.insert(tk.END,msg + '\n')
	root.after(t,read)	

read()



tk.Button(root,text='Forward',command=fwd).grid(row=1,column=2)
tk.Button(root,text='Backward',command=bwd).grid(row=3,column=2)
tk.Button(root,text='Left',command=lt).grid(row=2,column=1)
tk.Button(root,text='Right',command=rt).grid(row=2,column=3)
tk.Button(root,text='Stop',command=stp).grid(row=2,column=2)

root.mainloop()

#ser = serial.Serial('/dev/ttyUSB2', 9600, timeout=1)
