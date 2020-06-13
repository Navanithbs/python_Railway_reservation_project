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

import admin_support
import os.path
from tkinter import messagebox as mb
from os.path import join as pjoin

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    admin_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    admin_support.init(w, top, *args, **kwargs)
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
        font11 = "-family {Noto Serif} -size 21 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size 10 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font13 = "-family {DejaVu Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {DejaVu Sans} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+340+170")
        top.title("Admin")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.2, rely=0.044, height=81, width=429)
        self.Label1.configure(background="#5e5e5e")
        self.Label1.configure(font=font11)
        self.Label1.configure(text='''Railway Reservation System''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.067, rely=0.267, relheight=0.567
                , relwidth=0.858)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief="groove")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.019, rely=0.157, height=21, width=130)
        self.Label2.configure(font=font14)
        self.Label2.configure(text='''Train_name :''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.019, rely=0.314, height=21, width=119)
        self.Label3.configure(font=font14)
        self.Label3.configure(text='''Train_no :''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.019, rely=0.471, height=21, width=107)
        self.Label4.configure(font=font14)
        self.Label4.configure(text='''From :''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.019, rely=0.627, height=21, width=109)
        self.Label5.configure(font=font14)
        self.Label5.configure(text='''To :''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.019, rely=0.784, height=21, width=135)
        self.Label6.configure(font=font13)
        self.Label6.configure(text='''Departure_time :''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.291, rely=0.157,height=23, relwidth=0.594)
        self.Entry1.configure(background="white")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.291, rely=0.314,height=23, relwidth=0.594)
        self.Entry2.configure(background="white")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(font="TkFixedFont")

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.291, rely=0.471,height=23, relwidth=0.594)
        self.Entry3.configure(background="white")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(font="TkFixedFont")

        self.Entry4 = tk.Entry(self.Frame1)
        self.Entry4.place(relx=0.291, rely=0.627,height=23, relwidth=0.594)
        self.Entry4.configure(background="white")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(font="TkFixedFont")

        self.Entry5 = tk.Entry(self.Frame1)
        self.Entry5.place(relx=0.291, rely=0.784,height=23, relwidth=0.594)
        self.Entry5.configure(background="white")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(font="TkFixedFont")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.300, rely=0.867, height=41, width=68)
        self.Button1.configure(borderwidth="6")
        self.Button1.configure(font=font12)
        self.Button1.configure(text='''Add''')
        def next_main(self):
            if self.Entry1.get()=="" or self.Entry2.get()=="" or self.Entry3.get()=="" or self.Entry4.get()=="" or self.Entry5.get()=="":
                mb.showinfo(title="Error",message="Enter valid details")
            else:
                path_to_file=pjoin("/","home","navanith","Documents","Tkinter","project1","Train_timings.txt")
                with open(path_to_file,"a+") as wr:
                    wr.write("Train_name :"+str(self.Entry1.get()+"\n")+"Train_no :"+str(self.Entry2.get()+"\n")+
                                "From :"+str(self.Entry3.get()+"\n")+"To :"+str(self.Entry4.get()+"\n")+
                                "Departure_time :"+str(self.Entry5.get()+"\n")+
                                "\n------------------------------------------------------------------------------------\n")
                    mb.showinfo(title="Confirmation",message="Train added successfully..!!")
                    self.Entry1.delete(0,"end")
                    self.Entry2.delete(0,"end")
                    self.Entry3.delete(0,"end")
                    self.Entry4.delete(0,"end")
                    self.Entry5.delete(0,"end")
                    wr.close()
        self.Button1.configure(command=lambda: next_main(self))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.600, rely=0.867, height=41, width=68)
        self.Button2.configure(borderwidth="6")
        self.Button2.configure(font=font12)
        self.Button2.configure(text='''Clear''')
        def clear(self):
            self.Entry1.delete(0,"end")
            self.Entry2.delete(0,"end")
            self.Entry3.delete(0,"end")
            self.Entry4.delete(0,"end")
            self.Entry5.delete(0,"end")
        self.Button2.configure(command=lambda: clear(self))

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.017, rely=0.022, height=101, width=99)
        photo_location = os.path.join(prog_location,"/home/navanith/Documents/Tkinter/img/icons8-train-100.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label7.configure(image=_img0)
        self.Label7.configure(text='''Label''')

if __name__ == '__main__':
    vp_start_gui()