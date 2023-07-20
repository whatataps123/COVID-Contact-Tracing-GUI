# pseudocode
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

def first_window():
    hide_frames()
    panel_1.pack(pady=20, padx=60, fill="both", expand=True)

def start_btn():
    hide_frames()
    panel_2.pack()

def back_btn():
    hide_frames()
    panel_1.pack(pady=20, padx=60, fill="both", expand=True)

def next_btn():
    data_check = data_var.get()  
    if data_check == "Accepted":
        hide_frames()
        panel_3.pack()
    else:
        messagebox.showwarning(title="Error",message="Please check the box if you want to proceed.")

def hide_frames():
    panel_1.pack_forget()
    panel_2.pack_forget()
    panel_3.pack_forget()

window = Tk()
window.title("COVID Contact Tracing")
window.geometry("")

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

######################### Personal Information ######################### 

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

# Current Date
date_label = Label(user_frame, text="Date Today")
date_label.grid(row=4, column=2)
date_entry = DateEntry(user_frame, justify=CENTER)
date_entry.grid(row=5, column=2, sticky="news")

#data privacy grid
data_privacy_frame = LabelFrame(panel_2, text="Personal Information Protection")
data_privacy_frame.grid(row=1, column=0, sticky="news", pady=5, padx=10)

#data privacy
data_privacy_label = Label(data_privacy_frame,
                            text="Data Privacy Act\nI, hereby give my consent to COVID-19 Contanct Tracing to collect, process, and\nuse my personal information for the purposes stated in this form. I understand\nthat my personal data will be treated with confidentiality and will only be\ndisclosed to third parties as necessary for the specified purposes. I acknowledge \nthat I have the right to withdraw my consent at any time. By checking the box\nbelow, I confirm that I have read and understood this Data Privacy Consent Form,\nincluding the 'Data Privacy Act of 2012' of the Republic of the Philippines, its\nImplementing Rules and Regulations (IRR), as well as all other guidelines and\nissuances by the National Privacy Commission (NPC).")
data_privacy_label.grid(row=0,column=0, sticky="news", pady=2)

#data privacy check button
data_var = StringVar(value="Not Accepted")
data_privacy_check = Checkbutton(data_privacy_frame, text="I give my consent for my personal information.", variable=data_var, onvalue="Accepted", offvalue="Not Accepted")
data_privacy_check.grid(row=1,column=0)

# Buttons Frame
buttons_frame = Frame(data_privacy_frame)
buttons_frame.grid(row=2, column=0)

# Back Button
back_button = Button(buttons_frame, text="Back", command=back_btn)
back_button.pack(side=LEFT)

# Next Button
next_button = Button(buttons_frame, text="Next", command=next_btn)
next_button.pack(side=RIGHT)

######################### Health Declaration Form ######################### 

panel_3 = Frame(window)

question_frame = LabelFrame(panel_3, text="Health Declaration Form")
question_frame.grid(row=0, column=0, sticky="news", pady=5, padx=10)

# 1st Question
question_1 = Label(question_frame, text="1. Tested positive or presumptively positive with COVID-19 (the new coronavirus \nor SARS-CoV-2) or been identified as a potential carrier of the coronavirus?", wraplength=0, justify=LEFT)
question_1.grid(row=0, column=0, columnspan=2, sticky="w")
question_1_yes = Radiobutton(question_frame, text="Yes")
question_1_yes.grid(row=1, column=0, sticky="w")
question_1_no = Radiobutton(question_frame, text="No")
question_1_no.grid(row=1, column=1, sticky="w")

# 2nd Question
question_2 = Label(question_frame, text="2. Experienced any symptoms commonly associated with COVID-19 (fever; cough; \nfatigue or muscle pain; difficulty breathing; sore throat; lung infections; headache; \nloss of taste; or diarrhea)?", wraplength=0, justify=LEFT)
question_2.grid(row=2, column=0, columnspan=2, sticky="w")
question_2_yes = Radiobutton(question_frame, text="Yes")
question_2_yes.grid(row=3, column=0, sticky="w")
question_2_no = Radiobutton(question_frame, text="No")
question_2_no.grid(row=3, column=1, sticky="w")

# 3rd Question
question_3 = Label(question_frame, text="3. Been in any location/site declared as hazardous with and/or potentially infective \nwith the new coronavirus by a recognised health or regulatory authority?", wraplength=0, justify=LEFT)
question_3.grid(row=4, column=0, columnspan=2, sticky="w")
question_3_yes = Radiobutton(question_frame, text="Yes")
question_3_yes.grid(row=5, column=0, sticky="w")
question_3_no = Radiobutton(question_frame, text="No")
question_3_no.grid(row=5, column=1, sticky="w")

# 4th Question
question_4 = Label(question_frame, text="4.Been in direct contact with or in the immediate vicinity of any person who tested \npositive with the new coronavirus or who was diagnosed as possibly being infected \nby the new coronavirus?", wraplength=0, justify=LEFT)
question_4.grid(row=6, column=0, columnspan=2, sticky="w")
question_4_yes = Radiobutton(question_frame, text="Yes")
question_4_yes.grid(row=7, column=0, sticky="w")
question_4_no = Radiobutton(question_frame, text="No")
question_4_no.grid(row=7, column=1, sticky="w")
first_window()

window.mainloop()