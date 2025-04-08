import tkinter as tk
from tkinter import messagebox

def on_sumbit():
    name = entry.get()
    selected_gender = gender_var.get()
    subscribed = subscribe_var.get()
    language = language_var.get()

    info = f"Name: {name}\nGender: {selected_gender}\nSubscribed: {subscribed}\nLanguage: {language}"
    messagebox.showinfo("SumbitInfo", info)


root = tk.Tk()
root.title("test")
root.geometry("350x350")

labelName = tk.Label(root, text="Name:")
labelName.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

label_gender = tk.Label(root, text="Gender:")
label_gender.pack(pady=5)

gender_var = tk.StringVar(value="other")
radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio_male.pack()

radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio_female.pack()

radio_other = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other")
radio_other.pack()

subscribe_var = tk.BooleanVar()

checkBox = tk.Checkbutton(root, text="Subscribe", variable=subscribe_var)
checkBox.pack(pady=5)

label_language = tk.Label(root, text="Fav lang:")
label_language.pack(pady=5)

languages = ["python", "java", "c++", "c#"]
language_var = tk.StringVar(value=languages[1])

dropdown = tk.OptionMenu(root, language_var, *languages)
dropdown.pack()

sumit_button = tk.Button(root, text="Submit", command=on_sumbit)
sumit_button.pack(pady=20)

root.mainloop()