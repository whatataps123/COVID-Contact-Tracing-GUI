import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import Toplevel
import csv
import customtkinter

class QuestionsWindow(Toplevel):
    def __init__(self, firstname, lastname, sex, age, address, contact, email, currentdate):

    # Store the personal information passed from PersonalWindow
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.age = age
        self.address = address
        self.contact = contact
        self.email = email
        self.currentdate = currentdate
        
    # Call method of parent class
        super().__init__()
        self.title("COVID Contact Tracing")
        self.geometry()
        self.panel_3 = customtkinter.CTkFrame(self)
        self.panel_3.pack()

        question_frame = LabelFrame(self.panel_3, text="Health Declaration Form",  font=customtkinter.CTkFont)
        question_frame.grid(row=0, column=0, sticky="news", pady=5, padx=10)

        # 1st Question
        question_1 = customtkinter.CTkLabel(question_frame, text="1. Tested positive or presumptively positive with COVID-19 (the new coronavirus \nor SARS-CoV-2) or been identified as a potential carrier of the coronavirus?", wraplength=0, justify=LEFT)
        question_1.grid(row=0, column=0, columnspan=2, sticky="w")

        self.question_1_response = tk.StringVar()

        question_1_yes = customtkinter.CTkRadioButton(question_frame, text="Yes", variable=self.question_1_response, value="Yes")
        question_1_yes.grid(row=1, column=0, sticky="w")
        question_1_no = customtkinter.CTkRadioButton(question_frame, text="No", variable=self.question_1_response, value="No")
        question_1_no.grid(row=1, column=1, sticky="w")

        # 2nd Question
        question_2 = customtkinter.CTkLabel(question_frame, text="2. Experienced any symptoms commonly associated with COVID-19 (fever; cough; \nfatigue or muscle pain; difficulty breathing; sore throat; lung infections; headache; \nloss of taste; or diarrhea)?", wraplength=0, justify=LEFT)
        question_2.grid(row=2, column=0, columnspan=2, sticky="w")

        self.question_2_response = tk.StringVar()

        question_2_yes = customtkinter.CTkRadioButton(question_frame, text="Yes", variable=self.question_2_response, value="Yes")
        question_2_yes.grid(row=3, column=0, sticky="w")
        question_2_no = customtkinter.CTkRadioButton(question_frame, text="No",  variable=self.question_2_response, value="No")
        question_2_no.grid(row=3, column=1, sticky="w")

        # 3rd Question
        question_3 = customtkinter.CTkLabel(question_frame, text="3. Been in any location/site declared as hazardous with and/or potentially infective \nwith the new coronavirus by a recognised health or regulatory authority?", wraplength=0, justify=LEFT)
        question_3.grid(row=4, column=0, columnspan=2, sticky="w")

        self.question_3_response = tk.StringVar()

        question_3_yes = customtkinter.CTkRadioButton(question_frame, text="Yes", variable=self.question_3_response, value="Yes")
        question_3_yes.grid(row=5, column=0, sticky="w")
        question_3_no = customtkinter.CTkRadioButton(question_frame, text="No", variable=self.question_3_response, value="No")
        question_3_no.grid(row=5, column=1, sticky="w")

        # 4th Question
        question_4 = customtkinter.CTkLabel(question_frame, text="4.Been in direct contact with or in the immediate vicinity of any person who tested \npositive with the new coronavirus or who was diagnosed as possibly being infected \nby the new coronavirus?", wraplength=0, justify=LEFT)
        question_4.grid(row=6, column=0, columnspan=2, sticky="w")

        self.question_4_response = tk.StringVar()

        question_4_yes = customtkinter.CTkRadioButton(question_frame, text="Yes", variable=self.question_4_response, value="Yes")
        question_4_yes.grid(row=7, column=0, sticky="w")
        question_4_no = customtkinter.CTkRadioButton(question_frame, text="No", variable=self.question_4_response, value="No")
        question_4_no.grid(row=7, column=1, sticky="w")


        buttons_frame_3 = Frame(self.panel_3)
        buttons_frame_3.grid(row=2,column=0)

        # Back Button
        back_button_3 = customtkinter.CTkButton(buttons_frame_3, text="Back", command=self.back_to_previous)
        back_button_3.pack(side=LEFT, pady=2,padx=2)

        # Submit Button
        submit_button = customtkinter.CTkButton(buttons_frame_3, text="Submit", command=self.submit_btn)
        submit_button.pack(side=RIGHT, pady=2, padx=2)
    
    def back_to_previous(self):
        self.withdraw()
        from personal_info import PersonalWindow
        PersonalWindow()

    def submit_btn(self):
        # Saving Responses
        response1 = self.question_1_response.get()
        response2 = self.question_2_response.get()
        response3 = self.question_3_response.get()
        response4 = self.question_4_response.get()

        if response1 and response2 and response3 and response4:
            # Save personal information and responses to CSV file
            with open("COVID Tracker.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                # Write headers only if the file is empty
                if file.tell() == 0:
                    writer.writerow(["First Name", "Last Name", "Sex", "Age", "Address", "Contact Number", "Email", "Date Today", "Response 1", "Response 2", "Response 3", "Response 4"])
                writer.writerow([self.firstname, self.lastname, self.sex, self.age, self.address, self.contact, self.email, self.currentdate, response1, response2, response3, response4])

            # Ask if the user wants to add another entry or close the application
            msg_box = messagebox.askquestion(title="Completed", message="Do you want to add another entry?", icon='info')
            if msg_box == "yes":
                self.destroy()  # Close the current QuestionsWindow
                from home_window import CovidUI
                CovidUI()  # Reopen PersonalWindow to add another entry
            else:
                msg_box_search = messagebox.askquestion(title="Completed", message="Do you want to search an entry?", icon='info')
                if msg_box_search == "yes":
                    self.destroy()  # Close the current QuestionWindow
                    from search_window import SearchWindow # Open search window to search an entry
                    SearchWindow()
                else:
                    self.destroy()
        else:
            messagebox.showwarning(title="Error.", message="Please answer all the questions.")