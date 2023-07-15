from tkinter import *
from info_window import InfoWindow

class StartWindow(InfoWindow):
    def __init__(self):
        window = Tk()
        window.title("COVID Contact Tracing")
        window.geometry("500x350")

        #frame of panels
        panel_1 = Frame(window)
        panel_1.pack(pady=20, padx=60, fill="both", expand=True )

        # panel 1

        # Welcome Greetings
        welcome = Label(panel_1, text = "Welcome", font=("Times New Roman", 32))
        welcome.pack(pady=12, padx=10)

        # Program Description
        sub_head = Label(panel_1, text ="COVID Contact Tracing")
        sub_head.pack(pady=12,padx=10)

        # Start Button
        start = Button(panel_1, text = "Start", command=self.change_to_info) 
        start.pack(pady=12, padx=10)

        # Search Entry
        search_title = Label(panel_1, text = "Search Name:")
        search_title.pack(pady=10, padx=10)
        search_entry = Entry(panel_1)
        search_entry.pack(pady=10, padx=10)
        search_btn = Button(panel_1, text="Search")
        search_btn.pack(pady=10, padx=10)

        window.mainloop()
StartWindow()

from tkinter import ttk

class InfoWindow():
    def change_to_info(self):
        panel_2 = Tk()
        panel_2.title("Personal Information")
        # panel_2.geometry("500x350")

        #frame
        frame = Frame(panel_2)
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


        panel_2.mainloop()

InfoWindow()