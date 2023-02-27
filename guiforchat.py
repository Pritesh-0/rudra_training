import tkinter as tk
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
root=tk.Tk()
root.geometry("400x400")
msg=tk.StringVar()

def send():
	ans=msg.get()
	ser.write(msg.get().encode() + b'\r\n')
	msg.set("")
	print(f"Sent: {ans}")
	

h1=tk.Label(root,text='Your Message')
e1=tk.Entry(root,textvariable=msg)
btn=tk.Button(root,text='Send',command=send)
rec = ser.readline().decode().rstrip()
print(rec)
h2=tk.Label(root,text=rec)

h1.grid(row=0,column=0)
e1.grid(row=0,column=1)
btn.grid(row=1,column=1)
h2.grid(row=2,column=0)




root.mainloop()



