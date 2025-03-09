import tkinter as tk
TK_SILENCE_DEPRECATION=1

def on_button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Place Position and Size")
root.geometry("300x200")

# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)

# Change the size of the button
button.config(width=20, height=2)

# Position the button using absolute coordinates (x=50, y=50)
button.place(x=50, y=50)

# Start the event loop
root.mainloop()
