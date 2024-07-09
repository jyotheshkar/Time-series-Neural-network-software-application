import tkinter as tk
import os

def center_window():
    root.update_idletasks()
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate 90% of screen width and 72% of screen height
    width = int(screen_width * 0.90)
    height = int(screen_height * 0.72)

    # Calculate position x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f'{width}x{height}+{x}+{y}')

# Create the main window
root = tk.Tk()
root.title("Time-series Neural Network Software Suite")

# Set the window icon
icon_path = os.path.abspath('photo/cow.ico')  # Ensure you have the 'icon.ico' file in the specified path
root.iconbitmap(icon_path)

# Set the background color to black
root.configure(bg='black')

# Create a frame for the main content with less padding at the top
main_frame = tk.Frame(root, bg='black')
main_frame.pack(pady=(10, 0), fill=tk.BOTH, expand=True)  # Less padding at the top

# Add a label to the main frame
label = tk.Label(main_frame, text="Hello, I am tkinter", bg='black', fg='white', font=("Helvetica", 16))
label.pack(pady=20)

# Create a frame for adding bottom spacing
bottom_frame = tk.Frame(root, bg='black')
bottom_frame.pack(side=tk.BOTTOM, pady=40, fill=tk.X)  # More padding at the bottom

# Center the window after all widgets are created
center_window()

# Run the application
root.mainloop()
