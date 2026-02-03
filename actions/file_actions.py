import os

def open_downloads():
    os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))

def open_documents():
    os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))
