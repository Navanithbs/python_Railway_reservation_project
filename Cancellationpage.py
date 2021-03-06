#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    May 26, 2020 08:39:14 PM IST  platform: Linux

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

import Cancellationpage_support
import os
from tkinter import messagebox as mb

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Cancellationpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Cancellationpage_support.init(w, top, *args, **kwargs)
    return (w, top)

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
        font9 = "-family {DejaVu Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("611x402+358+208")
        top.title("Cancellation Page")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.131, rely=0.1, height=71, width=419)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font="-family {Noto Serif Display} -size 21 -weight bold -slant italic")
        self.Label1.configure(text='''Booking Cancellation''')

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.196, rely=0.323, relheight=0.311
                , relwidth=0.606)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(borderwidth="6")
        self.Labelframe1.configure(font="-family {DejaVu Sans} -size 11 -weight bold -slant italic -underline 1")
        self.Labelframe1.configure(text='''Customer Details :''')

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.027, rely=0.24, height=22, width=142
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(font="-family {DejaVu Sans} -size 11 -weight bold -slant italic")
        self.Label2.configure(text='''Name :''')

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.027, rely=0.48, height=22, width=142
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(font="-family {DejaVu Sans} -size 11 -weight bold -slant italic")
        self.Label3.configure(text='''Ticket no :''')

        self.Entry1 = tk.Entry(self.Labelframe1)
        self.Entry1.place(relx=0.459, rely=0.24, height=23, relwidth=0.503
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(foreground="#000000")        
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.459, rely=0.48, height=23, relwidth=0.503
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(foreground="#000000")        
        self.Entry2.configure(font="TkFixedFont")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.393, rely=0.721, height=31, width=141)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(borderwidth="6")
        self.Button1.configure(font=font9)
        self.Button1.configure(text='''Confirm''')      
        def delBooking(self):
                name=self.Entry1.get()
                first=name+"("+self.Entry2.get()+").txt"
                flist=os.listdir('/home/navanith/Documents/files')
                if name=="" and self.Entry2.get()=="":
                        root.destroy()
                        mb.showinfo(title="Error",message="Enter valid deatils")
                elif name=="":
                        root.destroy()
                        mb.showinfo(title="Error",message="Enter Name")
                elif self.Entry2.get()=="":
                        root.destroy()
                        mb.showinfo(title="Error",message="Enter Ticket number")
                elif first not in flist:
                        root.destroy()
                        mb.showinfo(title="confirmation",message="Please book the ticket before cancellation!!!")
                else:
                        os.remove('/home/navanith/Documents/files/'+first)
                        root.destroy()
                        mb.showinfo(title="confirmation",message="Booking Cancelled successfully...!!!")
        self.Button1.configure(command=lambda: delBooking(self))


if __name__ == '__main__':
    vp_start_gui()





