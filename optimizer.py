import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
# Keep window active above all other windows.
# root.attributes('-topmost', True)
root.geometry('450x300')


# root.withdraw()

# def select():
#     file_path = filedialog.askopenfilename()
#     label = tk.Label(root, text = file_path)
#     label.pack()

def selectFile():
        file_path = filedialog.askopenfilename()
        optimizeFile(file_path)


def selectFolder():
        folder_path = filedialog.askdirectory()
        optimizeFolder(folder_path)


def openFileDialogue():
    global button3, button4
    try:
        button3.destroy()
        button4.destroy()
        scale.destroy()
    except:
        pass
    button3 = tk.Button(root, text = 'Select File', command = selectFile)
    button3.pack()
    

def openFolderDialogue():
    global button3, button4
    try:
        button3.destroy()
        button4.destroy()
        scale.destroy()
    except:
        pass
    button4 = tk.Button(root, text='Select Folder', command = selectFolder)
    button4.pack()


def check(value = None):
    global scale_label
    print(v1.get())
    val = v1.get()/100
    scale_label = tk.Label(root, text =str(val))
    # scale_label.destroy()
    update_values()


def optimizeFile(path):
    global scale
    try:
        scale.destroy()
    except:
        pass
    scale = tk.Scale( root, variable = v1, from_ = 100, to = 1, orient = tk.HORIZONTAL, command = check)
    scale.set(20)
    scale.pack()


def optimizeFolder(path):
    pass


v1 = tk.DoubleVar()
scale_factor = tk.DoubleVar()

button3 = tk.Button(root, text = 'Select File', command = selectFile)
button4 = tk.Button(root, text='Select Folder', command = selectFolder)
scale = tk.Scale( root, variable = v1, from_ = 1, to = 100, orient = tk.HORIZONTAL, command = check)

message = tk.Label(root, text='Select image file')
message.pack()
button1 = tk.Button(root, text='1-Image', command=openFileDialogue)
button1.pack()
button2 = tk.Button(root, text='bulk-Image', command=openFolderDialogue)
button2.pack()
# label = tk.Label(root, text = file_path)
root.mainloop()