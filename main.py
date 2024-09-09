import psutil
import time


def print_stats():
    # CPU
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Frequency: {psutil.cpu_freq()}")

    # Memory
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024**3):.2f} GB")
    print(f"Used Memory: {memory.used / (1024**3):.2f} GB")
    print(f"Memory Usage: {memory.percent}%")

    # Disk
    disk = psutil.disk_usage("/")
    print(f"Disk Usage: {disk.percent}% (Used: {disk.used / (1024**3):.2f} GB)")

    # Network
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
    print(f"Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")

    # Battery
    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery: {battery.percent}% (Charging: {battery.power_plugged})")

    print("\n")


while True:
    print_stats()
    time.sleep(5)
