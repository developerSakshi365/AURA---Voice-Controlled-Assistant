import os
import subprocess
import ctypes
import platform
import psutil

# 🔌 SHUTDOWN
def shutdown_system():
    os.system("shutdown /s /t 5")

# 🔁 RESTART
def restart_system():
    os.system("shutdown /r /t 5")

# 🔒 LOCK
def lock_system():
    ctypes.windll.user32.LockWorkStation()

# 📷 OPEN CAMERA (WINDOWS 10/11)
def open_camera():
    os.system("start microsoft.windows.camera:")

# ⚙️ OPEN SETTINGS
def open_settings():
    os.system("start ms-settings:")

# 🖥️ SYSTEM INFO
def system_info():
    info = {
        "OS": platform.system() + " " + platform.release(),
        "Processor": platform.processor(),
        "RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
        "CPU Cores": psutil.cpu_count(logical=True),
        "Battery": f"{psutil.sensors_battery().percent}%" if psutil.sensors_battery() else "N/A"
    }

    text = ", ".join([f"{k}: {v}" for k, v in info.items()])
    return text

def bluetooth_on():
    command = (
        'powershell -Command '
        '"Get-PnpDevice -Class Bluetooth | '
        'Where-Object {$_.Status -ne \'OK\'} | '
        'Enable-PnpDevice -Confirm:$false"'
    )
    os.system(command)


def bluetooth_off():
    command = (
        'powershell -Command '
        '"Get-PnpDevice -Class Bluetooth | '
        'Where-Object {$_.Status -eq \'OK\'} | '
        'Disable-PnpDevice -Confirm:$false"'
    )
    os.system(command)
