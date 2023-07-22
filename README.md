# COVID Contact Tracing Application

The COVID Contact Tracing Application is a simple Python-based GUI application that allows users to provide their personal information and answer health declaration questions to assist in COVID contact tracing efforts. It uses a customtkinter module to improve the design and overall interface.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Application Features](#application-features)

## Requirements

Before running the application, make sure you have the following requirements installed on your system:

- Python 3.x
- tkinter (already included with most Python distributions)
- customtkinter (https://customtkinter.tomschimansky.com)
- csv
  
## Installation

1. Clone the repository to your local machine:
2. Navigate to the project directory:
3. Run the application:

## Usage

1. Once the application is launched, a welcome window will be displayed with two buttons: "Start" and "Search."

2. Click the "Start" button to proceed with providing your personal information. You will be directed to a personal information input window.

3. Fill in all the required fields, including your first name, last name, biological sex, age, address, contact number, email, and the current date. Make sure to check the data privacy checkbox before proceeding.

4. After filling in the personal information, click the "Next" button to answer the health declaration questions.

5. Answer all the health declaration questions honestly by selecting "Yes" or "No" for each question.

6. Click the "Submit" button to save the information and responses. You will be prompted whether you want to add another entry or search for an entry. Choose accordingly.

7. If you want to search for an entry, click the "Search" button on the welcome window. You will be directed to the search window.

8. In the search window, you can enter a name or date in the provided entry box and click the "Enter" button to perform a search. The matching records will be displayed in the listbox.

## Application Features

The COVID Contact Tracing application provides the following features:

- Adding personal information, including first name, last name, sex, age, address, contact number, email, and the current date.
- Answering health declaration questions to determine potential COVID exposure.
- Saving the personal information and responses in a CSV file named "COVID Tracker.csv."
- Searching for existing records by name or date.

---

# Code Explanation

Below is an overview of the main Python files included in the COVID Contact Tracing application:

### main.py

This script serves as the entry point to the application. It imports the necessary modules and initializes the main window of the application by creating an instance of the `CovidUI` class defined in `home_window.py`.

### home_window.py

This file contains the implementation of the `CovidUI` class, which represents the main window of the application. It inherits from a custom tkinter class (`CTk`) that provides appearance settings and basic functionalities. The `CovidUI` class includes methods for handling user interactions, such as starting the personal information input process and opening the search window.

### personal_info.py

This file defines the `PersonalWindow` class, which represents the window for users to provide their personal information. The class inherits from `Toplevel`, a tkinter widget used to create secondary windows. The `PersonalWindow` class includes methods for handling user interactions, such as submitting personal information and validating user inputs.

### search_window.py

This file contains the `SearchWindow` class, which represents the window for searching existing records. Similar to `personal_info.py`, it inherits from `Toplevel`. The `SearchWindow` class includes methods for handling user interactions, such as performing a search and displaying the results in a listbox.

### customtkinter.py

This module provides custom tkinter classes and functions for appearance settings and enhanced widgets. It includes classes for custom labels, buttons, frames, checkboxes, and fonts. The `set_appearance_mode` and `set_default_color_theme` functions allow users to set the appearance mode and color theme of the application.

Please note that the code provided is a simplified version of the COVID Contact Tracing application and may not include all the required code to run the application. For the complete application, please refer to the actual code in the respective files.

## Demo

You can access my demo through this link:

