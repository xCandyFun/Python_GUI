import tkinter as tk

# create main window
root = tk.Tk()
root.title("Basic window")
root.geometry("300x350")

# Lable
label = tk.Label(root, text = "This is a label")
label.pack(pady=5)

# Entry box
entry = tk.Entry()
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Click me")
button.pack(pady=5)

#Radio buttons
radio1 = tk.Radiobutton(root, text="Option 1", value=1)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Option 2", value=2)
radio2.pack()

#Check box
checkBox = tk.Checkbutton(root, text="do you want candy?")
checkBox.pack(pady=5)

# run the app
root.mainloop()
