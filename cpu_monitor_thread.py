import tkinter as tk
from PIL import Image, ImageTk
import psutil
import threading
import time


def update_system_usage():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent

        # Update the labels with new values in the GUI thread
        cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        memory_label.config(text=f"Memory Usage: {memory_percent}%")

        time.sleep(1)  # Sleep for 1 second before updating again


def start_update_thread():
    update_thread = threading.Thread(target=update_system_usage, daemon=True)
    update_thread.start()


# Create the main window
root = tk.Tk()
root.title("System Monitoring App")

# Load and resize the icon using Pillow
original_icon = Image.open("assets/cpu-12.png")  # Replace with your icon file path
resized_icon = original_icon.resize((50, 50), Image.ADAPTIVE)  # Resize to 50x50 pixels
icon = ImageTk.PhotoImage(resized_icon)

# Create labels with resized icons
cpu_label = tk.Label(root, font=("Helvetica", 24), image=icon, compound="left")
cpu_label.pack()

memory_label = tk.Label(root, font=("Helvetica", 24), image=icon, compound="left")
memory_label.pack()

# Start the thread to update system usage
start_update_thread()

# Start the Tkinter main loop
root.mainloop()
