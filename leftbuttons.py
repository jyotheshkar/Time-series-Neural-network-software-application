import tkinter as tk

def create_buttons(parent_frame):
    # Create a frame for the buttons
    button_frame = tk.Frame(parent_frame, bg='black')
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

    # Create the buttons
    upload_button = tk.Button(button_frame, text="Upload Data", **button_config)
    visualize_button = tk.Button(button_frame, text="Visualize Data", **button_config)
    download_button = tk.Button(button_frame, text="Download Report", **button_config)

    # Arrange the buttons in a grid
    upload_button.grid(row=0, column=0, padx=10, pady=10)  # Reduced padx to bring closer to Visualize Data
    visualize_button.grid(row=0, column=1, padx=10, pady=10)  # Reduced padx to bring closer to Upload Data
    download_button.grid(row=1, column=1, padx=10, pady=10)  # Keeping padding for consistency
