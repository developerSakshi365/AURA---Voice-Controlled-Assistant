import os
import webbrowser
import urllib.parse
import time
import ctypes
import subprocess
import pyautogui
import psutil
import threading
import re
from datetime import datetime
from speaker import speak

# ---------------- APP PROCESS MAP ----------------
APP_PROCESSES = {
    "chrome": ["chrome.exe"],
    "notepad": ["notepad.exe"],
    "calculator": ["CalculatorApp.exe"],
    "explorer": ["explorer.exe"],
    "whatsapp": ["WhatsApp.exe", "msedgewebview2.exe"],
    "spotify": ["Spotify.exe"],
    "vscode": ["Code.exe"],
    "discord": ["Discord.exe"],
    "word": ["WINWORD.EXE"],
    "excel": ["EXCEL.EXE"],
    "powerpoint": ["POWERPNT.EXE"],
    "task manager": ["Taskmgr.exe"]
}

# ---------------- HELPERS ----------------
def extract_query(text, triggers):
    text = text.lower()
    for t in triggers:
        if t in text:
            return text.replace(t, "").strip()
    return None

def desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

# ---------------- ALARM HELPERS ----------------
def parse_alarm_time(text):
    text = text.lower()

    match = re.search(r'(\d{1,2})[:.](\d{2})', text)
    if not match:
        return None

    hour = int(match.group(1))
    minute = int(match.group(2))

    if "pm" in text and hour < 12:
        hour += 12
    if "am" in text and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute:02d}"

def alarm_thread(alarm_time):
    speak(f"Alarm will ring at {alarm_time}")
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == alarm_time:
            speak("Alarm ringing. Wake up!")
            break
        time.sleep(1)

import ctypes
import time

def toggle_screen_recording():
    # Press Win + Alt + R
    ctypes.windll.user32.keybd_event(0x5B, 0, 0, 0)  # Win
    ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)  # Alt
    ctypes.windll.user32.keybd_event(0x52, 0, 0, 0)  # R

    time.sleep(0.1)

    ctypes.windll.user32.keybd_event(0x52, 0, 2, 0)
    ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)
    ctypes.windll.user32.keybd_event(0x5B, 0, 2, 0)

# 🪟 ALT + TAB (Switch Windows)
def switch_window():
    ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)  # Alt
    ctypes.windll.user32.keybd_event(0x09, 0, 0, 0)  # Tab
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(0x09, 0, 2, 0)
    ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)

# 🌐 CTRL + TAB (Next browser tab)
def next_tab():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # Ctrl
    ctypes.windll.user32.keybd_event(0x09, 0, 0, 0)  # Tab
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(0x09, 0, 2, 0)
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)

# 🌐 CTRL + SHIFT + TAB (Previous tab)
def previous_tab():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)   # Ctrl
    ctypes.windll.user32.keybd_event(0x10, 0, 0, 0)   # Shift
    ctypes.windll.user32.keybd_event(0x09, 0, 0, 0)   # Tab
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(0x09, 0, 2, 0)
    ctypes.windll.user32.keybd_event(0x10, 0, 2, 0)
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)

