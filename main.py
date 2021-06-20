from tkinter import *
from tkinter import ttk as tit
import json

ja = Tk()
key = json.load(open("nkey.json"))

def encry(event):
    
    msg=t.get("1.0",END)
    i=0
    global result
    result=""   
    while i<len(msg):
        result+=key[msg[i]]
        i+=1
    r.insert(END,result)
    r.config(state=DISABLED)
    
def clear():
    t.delete(1.0,END)
    r.config(state=NORMAL)
    r.delete(1.0,END)

dec = json.load(open("dkey.json"))
    
def decode():
    msg=t.get("1.0",END)
    i=0
    result=""   
    while i<len(msg):
        result+=dec[msg[i]]
        i+=1
    r.insert(END,result)
    


l1=Label(ja,text="Enter a string or password you wanna encrypt:")
t=Text(ja,width=50,height=5,bd=5)
l1.grid(row=0,columnspan=2)
t.grid(row=1,columnspan=2)

ja.bind('<Return>',encry)

butt=tit.Button(ja,text="Clear",command=clear)
butt.grid(row=2,column=0)
lab=Label(ja,text="Hit ENTER to see the encrpted text").grid(row=4,columnspan=2)
r=Text(ja,width=50,height=5,bd=5)
r.grid(row=5,columnspan=2)

ass=tit.Button(ja,text="Decode",command=decode)
ass.grid(row=2,column=1)    

ja.mainloop()
