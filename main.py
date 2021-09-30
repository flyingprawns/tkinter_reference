from tkinter import *

# Create and open GUI window
window = Tk()
window.title("My first GUI program")
window.minsize(width=800, height=500)

# Label
my_label = Label(text="I'm a label!", font=("Arial", 24))
my_label.pack()


# Button
def button_click():
    my_label["text"] = user_input.get()


button = Button(text="Click me!", command=button_click)
button.pack()

# Entry
user_input = Entry(width=50)
user_input.insert(END, string="Type something here, then press the button!")
user_input.pack()

# Text
text = Text(height=5, width=50)
text.focus() # puts cursor in textbox
text.insert(END, "Enter whatever you like inside.")
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Exit GUI window
window.mainloop()
