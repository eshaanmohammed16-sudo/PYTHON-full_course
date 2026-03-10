from tkinter import *
from tkinter import ttk

def savePosn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    if mixLineStatus:
        canvas.create_line(lastx, event.y, event.x, lasty, fill=lineColour, width=brushSize.get(), capstyle=ROUND)
    elif eraseStatus:
        canvas.create_line(lastx, lasty, event.x, event.y, fill='white', width=brushSize.get(), capstyle=ROUND)
        savePosn(event)
    else:
        canvas.create_line(lastx, lasty, event.x, event.y, fill=lineColour, width=brushSize.get(), capstyle=ROUND)
        savePosn(event)

def brushSelect(event=None):
    global eraseStatus, mixLineStatus
    eraseStatus = False
    mixLineStatus = False
    if typeMenu.get() == 'Spiro':
        mixLineStatus = True
    elif typeMenu.get() == 'Eraser':
        eraseStatus = True

def clear():
    canvas.delete("all")

def colourChange(colour):
    global lineColour
    lineColour = colour

root = Tk()
root.title("Draw")
root.geometry("800x500")
root.configure(bg='white')

lineColour = 'black'
mixLineStatus = False
eraseStatus = False

# Brush size control
brushSize = IntVar(value=2)
ttk.Label(root, text="Brush Size:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
sizeMenu = ttk.Combobox(root, textvariable=brushSize, values=[1, 2, 3, 4, 5], width=5) #,state='readonly')
sizeMenu.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# Brush type control
brushType = StringVar(value='Default')
ttk.Label(root, text="Brush Type:").grid(row=4, column=0, padx=5, pady=5, sticky='w')
typeMenu = ttk.Combobox(root, textvariable=brushType, values=['Default', 'Spiro', 'Eraser'], width=10, state='readonly')
typeMenu.grid(row=4, column=1, padx=5, pady=5, sticky='w')
typeMenu.bind("<<ComboboxSelected>>", brushSelect)

# Clear button
ttk.Button(root, text='Clear', command=clear).grid(row=6, column=1, pady=(10, 10))

# Colour selection
ttk.Label(root, text="Colours:").grid(row=0, column=0, columnspan=3, pady=(10, 0), sticky='w')
colourFrame = Frame(root)
colourFrame.grid(row=1, column=0, columnspan=3, pady=5, sticky='w')

for colour in ['black', 'red', 'blue',]:
    Button(colourFrame, bg=colour, width=4, height=2, command=lambda c=colour: colourChange(c)).pack(side=LEFT, padx=2)

# Canvas
canvas = Canvas(root, bg='white', bd=2, relief='sunken')
canvas.grid(row=0, column=3, rowspan=10, columnspan=7, sticky='nsew', padx=10, pady=10)
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

# Grid weight for resizing
for i in range(10):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

root.mainloop()
print("shush")