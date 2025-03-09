import tkinter as tk
import subprocess as sub
import os

TK_SILENCE_DEPRECATION=1

repo = input("Enter the html url of the repository: \n")
cd=input("Enter thelocal working directory: \n")

os.chdir(cd)

def stage_click():
    a = []
    a.append("git")
    a.append("add")
    num=int(input("Enter the number of files you want to stage changes in: \n"))
    for i in range(0, num):
        a.append(input("Enter the file name to stage changes in: \n"))
    sub.run(a)
    print("Changes staged successfully")
def commit_click():
    a = []
    a.append("git")
    a.append("commit")
    a.append("-m")
    a.append(input("Enter the commit message: \n"))
    sub.run(a)
    print("Changes committed successfully")
def push_click():
    a = ["git", "push", repo]
    sub.run(a)
    print("Changes pushed successfully")
# Create the main window
root = tk.Tk()
root.title("Git Client")
root.geometry("400x800")

# Create a button
stage = tk.Button(root, text="Stage changes", command=stage_click)

# Change the size of the button
stage.config(width=20, height=1)

# Position the button using absolute coordinates (x=50, y=50)
stage.place(x=50, y=50)

commit = tk.Button(root, text="Commit changes", command=commit_click)
commit.config(width = 20, height=1)
commit.place(x=50, y=100)

push = tk.Button(root, text="Push changes", command=push_click)
push.config(width = 20, height=1)
push.place(x=50, y=150)
# Start the event loop
root.mainloop()
