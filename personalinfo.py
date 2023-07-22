# pseudocode
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import Toplevel
from tkinter.font import Font
import customtkinter

GREEN1 = "#006400"   # Dark Green
GREEN2 = "#228B22"   # Forest Green
GREEN3 = "#32CD32"   # Lime Green
GREEN4 = "#00FF00"   # Green
WHITE1 = "#FFFFFF"   # White

class PersonalWindow(Toplevel):
    def __init__(self):
    # Call method of parent class
        super().__init__()
        self.title("COVID Contact Tracing")
        self.geometry()

        #self.config(bg=)

        self.panel_2 = customtkinter.CTkFrame(self)
        self.panel_2.pack()
        # Created frames for Personal Information Inputs
        user_frame = LabelFrame(self.panel_2, text="Personal Information", font=customtkinter.CTkFont)
        user_frame.grid(row=0, column=0, sticky="news", pady=5, padx=10)

        # Enter First Name
        first_name_label = customtkinter.CTkLabel(user_frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        self.first_name_entry = customtkinter.CTkEntry(user_frame, placeholder_text="Enter firstname")
        self.first_name_entry.grid(row=1, column=0)

        # Enter Last Name
        last_name_label = customtkinter.CTkLabel(user_frame, text="Last Name")
        last_name_label.grid(row=0,column=1)
        self.last_name_entry = customtkinter.CTkEntry(user_frame, placeholder_text="Enter lastname")
        self.last_name_entry.grid(row=1, column=1)

        # Biological Sex
        sex_label = customtkinter.CTkLabel(user_frame, text="Biological Sex")
        sex_label.grid(row=0, column=2)
        self.sex_box = customtkinter.CTkComboBox(user_frame, values=["","Male","Female"])
        self.sex_box.grid(row=1, column= 2)

        # Age
        age_label = customtkinter.CTkLabel(user_frame, text="Age")
        age_label.grid(row=0, column=3)
        font_roboto = ("Roboto", 13)
        self.age_box = ttk.Spinbox(user_frame, from_=1, to_=120, width=3, font=font_roboto)
        self.age_box.grid(row=1,column=3)

        # Enter Address
        address_label = customtkinter.CTkLabel(user_frame,text="Address")
        address_label.grid(row=2,columnspan=4)
        self.address_entry = customtkinter.CTkEntry(user_frame, placeholder_text="Enter complete address")
        self.address_entry.grid(row=3, columnspan=4, sticky="news")

        # Enter Number
        contact_num_label = customtkinter.CTkLabel(user_frame, text="Contact Number")
        contact_num_label.grid(row=4,column=0)
        self.contact_num_entry = customtkinter.CTkEntry(user_frame, placeholder_text="Enter contact number")
        self.contact_num_entry.grid(row=5, column=0)

        # Enter Email
        email_label = customtkinter.CTkLabel(user_frame, text="Email")
        email_label.grid(row=4,column=1)
        self.email_entry = customtkinter.CTkEntry(user_frame, placeholder_text="Enter email")
        self.email_entry.grid(row=5,column=1)

        # Current Date
        date_label = customtkinter.CTkLabel(user_frame, text="Date Today")
        date_label.grid(row=4, column=2)
        font_roboto = ("Roboto", 13)
        self.date_entry = DateEntry(user_frame, justify=CENTER, font=font_roboto)
        self.date_entry.grid(row=5, column=2, sticky="news")

        # Padding Configuration for user_frame Widgets
        for widget in user_frame.winfo_children():
            widget.grid_configure(padx=3, pady=3)

        #data privacy grid
        data_privacy_frame = LabelFrame(self.panel_2, text="Personal Information Protection", font=customtkinter.CTkFont)
        data_privacy_frame.grid(row=1, column=0, sticky="news", pady=5, padx=10)

        #data privacy
        data_privacy_label = customtkinter.CTkLabel(data_privacy_frame,
                                    text="Data Privacy Act\nI, hereby give my consent to COVID-19 Contanct Tracing to collect, process, and\nuse my personal information for the purposes stated in this form. I understand\nthat my personal data will be treated with confidentiality and will only be\ndisclosed to third parties as necessary for the specified purposes. I acknowledge \nthat I have the right to withdraw my consent at any time. By checking the box\nbelow, I confirm that I have read and understood this Data Privacy Consent Form,\nincluding the 'Data Privacy Act of 2012' of the Republic of the Philippines, its\nImplementing Rules and Regulations (IRR), as well as all other guidelines and\nissuances by the National Privacy Commission (NPC).")
        data_privacy_label.grid(row=0,column=0, sticky="news", pady=2)

        #data privacy check button
        self.data_var = StringVar(value="Not Accepted")
        data_privacy_check = customtkinter.CTkCheckBox(data_privacy_frame, text="I give my consent for my personal information.", variable=self.data_var, onvalue="Accepted", offvalue="Not Accepted")
        data_privacy_check.grid(row=1,column=0)

        # Buttons Frame
        buttons_frame = customtkinter.CTkFrame(data_privacy_frame)
        buttons_frame.grid(row=2, column=0)

        # Back Button
        back_button = customtkinter.CTkButton(buttons_frame, text="Back", command=self.back_to_main_event)
        back_button.pack(side=LEFT, pady=2, padx=2)

        # Next Button
        next_button = customtkinter.CTkButton(buttons_frame, text="Next", command=self.next_event)
        next_button.pack(side=RIGHT, pady=2, padx=2)

    def back_to_main_event(self):
        self.withdraw()
        self.master.deiconify()  # Show the main window again

    def next_event(self):
        # Saving Personal Info
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        sex = self.sex_box.get()
        age = self.age_box.get()
        address = self.address_entry.get()
        contact = self.contact_num_entry.get()
        email = self.email_entry.get()
        currentdate = self.date_entry.get()
        if firstname and lastname and sex and age and address and contact and email and currentdate:
            data_check = self.data_var.get()  
            if data_check == "Accepted":
                self.withdraw()
                from questionswindow import QuestionsWindow
                QuestionsWindow(firstname, lastname, sex, age, address, contact, email, currentdate)
            else:
                messagebox.showwarning(title="Error", message="Please check the box if you want to proceed")
        else:
            messagebox.showwarning(title="Error.", message="Please fill all the required fields.")

            