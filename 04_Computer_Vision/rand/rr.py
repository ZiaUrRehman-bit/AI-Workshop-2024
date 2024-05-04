import platform
import subprocess
import tkinter as tk

# specify the desired layout and size for each window
layout = [
    {'left': 0, 'top': 0, 'width': 400, 'height': 300},
    {'left': 400, 'top': 0, 'width': 400, 'height': 300},
    {'left': 0, 'top': 300, 'width': 400, 'height': 300},
    {'left': 400, 'top': 300, 'width': 400, 'height': 300},
]

def open_windows():
    for i, pos in enumerate(layout):
        if platform.system() == 'Windows':
            command = 'cmd'
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USEPOSITION
            startupinfo.x = pos['left']
            startupinfo.y = pos['top']
            startupinfo.cx = pos['width']
            startupinfo.cy = pos['height']
        else:
            command = 'sh'
            startupinfo = None
        subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE, startupinfo=startupinfo)

# create the GUI
root = tk.Tk()
root.title("Open Windows")
root.geometry("300x100")

# create a button to open the windows
button = tk.Button(root, text="Open Windows", command=open_windows)
button.pack(pady=20)

root.mainloop()