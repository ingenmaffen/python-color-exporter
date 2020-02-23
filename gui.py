from tkinter import *
import exporter

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        color="#00ffff"
        red=0
        green=255
        blue=255

        Canvas(self, bg=color, width=100, height=100).pack(side=RIGHT, padx=10, pady=20)

        Label(self, text="Width", pady=5).pack()
        width = Entry(self)
        width.insert(0,20)
        width.pack()

        Label(self, text="Height", pady=5).pack()
        height = Entry(self)
        height.insert(0, 20)
        height.pack()

        Label(self, text="Color (hexadecimal)", pady=5).pack()
        hexa = Entry(self)
        hexa.insert(0, color)
        hexa.pack()

        Label(self, text="Color (RGB)", pady=5).pack()
        rgb = Entry(self)
        rgb.insert(0, str(red) + ',' + str(green) + ',' + str(blue))
        rgb.pack()

        Label(self, text="Filename", pady=5).pack()
        filename = Entry(self)
        filename.insert(0, 'color')
        filename.pack()
        print(filename.get())

        Button(self, text="Export", command=lambda: exporter.export(width.get(),height.get(),red,green,blue,filename.get())).pack()

root = Tk()
app = Window(root)
root.wm_title("Python color exporter")
root.mainloop()

