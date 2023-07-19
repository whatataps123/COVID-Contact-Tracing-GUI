# pseudocode
import tkinter as tk
from tkinter import *
from tkinter import ttk

def first_window():
    hide_frames()
    panel_1.pack(pady=20, padx=60, fill="both", expand=True)

def start_btn():
    hide_frames()
    panel_2.pack()

def back_window():
    hide_frames()
    panel_1.pack(pady=20, padx=60, fill="both", expand=True)

def hide_frames():
    panel_1.pack_forget()
    panel_2.pack_forget()

window = Tk()
window.title("COVID Contact Tracing")
window.geometry()

#frame of panels
panel_1 = Frame(window)

# Welcome Greetings
welcome = Label(panel_1, text = "Welcome", font=("Times New Roman", 32))
welcome.pack(pady=12, padx=10)

# Program Description
sub_head = Label(panel_1, text ="COVID Contact Tracing")
sub_head.pack(pady=12,padx=10)

# Start Button
start = Button(panel_1, text = "Start", command=start_btn) 
start.pack(pady=12, padx=10)

# Search Entry
search_title = Label(panel_1, text = "Search Name:")
search_title.pack(pady=10, padx=10)
search_entry = Entry(panel_1)
search_entry.pack(pady=10, padx=10)
search_btn = Button(panel_1, text="Search")
search_btn.pack(pady=10, padx=10)

#### Personal Information
panel_2 = Frame(window)

user_frame = LabelFrame(panel_2, text="Personal Information")
user_frame.grid(row=0, column=0, sticky="news", pady=5, padx=10)

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
address_entry.grid(row=3, columnspan=4)

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

#data privacy grid
data_privacy_frame = LabelFrame(panel_2, text="Personal Information Protection")
data_privacy_frame.grid(row=1, column=0, sticky="news", pady=5, padx=10)

#data privacy
data_privacy_label = Label(data_privacy_frame,
                            text="Data Privacy Act\nI, hereby give my consent to COVID-19 Contanct Tracing to collect, process, and\nuse my personal information for the purposes stated in this form. I understand\nthat my personal data will be treated with confidentiality and will only be\ndisclosed to third parties as necessary for the specified purposes. I acknowledge \nthat I have the right to withdraw my consent at any time. By checking the box\nbelow, I confirm that I have read and understood this Data Privacy Consent Form,\nincluding the 'Data Privacy Act of 2012' of the Republic of the Philippines, its\nImplementing Rules and Regulations (IRR), as well as all other guidelines and\nissuances by the National Privacy Commission (NPC).")
data_privacy_label.grid(row=0,column=0, sticky="news", pady=2)

#data privacy check button
data_privacy_check = Checkbutton(data_privacy_frame, text="I give my consent for my personal information.")
data_privacy_check.grid(row=1,column=0)

# Buttons Frame
buttons_frame = Frame(data_privacy_frame)
buttons_frame.grid(row=2, column=0)

# Back Button
back_button = Button(buttons_frame, text="Back", command=back_window)
back_button.pack(side=LEFT)

# Next Button
next_button = Button(buttons_frame, text="Next")
next_button.pack(side=RIGHT)

first_window()

window.mainloop()