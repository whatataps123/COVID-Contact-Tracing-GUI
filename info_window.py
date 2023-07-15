from tkinter import *
from tkinter import ttk

class InfoWindow():
    def __init__(self):
        self.panel_2 = Tk()
        self.panel_2.title("Personal Information")
        self.panel_2.geometry("500x350")
        self.create_info_window()
        
        #frame
    def create_info_window(self):
        frame = Frame(self.panel_2)
        frame.pack()

        ### PERSONAL INFORMATION
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

        # Age
        age_label = Label(user_frame, text="Age")
        age_label.grid(row=0, column=3)
        age_box = ttk.Spinbox(user_frame, from_=1, to_=120, width=3)
        age_box.grid(row=1,column=3)

        # Enter Address
        address_label = Label(user_frame,text="Address")
        address_label.grid(row=2,columnspan=4)
        address_entry = Entry(user_frame, width=71)
        address_entry.grid(row=3, columnspan=10)

        # Enter Number
        contact_num_label = Label(user_frame, text="Contact Number")
        contact_num_label.grid(row=4,column=0)
        contact_num_entry = Entry(user_frame)
        contact_num_entry.grid(row=5, column=0)

        # Enter Email
        email_label = Label(user_frame, text="Email")
        email_label.grid(row=4,column=1)
        email_label_entry = Entry(user_frame)
        email_label_entry.grid(row=5,column=1)
    def run(self):
        self.panel_2.mainloop()

InfoWindow().run()