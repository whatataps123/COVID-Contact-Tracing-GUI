from tkinter import *


panel_2 = Tk()
panel_2.title("Personal Information")
panel_2.geometry("500x350")

#frame
frame = Frame(panel_2)
frame.pack(pady=20, padx=60, fill="both", expand=True )

# Personal Information Headings
welcome = Label(frame, text = "Personal Information", font=("Times New Roman", 32))
welcome.pack(pady=12, padx=10)

panel_2.mainloop()