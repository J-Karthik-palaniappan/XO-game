import tkinter as t
from tkinter import *
import random
from tkinter import messagebox

tk=Tk()
tk.title("X-O")
l=[['','',''],['','',''],['','','']]
colour={'X':'blue','O':'green'}
mov=1

class btn:
    def __init__(self,row,column):
        self.row=row
        self.column=column
        
    def print(self):
        self.but=Button(tk,padx=1,bg="papaya whip",width=3,text=" ",bd=15,font=('arial',60,'bold'),relief=SUNKEN,command=self.clicked)
        self.but.grid(row=self.row,column=self.column)

    def clicked(self):
        txt=['X','O'][mov%2]
        l[self.row][self.column]=txt
        self.but.config(text=txt,state=t.DISABLED,disabledforeground=colour[txt])
        self.wincheck()
        change()

    def wincheck(self):
        txt=['X','O'][mov%2]
        for i in range(3):
            if (l[i][0]==l[i][1]==l[i][2]==txt) or (l[0][i]==l[1][i]==l[2][i]==txt):
                messagebox.showinfo("game message",txt+" won\nloosers start")
                start()
        if (l[1][1]==l[2][2]==l[0][0]==txt) or (l[2][0]==l[1][1]==l[0][2]==txt):
            messagebox.showinfo("game message",txt+" won\nloosers start")
            start()
        elif ('' not in l[0]) and ('' not in l[1]) and ('' not in l[2]):
            messagebox.showinfo("game message","Tie !!\n awesome game :)")
            start()

def start():
    global l
    for i in range(3):
        for j in range(3):
            s=btn(i,j)
            s.print()
    l=[['','',''],['','',''],['','','']]
    colour={'X':'blue','O':'green'}

def change():
    global mov
    mov+=1
start()
