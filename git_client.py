import tkinter as tk
import subprocess as sub
import os

TK_SILENCE_DEPRECATION=1

repo = input("Enter the html url of the repository: \n")
cd=input("Enter thelocal working directory: \n")

def stage_click():
    a = []
    a.append("git")
    a.append("add")
    num=int(input("Enter the number of files you want to stage changes in: \n"))
    for i in range(0, num):
        a.append(input("Enter the file name to stage changes in: \n"))
    sub.run(a, cwd=cd)
    print("Changes staged successfully")

# Create the main window
root = tk.Tk()
root.title("Git Client")
root.geometry("300x200")

# Create a button
stage = tk.Button(root, text="Stage changes", command=stage_click)

# Change the size of the button
stage.config(width=20, height=1)

# Position the button using absolute coordinates (x=50, y=50)
stage.place(x=50, y=50)

# Start the event loop
root.mainloop()
