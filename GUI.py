# pseudocode
from tkinter import *

panel_1 = Tk()
panel_1.title("COVID Contact Tracing")
panel_1.geometry("500x350")

#frame
frame = Frame(panel_1)
frame.pack(pady=20, padx=60, fill="both", expand=True )

# Welcome Greetings
welcome = Label(frame, text = "Welcome", font=("Times New Roman", 32))
welcome.pack(pady=12, padx=10)

# Program Description
sub_head = Label(frame, text ="COVID Contact Tracing")
sub_head.pack(pady=12,padx=10)

# Start Button
start = Button(frame, text = "Start") 
start.pack(pady=12, padx=10)

# Search Entry
search_title = Label(frame, text = "Search Name:")
search_title.pack(pady=12, padx=10)
search_entry = Entry(frame)
search_entry.pack(pady=12, padx=10)

panel_1.mainloop()

# get information (name, age, bday, address, contact no., etc.)
# questions about covid status (vaccinated or booster?, symptoms, exposure to probable cause, in contact with someone, tested for covid?)
# submits the data and save in a file
# Add or search entry
# loop
# End