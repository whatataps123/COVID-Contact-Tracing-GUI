# pseudocode
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import csv

GREEN1 = "#006400"   # Dark Green
GREEN2 = "#228B22"   # Forest Green
GREEN3 = "#32CD32"   # Lime Green
GREEN4 = "#00FF00"   # Green
WHITE1 = "#FFFFFF"   # White

class CovidUI(tk.Tk):

    def __init__(self):
    # Call method of parent class
        super().__init__()
        self.title("COVID Contact Tracing")
        self.geometry()
        self.config(bg=GREEN3)
        self.panel_1 = Frame(self, bg=GREEN1)

        # Welcome Greetings
        welcome = Label(self.panel_1, text = "Welcome", font=("Times New Roman", 32), bg=GREEN1, fg=WHITE1)
        welcome.pack(pady=12, padx=10)

        # Program Description
        sub_head = Label(self.panel_1, text ="COVID Contact Tracing", bg=GREEN1, fg=WHITE1)
        sub_head.pack(pady=12,padx=10)

        # Start Button
        start = Button(self.panel_1, text = "Start", command=self.start_btn, bg=GREEN2, fg=WHITE1) 
        start.pack(pady=12, padx=10)

        # Search Button
        search_button = Button(self.panel_1, text="Search", command=self.start_search_btn, bg=GREEN2, fg=WHITE1)
        search_button.pack(pady=10, padx=10)

        self.first_window()

    def first_window(self):
        self.panel_1.pack(pady=20, padx=60, fill="both", expand=True)

    def start_btn(self):
        self.withdraw()
        from personalinfo import PersonalWindow
        PersonalWindow()

    def start_search_btn(self):
        self.withdraw()
        from searchwindow import SearchWindow
        SearchWindow()
