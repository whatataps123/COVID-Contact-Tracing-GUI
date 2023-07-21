# pseudocode
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import csv

class CovidUI(tk.Tk):

    def __init__(self):
    # Call method of parent class
        super().__init__()
        self.title("COVID Contact Tracing")
        self.geometry()
        
        self.panel_1 = Frame(self)

        # Welcome Greetings
        welcome = Label(self.panel_1, text = "Welcome", font=("Times New Roman", 32))
        welcome.pack(pady=12, padx=10)

        # Program Description
        sub_head = Label(self.panel_1, text ="COVID Contact Tracing")
        sub_head.pack(pady=12,padx=10)

        # Start Button
        start = Button(self.panel_1, text = "Start", command=self.start_btn) 
        start.pack(pady=12, padx=10)

        # Search Button
        search_button = Button(self.panel_1, text="Search", command=self.start_search_btn)
        search_button.pack(pady=10, padx=10)
        
        ######################## Search Frame ######################### 

        self.search_panel = Frame(self)
        search_title = Label(self.search_panel, text = "Search Name:")
        search_title.pack(pady=10, padx=10)
        self.search_entry = Entry(self.search_panel)
        self.search_entry.pack(pady=10, padx=10)
        enter_button = Button(self.search_panel, text= "Enter", command=self.perform_search)
        enter_button.pack(pady=10,padx=10)

        self.covid_data = Listbox(self.search_panel, height=10, width=50)
        self.covid_data.pack()

        search_back_button = Frame(self.search_panel)
        search_back_button.pack()

        back_button = Button(search_back_button, text="Back", command=self.back_btn)
        back_button.pack(side=LEFT, pady=2, padx=2)

        ######################## Personal Information ######################### 

        self.panel_2 = Frame(self)

        # Created frames for Personal Information Inputs
        user_frame = LabelFrame(self.panel_2, text="Personal Information")
        user_frame.grid(row=0, column=0, sticky="news", pady=5, padx=10)

        # Enter First Name
        first_name_label = Label(user_frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        self.first_name_entry = tk.Entry(user_frame)
        self.first_name_entry.grid(row=1, column=0)

        # Enter Last Name
        last_name_label = Label(user_frame, text="Last Name")
        last_name_label.grid(row=0,column=1)
        self.last_name_entry = Entry(user_frame)
        self.last_name_entry.grid(row=1, column=1)

        # Biological Sex
        sex_label = Label(user_frame, text="Biological Sex")
        sex_label.grid(row=0, column=2)
        self.sex_box = ttk.Combobox(user_frame, values=["Male","Female"])
        self.sex_box.grid(row=1, column= 2)

        # Age
        age_label = Label(user_frame, text="Age")
        age_label.grid(row=0, column=3)
        self.age_box = ttk.Spinbox(user_frame, from_=1, to_=120, width=3)
        self.age_box.grid(row=1,column=3)

        # Enter Address
        address_label = Label(user_frame,text="Address")
        address_label.grid(row=2,columnspan=4)
        self.address_entry = Entry(user_frame)
        self.address_entry.grid(row=3, columnspan=4, sticky="news")

        # Enter Number
        contact_num_label = Label(user_frame, text="Contact Number")
        contact_num_label.grid(row=4,column=0)
        self.contact_num_entry = Entry(user_frame)
        self.contact_num_entry.grid(row=5, column=0)

        # Enter Email
        email_label = Label(user_frame, text="Email")
        email_label.grid(row=4,column=1)
        self.email_entry = Entry(user_frame)
        self.email_entry.grid(row=5,column=1)

        # Current Date
        date_label = Label(user_frame, text="Date Today")
        date_label.grid(row=4, column=2)
        self.date_entry = DateEntry(user_frame, justify=CENTER)
        self.date_entry.grid(row=5, column=2, sticky="news")

        # Padding Configuration for user_frame Widgets
        for widget in user_frame.winfo_children():
            widget.grid_configure(padx=3, pady=3)

        #data privacy grid
        data_privacy_frame = LabelFrame(self.panel_2, text="Personal Information Protection")
        data_privacy_frame.grid(row=1, column=0, sticky="news", pady=5, padx=10)

        #data privacy
        data_privacy_label = Label(data_privacy_frame,
                                    text="Data Privacy Act\nI, hereby give my consent to COVID-19 Contanct Tracing to collect, process, and\nuse my personal information for the purposes stated in this form. I understand\nthat my personal data will be treated with confidentiality and will only be\ndisclosed to third parties as necessary for the specified purposes. I acknowledge \nthat I have the right to withdraw my consent at any time. By checking the box\nbelow, I confirm that I have read and understood this Data Privacy Consent Form,\nincluding the 'Data Privacy Act of 2012' of the Republic of the Philippines, its\nImplementing Rules and Regulations (IRR), as well as all other guidelines and\nissuances by the National Privacy Commission (NPC).")
        data_privacy_label.grid(row=0,column=0, sticky="news", pady=2)

        #data privacy check button
        self.data_var = StringVar(value="Not Accepted")
        data_privacy_check = Checkbutton(data_privacy_frame, text="I give my consent for my personal information.", variable=self.data_var, onvalue="Accepted", offvalue="Not Accepted")
        data_privacy_check.grid(row=1,column=0)

        # Buttons Frame
        buttons_frame = Frame(data_privacy_frame)
        buttons_frame.grid(row=2, column=0)

        # Back Button
        back_button = Button(buttons_frame, text="Back", command=self.back_btn)
        back_button.pack(side=LEFT, pady=2, padx=2)

        # Next Button
        next_button = Button(buttons_frame, text="Next", command=self.next_btn)
        next_button.pack(side=RIGHT, pady=2, padx=2)

        ######################### Health Declaration Form ######################### 

        self.panel_3 = Frame(self)

        question_frame = LabelFrame(self.panel_3, text="Health Declaration Form")
        question_frame.grid(row=0, column=0, sticky="news", pady=5, padx=10)

        # 1st Question
        question_1 = Label(question_frame, text="1. Tested positive or presumptively positive with COVID-19 (the new coronavirus \nor SARS-CoV-2) or been identified as a potential carrier of the coronavirus?", wraplength=0, justify=LEFT)
        question_1.grid(row=0, column=0, columnspan=2, sticky="w")

        self.question_1_response = tk.StringVar()

        question_1_yes = ttk.Radiobutton(question_frame, text="Yes", variable=self.question_1_response, value="Yes")
        question_1_yes.grid(row=1, column=0, sticky="w")
        question_1_no = ttk.Radiobutton(question_frame, text="No", variable=self.question_1_response, value="No")
        question_1_no.grid(row=1, column=1, sticky="w")

        # 2nd Question
        question_2 = Label(question_frame, text="2. Experienced any symptoms commonly associated with COVID-19 (fever; cough; \nfatigue or muscle pain; difficulty breathing; sore throat; lung infections; headache; \nloss of taste; or diarrhea)?", wraplength=0, justify=LEFT)
        question_2.grid(row=2, column=0, columnspan=2, sticky="w")

        self.question_2_response = tk.StringVar()

        question_2_yes = ttk.Radiobutton(question_frame, text="Yes", variable=self.question_2_response, value="Yes")
        question_2_yes.grid(row=3, column=0, sticky="w")
        question_2_no = ttk.Radiobutton(question_frame, text="No",  variable=self.question_2_response, value="No")
        question_2_no.grid(row=3, column=1, sticky="w")

        # 3rd Question
        question_3 = Label(question_frame, text="3. Been in any location/site declared as hazardous with and/or potentially infective \nwith the new coronavirus by a recognised health or regulatory authority?", wraplength=0, justify=LEFT)
        question_3.grid(row=4, column=0, columnspan=2, sticky="w")

        self.question_3_response = tk.StringVar()

        question_3_yes = ttk.Radiobutton(question_frame, text="Yes", variable=self.question_3_response, value="Yes")
        question_3_yes.grid(row=5, column=0, sticky="w")
        question_3_no = ttk.Radiobutton(question_frame, text="No", variable=self.question_3_response, value="No")
        question_3_no.grid(row=5, column=1, sticky="w")

        # 4th Question
        question_4 = Label(question_frame, text="4.Been in direct contact with or in the immediate vicinity of any person who tested \npositive with the new coronavirus or who was diagnosed as possibly being infected \nby the new coronavirus?", wraplength=0, justify=LEFT)
        question_4.grid(row=6, column=0, columnspan=2, sticky="w")

        self.question_4_response = tk.StringVar()

        question_4_yes = ttk.Radiobutton(question_frame, text="Yes", variable=self.question_4_response, value="Yes")
        question_4_yes.grid(row=7, column=0, sticky="w")
        question_4_no = ttk.Radiobutton(question_frame, text="No", variable=self.question_4_response, value="No")
        question_4_no.grid(row=7, column=1, sticky="w")


        buttons_frame_3 = Frame(self.panel_3)
        buttons_frame_3.grid(row=2,column=0)

        # Back Button
        back_button_3 = Button(buttons_frame_3, text="Back", command=self.back_btn_2)
        back_button_3.pack(side=LEFT, pady=2,padx=2)

        # Submit Button
        submit_button = Button(buttons_frame_3, text="Submit", command=self.submit_btn)
        submit_button.pack(side=RIGHT, pady=2, padx=2)

        self.first_window()


################################################################### BUTTON FUNCTIONS ################################################################### 
    # Starting Window
    def first_window(self):
        self.hide_frames()
        self.panel_1.pack(pady=20, padx=60, fill="both", expand=True)

    # Change to Frame 2 when Start Button is clicked
    def start_btn(self):
        self.delete_input()
        self.hide_frames()
        self.panel_2.pack()
    
    # Change to Frame 1 when Back Button is clicked
    def back_btn(self):
        self.hide_frames()
        self.panel_1.pack(pady=20, padx=60, fill="both", expand=True)

    # Go to Searching Window
    def start_search_btn(self):
        self.hide_frames()
        self.search_panel.pack(pady=20, padx=60, fill="both", expand=True)

    # Change to Frame 2 when Back Button is clicked
    def back_btn_2(self):
        self.hide_frames()
        self.panel_2.pack()

    # Change to Frame 3 when Checkbox is checked and Next Button is Clicked
    def next_btn(self):
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
                self.hide_frames()
                self.panel_3.pack()
            else:
                messagebox.showwarning(title="Error", message="Please check the box if you want to proceed.")
        else:
            messagebox.showwarning(title="Error.", message="Please fill all the required fields.")

            
    # Change to Frame 2 when Back Button is clicked
    def back_btn_2(self):
        self.hide_frames()
        self.panel_2.pack()

    # Submit the Data
    def submit_btn(self):
        # Saving Responses
        response1 = self.question_1_response.get()
        response2 = self.question_2_response.get()
        response3 = self.question_3_response.get()
        response4 = self.question_4_response.get()

        if response1 and response2 and response3 and response4:
            with open("COVID Tracker.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                # Write headers only if the file is empty
                if file.tell() == 0:
                    writer.writerow(["First Name", "Last Name", "sex", "age", "address", "contact", "email", "currentdate", "Response 1", "Response 2", "Response 3", "Response 4"])
                writer.writerow([self.first_name_entry.get(), self.last_name_entry.get(), self.sex_box.get(), self.age_box.get(), self.address_entry.get(), self.contact_num_entry.get(), self.email_entry.get(), self.date_entry.get(), response1, response2, response3, response4])
            msg_box = tk.messagebox.askquestion(title="Completed", message="Do you want to add another entry?", icon='info')
            
            if msg_box == "yes":
                self.hide_frames()
                self.panel_1.pack(pady=20, padx=60, fill="both", expand=True)
            
            else:
                self.destroy()
        else:
            messagebox.showwarning(title="Error.", message="Please answer all the questions.")

    def delete_input(self):
        # Personal Information Form
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.sex_box.set("")  # Clear the combobox selection
        self.age_box.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_num_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.data_var.set("Not Accepted")

        # Health Declaration Form
        self.question_1_response.set("")  # Clear the radio button selection
        self.question_2_response.set("")
        self.question_3_response.set("")
        self.question_4_response.set("")
        
        # Function to perform the search operation
    def perform_search(self):
        search_query = self.search_entry.get()
        results = []

        with open("COVID Tracker.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            for row in reader:
                first_name, last_name = row[0], row[1]
                full_name = f"{first_name} {last_name}"
                if search_query.lower() in full_name.lower():
                    results.append(row)

        if not results:
            messagebox.showinfo("Search Results", "No matching records found.")
        else:
            self.covid_data.delete(0, END)
            for row in results:
                self.covid_data.insert(END, f"{row[0]} {row[1]}")
       
    # Implementation to hide the frames
    def hide_frames(self):
        self.panel_1.pack_forget()
        self.panel_2.pack_forget()
        self.panel_3.pack_forget()
        self.search_panel.pack_forget()
