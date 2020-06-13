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

import Bookinginfo_support
from tkinter import messagebox as mb

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Bookinginfo_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Bookinginfo_support.init(w, top, *args, **kwargs)
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
        font10 = "-family {DejaVu Sans} -size 11 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans} -size 14 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font9 = "-family {Noto Serif Display} -size 21 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"

        top.geometry("600x450+359+191")
        top.title("Infopage")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.217, rely=0.111, height=61, width=319)
        self.Label1.configure(font=font9)
        self.Label1.configure(text='''Booking Information''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.033, rely=0.333, height=61, width=179)
        self.Label2.configure(font=font11)
        self.Label2.configure(text='''Enter name :''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.367, rely=0.356,height=33, relwidth=0.41)
        self.Entry1.configure(background="white")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(font="TkFixedFont")


        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.028, rely=0.433, height=61, width=179)
        self.Label3.configure(font=font11)
        self.Label3.configure(text='''Enter Ticket No:''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.367, rely=0.456,height=33, relwidth=0.41)
        self.Entry2.configure(background="white")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(font="TkFixedFont")


        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.533, rely=0.560, height=42, width=95)
        self.Button1.configure(borderwidth="6")
        self.Button1.configure(font=font10)
        self.Button1.configure(text='''Search''')
        def confirmation(self):
            import os
            name=self.Entry1.get()+"("+self.Entry2.get()+").txt"
            flist=os.listdir('/home/navanith/Documents/files')
            if self.Entry1.get()=="" and self.Entry2.get()=="":
                        root.destroy()
                        mb.showinfo(title="Error",message="Enter valid deatils")
            elif self.Entry1.get()=="":
                        root.destroy()
                        mb.showinfo(title="Error",message="Enter Name")
            elif self.Entry2.get()=="":
                        root.destroy()
                        mb.showinfo(title="Error",message="Enter Ticket number")
            elif name not in flist:
                root.destroy()
                mb.showinfo(title="confirmation",message="Ticket not confirmed\nPlease Book again!!!")
            else:
                for i in flist:
                    if i==name:
                        root.destroy()
                        mb.showinfo(title="confirmation",message="Booking Confirmed...!!!")

        self.Button1.configure(command=lambda: confirmation(self))

if __name__ == '__main__':
    vp_start_gui()