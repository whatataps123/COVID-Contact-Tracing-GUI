# pseudocode
import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class CovidUI(customtkinter.CTk):

    def __init__(self):
    # Call method of parent class
        super().__init__()
        self.title("COVID Contact Tracing")
        self.geometry()
        #self.config(bg=GREEN3)
        self.panel_1 = customtkinter.CTkFrame(self)

        # Welcome Greetings
        welcome = customtkinter.CTkLabel(self.panel_1, text = "Welcome", font=customtkinter.CTkFont(size=20, weight="bold"))
        welcome.pack(pady=12, padx=10)

        # Program Description
        sub_head = customtkinter.CTkLabel(self.panel_1, text ="COVID Contact Tracing")
        sub_head.pack(pady=12,padx=10)

        # Start Button
        start = customtkinter.CTkButton(self.panel_1, text = "Start", command=self.start_event) 
        start.pack( padx=20, pady=10, anchor=customtkinter.CENTER)

        # Search Button
        search_button = customtkinter.CTkButton(self.panel_1, text="Search", command=self.start_search_event)
        search_button.pack(padx=20, pady=10, anchor=customtkinter.CENTER)

        self.first_window()

    # To show first window
    def first_window(self):
        self.panel_1.pack(pady=20, padx=60, fill="both", expand=True)

    # Event for Start button, goes to Personal Window
    def start_event(self):
        self.withdraw()
        from personal_info import PersonalWindow
        PersonalWindow()

    # Event for Search button, goes to Search Window
    def start_search_event(self):
        self.withdraw()
        from search_window import SearchWindow
        SearchWindow()
