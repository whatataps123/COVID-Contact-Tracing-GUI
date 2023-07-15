from tkinter import *
from tkinter import ttk

panel_2 = Tk()
panel_2.title("Personal Information")
# panel_2.geometry("500x350")

#frame
frame = Frame(panel_2)
frame.pack()

# Enter Data for User
user_frame = LabelFrame(frame, text="Personal Information")
user_frame.grid(row=0, column=0, padx= 20, pady = 20)

# Enter First Name
first_name_label = Label(user_frame, text="First Name")
first_name_label.grid(row=0, column=0)
first_name_entry = Entry(user_frame)
first_name_entry.grid(row=1, column=0)

# Enter Last Name
last_name_label = Label(user_frame, text="Last Name")
last_name_label.grid(row=0,column=1)
last_name_entry = Entry(user_frame)
last_name_entry.grid(row=1, column=1)

# Biological Sex
sex_label = Label(user_frame, text="Biological Sex")
sex_label.grid(row=0, column=2)
sex_box = ttk.Combobox(user_frame, values=["Male","Female"])
sex_box.grid(row=1, column= 2)

panel_2.mainloop()