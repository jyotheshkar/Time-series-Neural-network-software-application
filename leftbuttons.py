import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

class UploadDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Upload Data")
        self.root.configure(bg='black')  # Set the window background to black

        self.activity_levels_file_path = None
        self.temperature_analysis_file_path = None

        # Create a frame to center the buttons
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Set up the button grid layout
        self.create_upload_buttons()
        self.create_view_buttons()
        self.create_save_button()

        self.center_window(600, 300, 180)  # Adjusted the x_offset to move the window slightly to the right

    def button_style(self):
        return {
            'bg': '#555555',  # Button background color
            'fg': 'white',    # Button text color
            'font': ('Helvetica', 11),  # Font style same as leftbuttons.py
            'activebackground': '#777777',  # Button background color when clicked
            'activeforeground': 'white',  # Button text color when clicked
            'bd': 0,  # No border
            'highlightthickness': 2,
            'highlightcolor': 'blue',
            'highlightbackground': 'blue',
            'width': 20,  # Width of the button
            'height': 2   # Height of the button
        }

    def create_upload_buttons(self):
        self.upload_activity_button = tk.Button(self.main_frame, text="Upload Daily Activity Data", command=self.upload_activity_data, **self.button_style())
        self.upload_activity_button.grid(row=0, column=0, padx=20, pady=10)

        self.upload_temperature_button = tk.Button(self.main_frame, text="Upload Temperature Data", command=self.upload_temperature_data, **self.button_style())
        self.upload_temperature_button.grid(row=0, column=1, padx=20, pady=10)

    def create_view_buttons(self):
        self.view_activity_button = tk.Button(self.main_frame, text="View Daily Activity Data", command=self.view_activity_data, state=tk.DISABLED, **self.button_style())
        self.view_activity_button.grid(row=1, column=0, padx=20, pady=10)

        self.view_temperature_button = tk.Button(self.main_frame, text="View Temperature Data", command=self.view_temperature_data, state=tk.DISABLED, **self.button_style())
        self.view_temperature_button.grid(row=1, column=1, padx=20, pady=10)

    def create_save_button(self):
        self.save_button = tk.Button(self.main_frame, text="Save", command=self.save_data, bg='#2e8b57', fg='white', font=('Helvetica', 11, 'bold'), width=10, height=2, bd=0, highlightthickness=0)
        self.save_button.grid(row=2, column=0, columnspan=2, pady=20)

    def center_window(self, width, height, x_offset=0):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2) + x_offset
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def upload_activity_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
        if file_path:
            self.activity_levels_file_path = file_path
            self.view_activity_button.config(state=tk.NORMAL)

    def upload_temperature_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
        if file_path:
            self.temperature_analysis_file_path = file_path
            self.view_temperature_button.config(state=tk.NORMAL)

    def view_activity_data(self):
        if self.activity_levels_file_path is not None:
            os.startfile(self.activity_levels_file_path)

    def view_temperature_data(self):
        if self.temperature_analysis_file_path is not None:
            os.startfile(self.temperature_analysis_file_path)

    def save_data(self):
        if self.activity_levels_file_path is not None or self.temperature_analysis_file_path is not None:
            # Save the data to a file or database as per requirement
            messagebox.showinfo("Save", "Data saved successfully!")
        else:
            messagebox.showwarning("Save", "No data to save!")

class VisualizeDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualize Data")
        self.root.configure(bg='black')  # Set the window background to black

        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.create_visualize_interface()

        self.center_window(600, 300, 180)  # Adjusted the x_offset to move the window slightly to the right

    def create_visualize_interface(self):
        label = tk.Label(self.main_frame, text="Cow ID Number:", bg='black', fg='white', font=('Helvetica', 11))
        label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.cow_id_entry = tk.Entry(self.main_frame, font=('Helvetica', 11), width=20)
        self.cow_id_entry.grid(row=0, column=1, padx=10, pady=10, ipady=5, sticky=tk.W)

        self.data_type = tk.StringVar(value="activity")
        activity_radio = tk.Radiobutton(self.main_frame, text="Visualize Daily Activity Levels", variable=self.data_type, value="activity", bg='black', fg='white', font=('Helvetica', 11), selectcolor='black')
        activity_radio.grid(row=1, column=0, padx=10, pady=10)

        temperature_radio = tk.Radiobutton(self.main_frame, text="Visualize Temperature Data", variable=self.data_type, value="temperature", bg='black', fg='white', font=('Helvetica', 11), selectcolor='black')
        temperature_radio.grid(row=1, column=1, padx=10, pady=10)

        visualize_button = tk.Button(self.main_frame, text="Visualize", command=self.visualize_data, bg='#2e8b57', fg='white', font=('Helvetica', 11, 'bold'), width=10, height=2, bd=0, highlightthickness=0)
        visualize_button.grid(row=2, column=0, columnspan=2, pady=20)

    def visualize_data(self):
        cow_id = self.cow_id_entry.get()
        data_type = self.data_type.get()

        # Add visualization logic here
        messagebox.showinfo("Visualize", f"Visualizing {data_type} data for Cow ID: {cow_id}")

    def center_window(self, width, height, x_offset=0):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2) + x_offset
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

def create_buttons(parent_frame):
    # Create a frame for the buttons
    button_frame = tk.Frame(parent_frame, bg='black')  # Set the frame background to black
    button_frame.pack(side=tk.BOTTOM, anchor='sw', padx=10, pady=5)

    # Button configuration
    button_config = {
        'bg': '#555555',  # Button background color
        'fg': 'white',    # Button text color
        'font': ("Helvetica", 11),  # Reduced font size
        'width': 16,  # Reduced width
        'height': 2,  # Reduced height
        'bd': 0,
        'highlightthickness': 2,
        'highlightcolor': 'blue',
        'highlightbackground': 'blue',
        'activebackground': '#777777',
        'activeforeground': 'white'
    }

    def open_upload_data():
        upload_data_window = tk.Toplevel(parent_frame)
        app = UploadDataApp(upload_data_window)
        upload_data_window.transient(parent_frame)  # Set to be on top of the parent window
        upload_data_window.grab_set()  # Modal-like behavior
        parent_frame.wait_window(upload_data_window)  # Pause the main window until this one closes

    def open_visualize_data():
        visualize_data_window = tk.Toplevel(parent_frame)
        app = VisualizeDataApp(visualize_data_window)
        visualize_data_window.transient(parent_frame)  # Set to be on top of the parent window
        visualize_data_window.grab_set()  # Modal-like behavior
        parent_frame.wait_window(visualize_data_window)  # Pause the main window until this one closes

    # Create the buttons
    upload_button = tk.Button(button_frame, text="Upload Data", command=open_upload_data, **button_config)
    visualize_button = tk.Button(button_frame, text="Visualize Data", command=open_visualize_data, **button_config)
    download_button = tk.Button(button_frame, text="Download Report", **button_config)

    # Arrange the buttons in a grid
    upload_button.grid(row=0, column=0, padx=10, pady=10)
    visualize_button.grid(row=0, column=1, padx=10, pady=10)
    download_button.grid(row=1, column=1, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    create_buttons(root)
    root.mainloop()
