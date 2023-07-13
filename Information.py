# pseudocode
from tkinter import *

# Panel 1
panel_1 = Tk()
panel_1.title("COVID Contact Tracing")
panel_1.geometry("500x350")

# Welcome Greetings
welcome = Label(panel_1, text = "Welcome")
welcome.pack(pady=12, padx=10)

# Start Button
start = Button(panel_1, text = "Start") 
start.pack(pady=12, padx=10)

# Search Entry
search_title = Label(panel_1, text = "Search Name:")
search_title.pack(pady=12, padx=10)
search_entry = Entry(panel_1)
search_entry.pack(pady=12, padx=10)
panel_1.mainloop()
# get information (name, age, bday, address, contact no., etc.)
# questions about covid status (vaccinated or booster?, symptoms, exposure to probable cause, in contact with someone, tested for covid?)
# submits the data and save in a file
# Add or search entry
# loop
# End