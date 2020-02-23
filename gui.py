from tkinter import *
import exporter
root = Tk()
root.wm_title("Python color exporter")

color = "#00ffff"
red = 0
green = 255
blue = 255

hexaColor = StringVar()
hexaColor.set(color)
rgbColor = StringVar()
rgbColor.set(str(red) + ',' + str(green) + ',' + str(blue))

# canvas = Canvas(root, bg=color, width=100, height=100).pack(side=RIGHT, padx=10, pady=20)

def hexatorgb(*args):
    hexOrder = '0123456789abcdef'
    hexValue = hexaColor.get()

    if not(hexValue[0] == '#' and len(hexValue) < 7):
        global red
        red = 16 * hexOrder.index(hexValue[1]) + hexOrder.index(hexValue[2])
        global green
        green = 16 * hexOrder.index(hexValue[3]) + hexOrder.index(hexValue[4])
        global blue
        blue = 16 * hexOrder.index(hexValue[5]) + hexOrder.index(hexValue[6])
        # rgbColor.set(str(red) + ',' + str(green) + ',' + str(blue))

# def rgbtohexa(*args):
#    print(rgbColor.get())


Label(root, text="Width", pady=5).pack()
width = Entry(root)
width.insert(0,20)
width.pack()

Label(root, text="Height", pady=5).pack()
height = Entry(root)
height.insert(0, 20)
height.pack()

Label(root, text="Color (hexadecimal)", pady=5).pack()
hexa = Entry(root, textvariable=hexaColor).pack()
hexaColor.trace("w", hexatorgb)

# Label(root, text="Color (RGB)", pady=5).pack()
# rgb = Entry(root, textvariable=rgbColor).pack()
# rgbColor.trace("w", rgbtohexa)

Label(root, text="Filename", pady=5).pack()
filename = Entry(root)
filename.insert(0, 'color')
filename.pack()

Button(root, text="Export", command=lambda: exporter.export(int(width.get()), int(height.get()), red, green, blue, filename.get())).pack()

root.mainloop()