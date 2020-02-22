from tkinter import *
import exporter

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
app = Window(root)
root.geometry("600x400")
root.wm_title("Python color exporter")
root.mainloop()

