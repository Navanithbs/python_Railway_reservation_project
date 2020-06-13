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

import Bookingpage_support
from tkinter import messagebox as mb
import os

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Bookingpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Bookingpage_support.init(w, top, *args, **kwargs)
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
        font19 = "-family {Noto Serif} -size 22 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font20 = "-family {DejaVu Sans} -size 11 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font21 = "-family {DejaVu Sans} -size 11 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"
        font22 = "-family {DejaVu Sans} -size 10 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font24 = "-family {DejaVu Sans} -size 9 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"

        top.geometry("680x450+341+170")
        top.title("New Booking")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.118, rely=0.067, height=51, width=509)
        self.Label1.configure(font=font19)
        self.Label1.configure(text='''Booking page''')

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.015, rely=0.222, relheight=0.5
                , relwidth=0.485)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(borderwidth="6")
        self.Labelframe1.configure(font=font21)
        self.Labelframe1.configure(text='''Train Details :''')

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.061, rely=0.133, height=22, width=109
                , bordermode='ignore')
        self.Label2.configure(font=font22)
        self.Label2.configure(text='''Train Name :''')

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.061, rely=0.267, height=21, width=98
                , bordermode='ignore')
        self.Label3.configure(font=font22)
        self.Label3.configure(text='''Train no :''')

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(relx=0.061, rely=0.4, height=21, width=93
                , bordermode='ignore')
        self.Label4.configure(font=font22)
        self.Label4.configure(text='''From :''')

        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(relx=0.061, rely=0.533, height=21, width=82
                , bordermode='ignore')
        self.Label5.configure(font=font22)
        self.Label5.configure(text='''To :''')

        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(relx=0.03, rely=0.667, height=21, width=118
                , bordermode='ignore')
        self.Label6.configure(font=font22)
        self.Label6.configure(text='''Type of seat :''')

        self.Label7 = tk.Label(self.Labelframe1)
        self.Label7.place(relx=0.03, rely=0.8, height=21, width=104
                , bordermode='ignore')
        self.Label7.configure(font=font22)
        self.Label7.configure(text='''No. of seats :''')

        self.Entry1 = tk.Entry(self.Labelframe1)
        self.Entry1.place(relx=0.424, rely=0.133, height=23, relwidth=0.503
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.424, rely=0.267, height=23, relwidth=0.503
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")

        self.Entry3 = tk.Entry(self.Labelframe1)
        self.Entry3.place(relx=0.424, rely=0.4, height=23, relwidth=0.503
                , bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")


        self.Entry4 = tk.Entry(self.Labelframe1)
        self.Entry4.place(relx=0.424, rely=0.533, height=23, relwidth=0.503
                , bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")

        self.Entry5 = tk.Entry(self.Labelframe1)
        self.Entry5.place(relx=0.424, rely=0.667, height=23, relwidth=0.503
                , bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")

        self.Entry6 = tk.Entry(self.Labelframe1)
        self.Entry6.place(relx=0.424, rely=0.8, height=23, relwidth=0.503
                , bordermode='ignore')
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")

        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.515, rely=0.222, relheight=0.5
                , relwidth=0.471)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(font=font21)
        self.Labelframe2.configure(borderwidth="6")
        self.Labelframe2.configure(text='''Customer Details :''')

        self.Label8 = tk.Label(self.Labelframe2)
        self.Label8.place(relx=0.031, rely=0.133, height=21, width=97
                , bordermode='ignore')
        self.Label8.configure(font=font22)
        self.Label8.configure(text='''Name :''')

        self.Label9 = tk.Label(self.Labelframe2)
        self.Label9.place(relx=0.031, rely=0.267, height=21, width=103
                , bordermode='ignore')
        self.Label9.configure(font=font22)
        self.Label9.configure(text='''Age :''')

        self.Label10 = tk.Label(self.Labelframe2)
        self.Label10.place(relx=0.031, rely=0.4, height=21, width=106
                , bordermode='ignore')
        self.Label10.configure(font=font22)
        self.Label10.configure(text='''Phone no :''')

        self.Label11 = tk.Label(self.Labelframe2)
        self.Label11.place(relx=0.031, rely=0.533, height=21, width=107
                , bordermode='ignore')
        self.Label11.configure(font=font22)
        self.Label11.configure(text='''Email ID :''')

        self.Label12 = tk.Label(self.Labelframe2)
        self.Label12.place(relx=0.031, rely=0.667, height=21, width=113
                , bordermode='ignore')
        self.Label12.configure(font=font22)
        self.Label12.configure(text='''Aadhar no :''')

        self.Label13 = tk.Label(self.Labelframe2)
        self.Label13.place(relx=0.031, rely=0.8, height=29, width=118
                , bordermode='ignore')
        self.Label13.configure(font=font24)
        self.Label13.configure(text='''Date of Journey :''')

        self.Entry7 = tk.Entry(self.Labelframe2)
        self.Entry7.place(relx=0.406, rely=0.133, height=23, relwidth=0.519
                , bordermode='ignore')
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")

        self.Entry8 = tk.Entry(self.Labelframe2)
        self.Entry8.place(relx=0.406, rely=0.267, height=23, relwidth=0.519
                , bordermode='ignore')
        self.Entry8.configure(background="white")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")

        self.Entry9 = tk.Entry(self.Labelframe2)
        self.Entry9.place(relx=0.406, rely=0.4, height=23, relwidth=0.519
                , bordermode='ignore')
        self.Entry9.configure(background="white")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")

        self.Entry10 = tk.Entry(self.Labelframe2)
        self.Entry10.place(relx=0.406, rely=0.533, height=23, relwidth=0.519
                , bordermode='ignore')
        self.Entry10.configure(background="white")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")

        self.Entry11 = tk.Entry(self.Labelframe2)
        self.Entry11.place(relx=0.406, rely=0.667, height=23, relwidth=0.519
                , bordermode='ignore')
        self.Entry11.configure(background="white")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")

        self.Entry12 = tk.Entry(self.Labelframe2)
        self.Entry12.place(relx=0.406, rely=0.8, height=23, relwidth=0.519
                , bordermode='ignore')
        self.Entry12.configure(background="white")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.412, rely=0.778, height=31, width=101)
        self.Button1.configure(borderwidth="5")
        self.Button1.configure(font=font20)
        self.Button1.configure(text='''submit''')
        self.count=21100

        from os.path import join as pjoin

        def writefiles(self):
                self.z=1
                flist=os.listdir('/home/navanith/Documents/files')
                for i in flist:
                        self.z=self.z+1

                name=self.Entry7.get()
                if name=="":
                        root.destroy()
                        mb.showinfo(title="Error",message="Enter valid name")
                else:
                        self.count=self.count+self.z
                        first=name+"("+str(self.count)+").txt"
                        path_to_file=pjoin("/","home","navanith","Documents","files",first)
                        with open(path_to_file,"w") as wr:
                                wr.write("Train name :"+str(self.Entry1.get()+"\n")+"Train no :"+str(self.Entry2.get()+"\n")+
                                "From :"+str(self.Entry3.get()+"\n")+"To :"+str(self.Entry4.get()+"\n")+"Type of seat :"+str(self.Entry5.get()+"\n")+"No. of seat :"+str(self.Entry6.get()+
                                "\n-----------------------------------------------------------------------\n")+"Name :"+str(self.Entry7.get()+"\n")+"Age :"+str(self.Entry8.get()+"\n")+
                                "Phone no :"+str(self.Entry9.get()+"\n")+"Email ID :"+str(self.Entry10.get()+"\n")+"Aadhar no :"+str(self.Entry11.get()+"\n")+
                                "Date of Journey :"+str(self.Entry12.get()+"\n")+"Ticket no : "+str(self.count))
                        root.destroy()
                        import paymentpage
                        paymentpage.vp_start_gui()
        self.Button1.configure(command=lambda: writefiles(self))
if __name__ == '__main__':
    vp_start_gui()