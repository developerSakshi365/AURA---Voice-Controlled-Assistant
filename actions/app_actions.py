import os
import subprocess
import winreg

def open_app(app_name):
    try:
        subprocess.Popen(app_name)
        return f"Opening {app_name}"
    except:
        return f"I couldn't find {app_name}"

def close_app(app_name):
    os.system(f"taskkill /f /im {app_name}.exe")
    return f"Closing {app_name}"