import sys
from PyQt5.QtWidgets import QApplication

# 🔹 Import GUI - Fixed to match your actual structure
from gui.gui import AuraAdvancedGUI  # Correct class name from your document

# 🔹 Import Assistant logic
from assistant import Assistant


def main():
    print("🚀 AURA Voice Assistant Starting...")

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    # 🖥️ Create GUI with correct class name
    ui = AuraAdvancedGUI()
    ui.show()

    print("✅ AURA Interface Ready")

    # 🤖 Start Assistant (runs in background thread)
    assistant = Assistant(ui)

    # Handle app exit
    def on_exit():
        print("🛑 Shutting down assistant...")
        assistant.stop()

    app.aboutToQuit.connect(on_exit)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()