# ---------------- MAIN ROUTER ----------------
def handle_intent(intent, text=None, last_app=None):

    try:
        # 🔍 GOOGLE SEARCH
        if intent == "search_google":
            q = extract_query(text, [
                "search for", "search google for", "google search",
                "find on google", "look up"
            ])
            if q:
                webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote(q))
                speak(f"Searching Google for {q}")
            return None, None

        # 🎥 YOUTUBE SEARCH
        if intent == "search_youtube":
            q = extract_query(text, [
                "search youtube for", "find on youtube", "play on youtube"
            ])
            if q:
                webbrowser.open("https://www.youtube.com/results?search_query=" + urllib.parse.quote(q))
                speak(f"Searching YouTube for {q}")
            return None, None

        # 🌐 OPEN APPS
        if intent == "open_chrome":
            subprocess.Popen("start chrome", shell=True)
            speak("Opening Chrome")
            return None, "chrome"

        # 🔵 BLUETOOTH ON
        if intent == "bluetooth_on":
            os.system("start ms-settings:bluetooth")
            speak("Opening Bluetooth settings")
            return None, None

        # 🔵 BLUETOOTH OFF
        if intent == "bluetooth_off":
            os.system("start ms-settings:bluetooth")
            speak("Opening Bluetooth settings")
            return None, None

        if intent == "screen_record_start":
            toggle_screen_recording()
            speak("Screen recording started")
            return None, None

        # 🪟 SWITCH WINDOW
        if intent == "switch_window":
            switch_window()
            speak("Switching window")
            return None, None

        # 🌐 NEXT TAB
        if intent == "next_tab":
            next_tab()
            speak("Switching tab")
            return None, None

        # 🌐 PREVIOUS TAB
        if intent == "previous_tab":
            previous_tab()
            speak("Going to previous tab")
            return None, None

        if intent == "open_explorer":
            subprocess.Popen("explorer", shell=True)
            speak("Opening File Explorer")
            return None, "explorer"

        if intent == "open_notepad":
            subprocess.Popen("notepad", shell=True)
            speak("Opening Notepad")
            return None, "notepad"

        if intent == "open_calculator":
            subprocess.Popen("start calculator:", shell=True)
            speak("Opening Calculator")
            return None, "calculator"

        if intent == "open_whatsapp":
            subprocess.Popen("start whatsapp:", shell=True)
            speak("Opening WhatsApp")
            return None, "whatsapp"

        if intent == "open_spotify":
            subprocess.Popen("start spotify", shell=True)
            speak("Opening Spotify")
            return None, "spotify"

        if intent == "open_vscode":
            subprocess.Popen("start code", shell=True)
            speak("Opening Visual Studio Code")
            return None, "vscode"

        if intent == "open_discord":
            subprocess.Popen("start discord", shell=True)
            speak("Opening Discord")
            return None, "discord"

        if intent == "open_word":
            subprocess.Popen("start winword", shell=True)
            speak("Opening Microsoft Word")
            return None, "word"

        if intent == "open_excel":
            subprocess.Popen("start excel", shell=True)
            speak("Opening Microsoft Excel")
            return None, "excel"

        if intent == "open_powerpoint":
            subprocess.Popen("start powerpnt", shell=True)
            speak("Opening PowerPoint")
            return None, "powerpoint"

        # 🧠 TASK MANAGER
        if intent == "open_task_manager":
            subprocess.Popen("taskmgr", shell=True)
            speak("Opening Task Manager")
            return None, None

        # 📷 CAMERA
        if intent == "open_camera":
            os.system("start microsoft.windows.camera:")
            speak("Opening camera")
            return None, None

        # ⚙️ SETTINGS
        if intent == "open_settings":
            os.system("start ms-settings:")
            speak("Opening settings")
            return None, None

        # 💻 SYSTEM INFO
        if intent == "system_info":
            subprocess.Popen("msinfo32", shell=True)
            speak("Opening system information")
            return None, None

        # ❌ CLOSE APP
        if intent == "close_app" and text:
            for app, procs in APP_PROCESSES.items():
                if app in text.lower():
                    for p in procs:
                        os.system(f"taskkill /f /im {p} >nul 2>&1")
                    speak(f"Closing {app}")
                    return None, None
            speak("I don't know which app to close")
            return None, None

        # 📸 SCREENSHOT
        if intent == "take_screenshot":
            file = os.path.join(desktop_path(), f"screenshot_{int(time.time())}.png")
            pyautogui.screenshot(file)
            speak("Screenshot saved on Desktop")
            return None, None

        # 🔊 VOLUME
        if intent == "volume_up":
            for _ in range(5):
                ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)
            speak("Volume increased")
            return None, None

        if intent == "volume_down":
            for _ in range(5):
                ctypes.windll.user32.keybd_event(0xAE, 0, 0, 0)
            speak("Volume decreased")
            return None, None

        if intent == "mute":
            ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)
            speak("Volume muted")
            return None, None

        if intent == "unmute":
            ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)
            speak("Volume unmuted")
            return None, None

        # 🌞 BRIGHTNESS
        if intent == "brightness_up":
            subprocess.run(
                ["powershell",
                 "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,90)"],
                shell=True
            )
            speak("Brightness increased")
            return None, None

        if intent == "brightness_down":
            subprocess.run(
                ["powershell",
                 "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,30)"],
                shell=True
            )
            speak("Brightness decreased")
            return None, None

        # 🔋 BATTERY
        if intent == "battery_status":
            battery = psutil.sensors_battery()
            speak(f"Battery is at {battery.percent} percent")
            return None, None

        # ⏰ TIME / DATE
        if intent == "time":
            speak(datetime.now().strftime("The time is %I:%M %p"))
            return None, None

        if intent == "date":
            speak(datetime.now().strftime("Today's date is %B %d, %Y"))
            return None, None

        # ⏰ SET ALARM (FIXED)
        if intent == "set_alarm":
            alarm_time = parse_alarm_time(text)

            if alarm_time:
                speak(f"Alarm set for {alarm_time}")
                threading.Thread(
                    target=alarm_thread,
                    args=(alarm_time,),
                    daemon=True
                ).start()
            else:
                speak("Please say the alarm time clearly")
            return None, None

        # 🔒 SYSTEM
        if intent == "lock":
            ctypes.windll.user32.LockWorkStation()
            speak("System locked")
            return None, None

        if intent == "shutdown":
            speak("Shutting down system")
            os.system("shutdown /s /t 1")

        if intent == "restart":
            speak("Restarting system")
            os.system("shutdown /r /t 1")


        # 🛑 STOP
        if intent == "stop":
            speak("Okay, stopping")
            return None, None

    except Exception as e:
        speak("Sorry, something went wrong")
        print("ERROR:", e)

    return None, None
