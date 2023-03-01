import tkinter as tk
import serial
ser = serial.Serial('/dev/pts/0', 9600, timeout=1)
root=tk.Tk()
root.geometry("400x400")

#h1=tk.Label(root,text='Your Message')
#h1.grid(row=0,column=0)
send_box=tk.Entry(root,width=50)
send_box.pack(pady=10)


def send():
	msg=send_box.get()
	ser.write(msg.encode())
	send_box.delete(0,tk.END)
	print(f"Sent: {msg}")

btn=tk.Button(root,text='Send',command=send)
btn.pack(pady=10)

rcv_box=tk.Text(root,width=50,height=20)
rcv_box.pack()


def read():
	msg=ser.readline().decode()
	if msg:
		rcv_box.insert(tk.END,msg + '\n')
	
	root.after(100,read)	

read()

root.mainloop()



