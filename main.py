from tkinter import *

# Create and open GUI window
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I'm a label!", font=("Arial", 24))
my_label.grid(column=3, row=1)


# Button
def button_click():
    my_label["text"] = user_input.get()


button = Button(text="Click me!", command=button_click)
button.grid(column=3, row=2)

# Entry
user_input = Entry(width=50)
user_input.insert(END, string="Type something here, then press the button!")
user_input.grid(column=3, row=3)

# Text
text = Text(height=5, width=50)
text.focus() # puts cursor in textbox
text.insert(END, "Enter whatever you like inside.")
text.grid(column=3, row=4)


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=1, row=2)


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=1, row=4)


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.grid(column=5, row=1)


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=5, row=3)
radiobutton2.grid(column=5, row=4)


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# listbox.place(x=335, y=410)
listbox.grid(column=3, row=5)

# Image example : tomato image with "timer" text, taken from one of my projects
tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=240, height=264, bg=YELLOW, highlightthickness=0)
canvas.create_image(119, 132, image=tomato_image)
timer_text = canvas.create_text(119, 152, text="0:00", fill="white", font=(FONT_NAME_TIMER, 35, "bold"))
canvas.grid(row=2, column=2)

# Exit GUI window
window.mainloop()
