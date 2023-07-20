import tkinter as tk
from tkinter import Frame, Label, Button, Entry

class CovidUI(tk.Tk):
    def __init__(self):
        # Call method of the parent class
        super().__init__()
        self.title("COVID Contact Tracing")
        self.geometry("400x300")  # Set an appropriate size for the window

        self.create_widgets()

    def start_btn(self):
        # Define the function that will be called when the Start button is clicked
        print("Start button clicked!")

    def create_widgets(self):
        panel_1 = Frame(self)

        # Welcome Greetings
        welcome = Label(panel_1, text="Welcome", font=("Times New Roman", 32))
        welcome.pack(pady=12, padx=10)

        # Program Description
        sub_head = Label(panel_1, text="COVID Contact Tracing")
        sub_head.pack(pady=12, padx=10)

        # Start Button
        start = Button(panel_1, text="Start", command=self.start_btn)  # Use self.start_btn as the command
        start.pack(pady=12, padx=10)

        # Search Entry
        search_title = Label(panel_1, text="Search Name:")
        search_title.pack(pady=10, padx=10)
        search_entry = Entry(panel_1)
        search_entry.pack(pady=10, padx=10)
        search_btn = Button(panel_1, text="Search")
        search_btn.pack(pady=10, padx=10)

        panel_1.pack()

if __name__ == "__main__":
    app = CovidUI()
    app.mainloop()
