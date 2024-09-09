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
        memory_total = memory_info.total
        memory_used = memory_info.used
        battery_info = psutil.sensors_battery()
        # internet_info = psutil.net_if_stats()

        # Update labels with new values
        cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        memory_label.config(text=f"Memory Usage: {memory_percent}%")
        memory_total_label.config(
            text=f"Total Memory: {memory_total / (1024**3):.2f} GB"
        )
        memory_used_label.config(text=f"Used Memory: {memory_used / (1024**3):.2f} GB")
        battery_percent.config(text=f"Battery Percent: {battery_info.percent}%")
        # internet_stat.config(text=f"Internet: {internet_info}")
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


# Load and resize the icons using Pillow
def load_resized_icon(path, size):
    original_icon = Image.open(path)
    resized_icon = original_icon.resize(size, Image.ADAPTIVE)
    return ImageTk.PhotoImage(resized_icon)


cpu_icon = load_resized_icon("assets/cpu-12.png", (50, 50))
memory_icon = load_resized_icon("assets/ram.png", (45, 45))
battery_icon = load_resized_icon("assets/battery.png", (50, 50))

# Create a frame for the icons and labels
left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# Create labels for CPU, memory usage, and battery
cpu_label = tk.Label(
    left_frame, font=("Helvetica", 15), image=cpu_icon, compound="left", padx=16
)
cpu_label.grid(row=0, column=0, sticky="w", pady=5)

memory_label = tk.Label(
    left_frame, font=("Helvetica", 15), image=memory_icon, compound="left", padx=20
)
memory_label.grid(row=1, column=0, sticky="w", pady=5)

memory_total_label = tk.Label(
    left_frame, font=("Helvetica", 15), image=memory_icon, compound="left", padx=20
)
memory_total_label.grid(row=2, column=0, sticky="w", pady=5)

memory_used_label = tk.Label(
    left_frame, font=("Helvetica", 15), image=memory_icon, compound="left", padx=20
)
memory_used_label.grid(row=3, column=0, sticky="w", pady=5)

battery_percent = tk.Label(
    left_frame, font=("Helvetica", 15), image=battery_icon, compound="left", padx=18
)
battery_percent.grid(row=4, column=0, sticky="w", pady=5)

battery_stat = tk.Label(left_frame, font=("Helvetica", 15))
battery_stat.grid(row=5, column=0, sticky="w", pady=5, padx=86)

# internet_stat = tk.Label(left_frame, font=("Helvetica", 24), wraplength=1000)
# internet_stat.grid(row=3, column=0, sticky="w", pady=5, padx=50)

# Start the thread to update system usage
start_update_thread()

# Start the Tkinter main loop
root.mainloop()
