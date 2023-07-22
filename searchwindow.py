# pseudocode
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from tkinter import Toplevel

GREEN1 = "#006400"   # Dark Green
GREEN2 = "#228B22"   # Forest Green
GREEN3 = "#32CD32"   # Lime Green
GREEN4 = "#00FF00"   # Green
WHITE1 = "#FFFFFF"   # White

class SearchWindow(Toplevel):
    def __init__(self):
    # Call method of parent class
        super().__init__()
        self.title("COVID Contact Tracing")
        self.geometry()
        #self.config(bg=)

        self.search_panel = Frame(self, bg=GREEN1)
        self.search_panel.pack()
        search_title = Label(self.search_panel, text = "Search Name or Date:", bg=GREEN1, fg=WHITE1)
        search_title.pack(pady=10, padx=10)

        # Where the user will enter date or name to search
        self.search_entry = Entry(self.search_panel, bg=WHITE1, fg="black")
        self.search_entry.pack(anchor=CENTER,pady=10, padx=10)

        # Enter Button to Search
        enter_button = Button(self.search_panel, text= "Enter", command=self.perform_search,  bg=GREEN2, fg=WHITE1)
        enter_button.pack(pady=10,padx=10)
        # ScrollBar
        scroll_bar = Scrollbar(self.search_panel)
        scroll_bar.pack(side=RIGHT, fill= Y)
        
        # ListBox of Entries
        self.covid_data = Listbox(self.search_panel, yscrollcommand= scroll_bar.set, height=10, width=50, bg=WHITE1, fg="black")
        self.show_all_data()
        self.covid_data.pack(pady=5,padx=5,expand=TRUE, fill=BOTH)

        scroll_bar.config(command= self.covid_data.yview)
        
        #Back Button in Search Panel
        back_button = Button(self.search_panel, text="Back", command=self.back_to_main)
        back_button.pack(anchor=CENTER, pady=2, padx=2)

    def back_to_main(self):
        self.withdraw()
        self.master.deiconify()

    def perform_search(self):
        search_query = self.search_entry.get()
        results = []

        with open("COVID Tracker.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            for row in reader:
                first_name, last_name, date = row[0], row[1], row[7]
                full_name = f"{first_name} {last_name}"
                if search_query in full_name.lower() or search_query in date.lower():
                    results.append((full_name, date))

        if not results:
            messagebox.showinfo("Search Results", "No matching records found.")
        else:
            self.covid_data.delete(0, END)
            for row in results:
                self.covid_data.insert(END, f"{row[0]} {row[1]}")
                
    def read_csv_data(self, filename):
        data = []
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            for row in reader:
                data.append(row)
        return data

    def show_all_data(self):
        data = self.read_csv_data("COVID Tracker.csv")
        self.covid_data.delete(0, END)
        for row in data:
            self.covid_data.insert(END, f"{row[0]} {row[1]} {row[7]}")