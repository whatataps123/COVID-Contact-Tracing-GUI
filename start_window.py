# pseudocode
from tkinter import *
from info_window import InfoWindow

class StartWindow():
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
        start = Button(panel_1, text = "Start") 
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
# get information (name, age, bday, address, contact no., etc.)
# questions about covid status (vaccinated or booster?, symptoms, exposure to probable cause, in contact with someone, tested for covid?)
# submits the data and save in a file
# Add or search entry
# loop
# End