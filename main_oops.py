from tkinter import *
from tkinter import ttk
import json
from ttkbootstrap import *


class window:
    key = json.load(open("nkey.json"))
    dec = json.load(open("dkey.json"))

    def __init__(self,win,title) -> None:
        self.win=win
        self.win.title(title)
        l1=Label(self.win,text="Enter a string or password you wanna encrypt:")
        self.t=Text(self.win,width=50,height=5,bd=5)
        l1.grid(row=0,columnspan=2)
        self.t.grid(row=1,columnspan=2)

        self.win.bind('<Return>',self.encry)

        butt=ttk.Button(self.win,text="Clear",command=self.clear)
        butt.grid(row=2,column=0)
        lab=Label(self.win,text="Hit ENTER to see the encrpted text")
        lab.grid(row=4,columnspan=2)
        self.r=Text(self.win,width=50,height=5,bd=5)
        self.r.grid(row=5,columnspan=2)

        ass=ttk.Button(self.win,text="Decode",command=self.decode)
        ass.grid(row=2,column=1)  

    def encry(self,event):
        msg=self.t.get("1.0",END)
        i=0
        global result
        result=""   
        while i<len(msg):
            result+=self.key[msg[i]]
            i+=1
        self.r.insert(END,result)
        self.r.config(state=DISABLED)
        pass

    def clear(self):
        self.t.delete(1.0,END)
        self.r.config(state=NORMAL)
        self.r.delete(1.0,END)
    def decode(self):
        msg=self.t.get("1.0",END)
        i=0
        
        result=""   
        while i<len(msg):
            result+=self.dec[msg[i]]
            i+=1
        self.r.insert(END,result)
        self.r.config(state=DISABLED)


if __name__ == "__main__":
    win= Style(theme='yeti').master
    app =window(win,'Secure Password')

    win.mainloop()

