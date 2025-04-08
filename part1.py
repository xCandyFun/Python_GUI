import tkinter as tk

# create main window
root = tk.Tk()
root.title("Basic window")
root.geometry("300x350")

# Lable
label = tk.Label(root, text = "This is a label")
label.pack(pady=5)


# run the app
root.mainloop()
