import tkinter as tk
from PIL import Image, ImageTk
import psutil
import threading
import time


def update_system_usage():
    while True:
        # Get CPU and memory usage
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        battery_info = psutil.sensors_battery()

        # Update labels with new values
        cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        memory_label.config(text=f"Memory Usage: {memory_percent}%")
        battery_percent.config(text=f"Battery Percent: {battery_info.percent}%")
        battery_stat.config(text=f"Charging: {isCharging(battery_info.power_plugged)}")

        time.sleep(1)  # Sleep for 1 second before updating again


def isCharging(batt_info):
    if batt_info == True:
        return "Yes"
    else:
        return "No"


def start_update_thread():
    update_thread = threading.Thread(target=update_system_usage, daemon=True)
    update_thread.start()


# Create the main window
root = tk.Tk()
root.title("System Monitoring App")

# Load icons for labels
# Load and resize the icon using Pillow
original_icon = Image.open("assets/cpu-12.png")  # Replace with your icon file path
resized_icon = original_icon.resize((50, 50), Image.ADAPTIVE)  # Resize to 50x50 pixels
cpu_icon = ImageTk.PhotoImage(resized_icon)

mem_original = Image.open("assets/ram.png")
mem_resized = mem_original.resize((45, 45), Image.ADAPTIVE)
memory_icon = ImageTk.PhotoImage(mem_resized)  # Replace with your own Memory icon path

batt_original = Image.open("assets/battery.png")
batt_resized = batt_original.resize((50, 50), Image.ADAPTIVE)
battery_icon = ImageTk.PhotoImage(
    batt_resized
)  # Replace with your own battery icon path


# Create labels for CPU and memory usage
cpu_label = tk.Label(
    root,
    font=("Helvetica", 24),
    image=cpu_icon,
    compound="left",
    wraplength=1000,
    justify="left",
)
cpu_label.pack()

memory_label = tk.Label(
    root,
    font=("Helvetica", 24),
    image=memory_icon,
    compound="left",
    wraplength=1000,
    justify="left",
)
memory_label.pack()

battery_percent = tk.Label(
    root,
    font=("Helvetica", 24),
    image=battery_icon,
    compound="left",
    wraplength=1000,
    justify="left",
)
battery_percent.pack()

battery_stat = tk.Label(root, font=("Helvetica", 24), wraplength=1000)
battery_stat.pack()

# Start the thread to update system usage
start_update_thread()

# Start the Tkinter main loop
root.mainloop()
