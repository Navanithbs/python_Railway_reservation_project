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

import TrainTimings_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    TrainTimings_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    TrainTimings_support.init(w, top, *args, **kwargs)
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

        top.geometry("600x450+367+170")
        top.title("Trains & Timings")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.2, rely=0.067, height=71, width=369)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font="-family {Noto Serif Display} -size 22 -weight bold -slant italic")
        self.Label1.configure(text='''Trains & Timings''')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.083, rely=0.2, relheight=0.698, relwidth=0.843)
        self.Text1.configure(background="white")
        self.Text1.configure(foreground="#000000")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(wrap="word")
        with open("Train_timings.txt","r") as wr:
            flist=wr.readlines()
            self.Text1.insert(tk.END,flist)
        wr.close()

if __name__ == '__main__':
    vp_start_gui()