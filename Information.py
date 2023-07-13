# pseudocode
from tkinter import *

start = Tk()
start.title("COVID Contact Tracing")
start.geometry("500x500")

# titles

welcome = Label(start, text = "Welcome")
welcome.pack()

#buttons
submit = Button(start, text = "Start") 
submit.pack()
start.mainloop()
# get information (name, age, bday, address, contact no., etc.)
# questions about covid status (vaccinated or booster?, symptoms, exposure to probable cause, in contact with someone, tested for covid?)
# submits the data and save in a file
# Add or search entry
# loop
# End