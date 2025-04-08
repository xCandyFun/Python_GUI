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
checkBox = tk.Checkbutton(root, text="Do you want candy?")
checkBox.pack(pady=5)

#Dropdown menu
options = ["Java", "Python", "C#"]
dropdown_var = tk.StringVar(value=options[0])

Dropdown_label = tk.Label(root, text="Choose favorite language")
Dropdown_label.pack(pady=10)

dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack()

# run the app
root.mainloop()
