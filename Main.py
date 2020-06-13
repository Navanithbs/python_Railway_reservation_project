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

import Main_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Railways (root)
    Main_support.init(root, top)
    root.mainloop()


w = None
def create_Railways(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Railways (w)
    Info_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Railways():
    global w
    w.destroy()
    w = None
def time():
    import TrainTimings
    TrainTimings.vp_start_gui()

def info():
    import Bookinginfo
    Bookinginfo.vp_start_gui()

def cancellation():
    import Cancellationpage
    Cancellationpage.vp_start_gui()

def newBook():
    import Bookingpage
    #root.destroy()
    Bookingpage.vp_start_gui()

class Railways:
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
        font14 = "-family Yrsa -size 22 -weight bold -slant italic "  \
            "-underline 1 -overstrike 0"

        top.geometry("600x450+441+187")
        top.title("Railways")
        top.configure(background="#605F5F")

        self.infoBtn = tk.Button(top)
        self.infoBtn.place(relx=0.017, rely=0.222, height=111, width=261)
        self.infoBtn.configure(activebackground="#f9f9f9")
        self.infoBtn.configure(activeforeground="white")
        photo_location = os.path.join(prog_location,"/home/navanith/Documents/Tkinter/img/icons8-contact-info-96.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.infoBtn.configure(image=_img0)
        self.infoBtn.configure(borderwidth="4")
        self.infoBtn.configure(command=info)


        self.TrainTime = tk.Button(top)
        self.TrainTime.place(relx=0.567, rely=0.222, height=111, width=231)
        self.TrainTime.configure(activebackground="#f9f9f9")
        self.TrainTime.configure(activeforeground="white")
        self.TrainTime.configure(borderwidth="4")
        photo_location = os.path.join(prog_location,"/home/navanith/Documents/Tkinter/img/icons8-time-100.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.TrainTime.configure(image=_img1)
        self.TrainTime.configure(command=time)

        self.BC = tk.Button(top)
        self.BC.place(relx=0.567, rely=0.533, height=131, width=231)
        self.BC.configure(activebackground="#f9f9f9")
        self.BC.configure(activeforeground="white")
        photo_location = os.path.join(prog_location,"/home/navanith/Documents/Tkinter/img/icons8-cancel-subscription-96.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.BC.configure(image=_img2)
        self.BC.configure(borderwidth="4")
        self.BC.configure(command=cancellation)

        self.NB = tk.Button(top)
        self.NB.place(relx=0.017, rely=0.556, height=121, width=261)
        self.NB.configure(activebackground="#f9f9f9")
        photo_location = os.path.join(prog_location,"/home/navanith/Documents/Tkinter/img/icons8-train-100.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.NB.configure(image=_img3)
        self.NB.configure(borderwidth="4")
        self.NB.configure(command=newBook)

        self.Label1_8 = tk.Label(top)
        self.Label1_8.place(relx=0.017, rely=0.467, height=21, width=259)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(font=font10)
        self.Label1_8.configure(text='''Booking Information''')

        self.Label1_9 = tk.Label(top)
        self.Label1_9.place(relx=0.567, rely=0.467, height=21, width=229)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(font=font10)
        self.Label1_9.configure(text='''Trains & Timings''')

        self.Label1_10 = tk.Label(top)
        self.Label1_10.place(relx=0.567, rely=0.822, height=21, width=229)
        self.Label1_10.configure(activebackground="#f9f9f9")
        self.Label1_10.configure(font=font10)
        self.Label1_10.configure(text='''Cancellation''')

        self.Label1_11 = tk.Label(top)
        self.Label1_11.place(relx=0.017, rely=0.822, height=21, width=259)
        self.Label1_11.configure(activebackground="#f9f9f9")
        self.Label1_11.configure(font=font10)
        self.Label1_11.configure(text='''New Booking''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.0, rely=0.022, height=61, width=599)
        self.Label2.configure(font=font14)
        self.Label2.configure(text='''Railway Reservation System''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()
