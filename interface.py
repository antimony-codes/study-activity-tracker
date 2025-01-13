import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
import interfaceOOP
import ctypes

class Window:
    def __init__(self, master):
        self.master = master
        self.master.title('Activity Tracker')
        self.notebook = ttk.Notebook(self.master, width=650, height=650)
        
        # individual frames embedded in the notebook
        frame1 = tk.Frame(self.notebook)
        frame2 = tk.Frame(self.notebook)
        frame3 = tk.Frame(self.notebook)
        frame4 = tk.Frame(self.notebook)
        frame5 = tk.Frame(self.notebook)
        
        f1 = interfaceOOP.Frame1()
        f1.add_frame1_widgets(frame1)
        
        f2 = interfaceOOP.Frame2()
        f2.add_frame2_widgets(frame2)
        
        f3 = interfaceOOP.Frame3()
        f3.add_frame3_widgets(frame3)
        
        f4 = interfaceOOP.Frame4()
        f4.add_frame4_widgets(frame4)
        
        f5 = interfaceOOP.Frame5()
        f5.add_frame5_widgets(frame5)
        
        # adding these frames to the notebook
        frame1.pack(padx=25, pady=5)    
        frame2.pack(padx=25, pady=5)
        frame3.pack(padx=25, pady=5)
        frame4.pack(padx=25, pady=5)
        frame5.pack(padx=25, pady=5)
        
        self.notebook.add(frame1, text = 'Targets')
        self.notebook.add(frame2, text = 'Progress')
        self.notebook.add(frame3, text = 'Blocking')
        self.notebook.add(frame4, text = 'To-Do')
        self.notebook.add(frame5, text = 'Pomodoro')
        
        self.notebook.pack(padx = 5, pady = 5)


ctypes.windll.shcore.SetProcessDpiAwareness(1)   
root = tk.Tk()
window = Window(root)
root.mainloop()

