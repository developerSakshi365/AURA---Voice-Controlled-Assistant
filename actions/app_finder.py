import os

START_MENU_PATHS = [
    os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs"),
    os.path.join(os.environ["PROGRAMDATA"], r"Microsoft\Windows\Start Menu\Programs")
]

def find_app(app_name):
    app_name = app_name.lower()

    for path in START_MENU_PATHS:
        for root, _, files in os.walk(path):
            for file in files:
                if app_name in file.lower():
                    return os.path.join(root, file)

    return None
