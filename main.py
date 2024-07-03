import tkinter as tk
import os

def center_window(width=800, height=600):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x and y coordinates
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f'{width}x{height}+{x}+{y}')

def on_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Centered GUI")

# Set the window icon
icon_path = os.path.abspath('photo/forecast_icon.ico')  # Ensure you have a 'prediction.ico' file in the same directory
root.iconbitmap(icon_path)

# Center the window
center_window(800, 600)

# Set the background color to black
root.configure(bg='black')

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", bg='black', fg='white')
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=on_click, bg='black', fg='white')
button.pack(pady=20)

# Run the application
root.mainloop()
