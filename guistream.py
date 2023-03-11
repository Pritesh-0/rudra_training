from tkinter import *
import webbrowser

root = Tk()

new = 1
url = "http://192.168.156.87:8080/" #Replace with the ip of stream

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(root, text = "Stream Cam",command=openweb)
Btn.pack()

root.mainloop()
