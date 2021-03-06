#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    May 29, 2020 01:45:04 PM IST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import paymentpage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    paymentpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    paymentpage_support.init(w, top, *args, **kwargs)
    return (w, top)
import os
from tkinter import messagebox as mb

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Sans} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Noto Serif} -size 30 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"

        top.geometry("590x450+392+191")
        top.title("Payments")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.153, rely=0.067, height=61, width=419)
        self.Label1.configure(font=font13)
        self.Label1.configure(text='''Payments Page''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.186, rely=0.289, relheight=0.478
                , relwidth=0.686)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="6")
        self.Frame1.configure(relief="groove")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.049, rely=0.186, height=22, width=137)
        self.Label2.configure(borderwidth="3")
        self.Label2.configure(font=font10)
        self.Label2.configure(text='''Card number :''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.049, rely=0.326, height=21, width=144)
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(font=font10)
        self.Label3.configure(text='''Name on card :''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.074, rely=0.465, height=22, width=126)
        self.Label4.configure(font=font10)
        self.Label4.configure(text='''Cvv :''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.395, rely=0.651, height=39, width=97)
        self.Button1.configure(borderwidth="5")
        self.Button1.configure(font=font11)
        self.Button1.configure(text='''Confirm''')
        def next(self):
            self.x=0
            self.count=21100
            flist=os.listdir('/home/navanith/Documents/files')
            for i in flist:
                self.x=self.x+1
            self.count=self.count+self.x
            if self.Entry1.get()=="" or self.Entry2.get()=="" or self.Entry3.get()=="":
                mb.showinfo(title="Error",message="Enter valid details..!!!!")
            else:
                root.destroy()
                mb.showinfo(title="confirmation",message="Booking Successfull...!!!\nYour Ticket number is :"+str(self.count))
        self.Button1.configure(command=lambda: next(self))


        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.444, rely=0.186,height=23, relwidth=0.41)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.444, rely=0.326,height=23, relwidth=0.41)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.444, rely=0.465,height=23, relwidth=0.41)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")

if __name__ == '__main__':
    vp_start_gui()





