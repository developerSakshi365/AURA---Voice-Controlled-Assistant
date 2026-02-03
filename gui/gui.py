from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QGraphicsDropShadowEffect, QGridLayout
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QThread
from PyQt5.QtGui import QFont, QPainter, QColor, QPen, QLinearGradient, QRadialGradient, QPixmap, QPalette, QBrush
import math
import os


# ===================== VOICE LISTENER THREAD =====================
class VoiceListenerThread(QThread):
    """Thread to handle voice recognition without blocking the GUI"""
    command_received = pyqtSignal(str)  # Emits the recognized command
    status_changed = pyqtSignal(str)  # Emits status updates (LISTENING, PROCESSING, etc.)

    def __init__(self):
        super().__init__()
        self.is_running = False

    def run(self):
        """Main loop for voice recognition"""
        self.is_running = True

        # Import your voice recognition modules here
        # Example: from your_module import recognize_speech, process_command

        while self.is_running:
            try:
                self.status_changed.emit("LISTENING")

                # TODO: Replace this with your actual speech recognition code
                # Example:
                # command = recognize_speech()  # Your speech recognition function
                # if command:
                #     self.status_changed.emit("PROCESSING")
                #     self.command_received.emit(command)
                #     process_command(command)  # Your command processing function
                #     self.status_changed.emit("SPEAKING")

                # For now, this is a placeholder
                self.msleep(100)  # Small delay to prevent CPU overload

            except Exception as e:
                print(f"Error in voice listener: {e}")
                self.msleep(1000)

    def stop(self):
        """Stop the voice recognition thread"""
        self.is_running = False
        self.wait()


# ===================== ADVANCED ROTATING ORB =====================
class AdvancedOrb(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(280, 280)
        self.angle = 0
        self.active = False
        self.pulse = 0
        self.particles = []

        # Make background transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Generate particles
        for i in range(20):
            self.particles.append({
                'angle': i * 18,
                'distance': 0,
                'speed': 0.5 + (i % 3) * 0.3
            })

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def animate(self):
        self.angle = (self.angle + 2) % 360
        self.pulse = (self.pulse + 0.1) % (2 * math.pi)

        # Update particles
        for p in self.particles:
            if self.active:
                p['distance'] = min(p['distance'] + p['speed'], 60)
                p['angle'] = (p['angle'] + 1) % 360
            else:
                p['distance'] = max(p['distance'] - p['speed'] * 2, 0)

        self.update()

    def set_active(self, state):
        self.active = state

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        cx, cy = 140, 140
        pulse_scale = 1 + math.sin(self.pulse) * 0.05

        # Outer glow rings
        for i in range(3):
            opacity = 30 - i * 10
            radius = 100 + i * 15
            gradient = QRadialGradient(cx, cy, radius)
            gradient.setColorAt(0, QColor(0, 255, 255, opacity))
            gradient.setColorAt(1, QColor(0, 255, 255, 0))
            painter.setBrush(gradient)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(cx - radius, cy - radius, radius * 2, radius * 2)

        # Rotating arcs
        for i in range(3):
            offset = i * 120
            arc_color = QColor(0, 255, 255) if self.active else QColor(0, 200, 255)
            painter.setPen(QPen(arc_color, 3 if i == 1 else 2))
            painter.drawArc(
                40 + i * 10, 40 + i * 10,
                200 - i * 20, 200 - i * 20,
                (self.angle + offset) * 16, 100 * 16
            )

        # Particles
        for p in self.particles:
            rad = math.radians(p['angle'])
            px = cx + math.cos(rad) * (80 + p['distance'])
            py = cy + math.sin(rad) * (80 + p['distance'])

            size = 4 if self.active else 2
            gradient = QRadialGradient(px, py, size * 2)
            gradient.setColorAt(0, QColor(0, 255, 255, 200))
            gradient.setColorAt(1, QColor(0, 255, 255, 0))

            painter.setBrush(gradient)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(int(px - size), int(py - size), size * 2, size * 2)

        # Core sphere
        core_size = int(80 * pulse_scale)
        gradient = QRadialGradient(cx, cy, core_size)

        if self.active:
            gradient.setColorAt(0, QColor(0, 150, 180))
            gradient.setColorAt(0.6, QColor(0, 100, 140))
            gradient.setColorAt(1, QColor(0, 60, 100, 150))
        else:
            gradient.setColorAt(0, QColor(0, 120, 150))
            gradient.setColorAt(0.6, QColor(0, 80, 120))
            gradient.setColorAt(1, QColor(0, 40, 80, 150))

        painter.setBrush(gradient)
        painter.setPen(QPen(QColor(0, 255, 255, 100), 2))
        painter.drawEllipse(cx - core_size, cy - core_size, core_size * 2, core_size * 2)

        # Inner highlight
        highlight = QRadialGradient(cx - 20, cy - 20, 30)
        highlight.setColorAt(0, QColor(255, 255, 255, 150))
        highlight.setColorAt(1, QColor(255, 255, 255, 0))
        painter.setBrush(highlight)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(cx - 35, cy - 35, 50, 50)


# ===================== ADVANCED SOUND WAVE =====================
class AdvancedWave(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(80)
        self.active = False
        self.phase = 0

        # Make background transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(40)

    def set_active(self, state):
        self.active = state

    def animate(self):
        if self.active:
            self.phase += 0.2
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        bars = 30
        bar_w = 4
        gap = 6
        total_w = bars * (bar_w + gap)
        start_x = (self.width() - total_w) // 2
        h = self.height()

        for i in range(bars):
            # Multiple frequency components
            freq1 = math.sin((i + self.phase) * 0.4)
            freq2 = math.sin((i + self.phase) * 0.2 + 1)
            combined = (freq1 + freq2) / 2

            if self.active:
                height = abs(combined) * 50 + 12
            else:
                height = 6

            # Cyan color matching the background
            color = QColor(0, 255, 255, 200)

            # Draw bar with gradient
            gradient = QLinearGradient(0, h - height, 0, h)
            gradient.setColorAt(0, color)
            gradient.setColorAt(1, QColor(0, 180, 255, 100))

            painter.setBrush(gradient)
            painter.setPen(Qt.NoPen)

            x = start_x + i * (bar_w + gap)
            painter.drawRoundedRect(int(x), int(h - height), bar_w, int(height), 2, 2)

            # Glow effect
            if self.active and height > 35:
                glow = QRadialGradient(x + bar_w / 2, h - height, bar_w * 2)
                glow.setColorAt(0, QColor(0, 255, 255, 100))
                glow.setColorAt(1, QColor(0, 255, 255, 0))
                painter.setBrush(glow)
                painter.drawEllipse(int(x - bar_w), int(h - height - bar_w), bar_w * 3, bar_w * 3)


# ===================== MODERN STATUS CARD =====================
class ModernCard(QFrame):
    def __init__(self, title, icon=""):
        super().__init__()
        # Glass morphism effect
        self.setStyleSheet("""
            QFrame {
                background: rgba(0, 20, 40, 120);
                border: 1px solid rgba(0, 255, 255, 150);
                border-radius: 10px;
                padding: 12px;
            }
        """)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(0, 255, 255, 80))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)
        layout.setSpacing(6)

        # Title with icon
        title_layout = QHBoxLayout()
        self.title = QLabel(f"{icon} {title}" if icon else title)
        self.title.setStyleSheet("""
            color: #00FFFF;
            font-size: 10px;
            font-weight: bold;
            letter-spacing: 1px;
        """)
        title_layout.addWidget(self.title)
        title_layout.addStretch()
        layout.addLayout(title_layout)

        # Value
        self.value = QLabel("-")
        self.value.setStyleSheet("""
            color: #FFFFFF;
            font-size: 14px;
            font-weight: 500;
        """)
        self.value.setWordWrap(True)
        layout.addWidget(self.value)

    def set_value(self, text):
        self.value.setText(text)


# ===================== ANIMATED BUTTON =====================
class GlowButton(QPushButton):
    def __init__(self, text, primary=False):
        super().__init__(text)
        self.primary = primary
        self.setFixedHeight(55)
        self.setMinimumWidth(200)
        self.setCursor(Qt.PointingHandCursor)

        if primary:
            self.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y2:0,
                        stop:0 rgba(0, 200, 255, 180),
                        stop:1 rgba(0, 255, 255, 180)
                    );
                    color: #000000;
                    border: 2px solid #00FFFF;
                    border-radius: 27px;
                    font-size: 15px;
                    font-weight: bold;
                    padding: 10px 35px;
                }
                QPushButton:hover {
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y2:0,
                        stop:0 rgba(0, 220, 255, 220),
                        stop:1 rgba(0, 255, 255, 220)
                    );
                    border: 2px solid #FFFFFF;
                }
                QPushButton:pressed {
                    background: rgba(0, 180, 255, 200);
                }
                QPushButton:disabled {
                    background: rgba(30, 50, 80, 120);
                    color: rgba(100, 150, 200, 150);
                    border: 2px solid rgba(0, 191, 255, 80);
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background: rgba(0, 30, 60, 150);
                    color: #00FFFF;
                    border: 2px solid rgba(0, 255, 255, 120);
                    border-radius: 27px;
                    font-size: 15px;
                    font-weight: bold;
                    padding: 10px 35px;
                }
                QPushButton:hover {
                    background: rgba(0, 50, 90, 180);
                    border: 2px solid #00FFFF;
                }
                QPushButton:pressed {
                    background: rgba(0, 40, 70, 150);
                }
                QPushButton:disabled {
                    background: rgba(20, 30, 50, 100);
                    color: rgba(0, 191, 255, 100);
                    border: 2px solid rgba(0, 191, 255, 60);
                }
            """)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 255, 255, 180) if primary else QColor(0, 255, 255, 100))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)


# ===================== MAIN ADVANCED GUI =====================
class AuraAdvancedGUI(QWidget):
    signal_command = pyqtSignal(str)
    signal_intent = pyqtSignal(str, float)
    signal_response = pyqtSignal(str)
    signal_mic = pyqtSignal(str)

    def __init__(self, voice_assistant=None):
        super().__init__()
        self.setWindowTitle("AURA - Advanced Voice Assistant")
        self.setGeometry(200, 50, 1000, 800)

        # State tracking
        self.is_listening = False
        self.voice_assistant = voice_assistant  # Your main voice assistant instance
        self.listener_thread = None

        # Set background image
        self.set_background_image()

        self.build_ui()
        self.connect_signals()

    def set_background_image(self):
        """Set the background image from assets folder"""
        bg_path = os.path.join("assets", "bg.jpg")

        if os.path.exists(bg_path):
            # Create a palette and set the background
            palette = QPalette()
            pixmap = QPixmap(bg_path)
            # Scale to window size
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            brush = QBrush(scaled_pixmap)
            palette.setBrush(QPalette.Window, brush)
            self.setPalette(palette)
            self.setAutoFillBackground(True)
        else:
            # Fallback to gradient if image not found
            print(f"Warning: Background image not found at {bg_path}")
            self.setStyleSheet("""
                QWidget {
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y2:1,
                        stop:0 #0a0e27,
                        stop:0.5 #1a1e3f,
                        stop:1 #0a0e27
                    );
                }
            """)

    def resizeEvent(self, event):
        """Update background when window is resized"""
        super().resizeEvent(event)
        bg_path = os.path.join("assets", "bg.jpg")
        if os.path.exists(bg_path):
            palette = QPalette()
            pixmap = QPixmap(bg_path)
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            brush = QBrush(scaled_pixmap)
            palette.setBrush(QPalette.Window, brush)
            self.setPalette(palette)

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(30, 20, 30, 25)

        # Header
        header_layout = QVBoxLayout()
        header_layout.setSpacing(3)

        title = QLabel("AURA")
        title.setFont(QFont("Arial Black", 58, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            color: #00FFFF;
            padding: 8px;
            letter-spacing: 8px;
            font-weight: 900;
            text-transform: uppercase;
        """)

        title_shadow = QGraphicsDropShadowEffect(title)
        title_shadow.setBlurRadius(50)
        title_shadow.setColor(QColor(0, 255, 255, 255))
        title_shadow.setOffset(0, 0)
        title.setGraphicsEffect(title_shadow)

        subtitle = QLabel("Advanced Voice Assistant Interface")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            color: #00FFFF; 
            font-size: 16px; 
            letter-spacing: 3px;
            font-weight: 500;
        """)

        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        layout.addLayout(header_layout)

        layout.addSpacing(5)

        # Orb
        self.orb = AdvancedOrb()
        layout.addWidget(self.orb, alignment=Qt.AlignCenter)

        # Sound wave
        self.wave = AdvancedWave()
        layout.addWidget(self.wave, alignment=Qt.AlignCenter)

        layout.addSpacing(5)

        # Status indicator
        status_container = QHBoxLayout()
        status_container.addStretch()

        self.status = QLabel("● IDLE")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("""
            color: rgba(0, 200, 255, 220);
            font-size: 14px;
            font-weight: bold;
            padding: 6px 18px;
            background: rgba(0, 20, 40, 150);
            border-radius: 15px;
            border: 1px solid rgba(0, 255, 255, 120);
        """)

        status_container.addWidget(self.status)
        status_container.addStretch()
        layout.addLayout(status_container)

        layout.addSpacing(10)

        # Info cards grid
        cards_grid = QGridLayout()
        cards_grid.setSpacing(12)

        self.command = ModernCard("COMMAND", "🎤")
        self.intent = ModernCard("INTENT", "🎯")
        self.confidence = ModernCard("CONFIDENCE", "📊")

        cards_grid.addWidget(self.command, 0, 0)
        cards_grid.addWidget(self.intent, 0, 1)
        cards_grid.addWidget(self.confidence, 0, 2)

        layout.addLayout(cards_grid)

        # Response card
        self.response = ModernCard("RESPONSE", "💬")
        layout.addWidget(self.response)

        layout.addSpacing(5)

        # Control buttons
        btns = QHBoxLayout()
        btns.setSpacing(25)

        self.start_btn = GlowButton("🎤 START LISTENING", primary=True)
        self.stop_btn = GlowButton("⏹ STOP")
        self.stop_btn.setEnabled(False)  # Initially disabled

        # Connect button clicks
        self.start_btn.clicked.connect(self.start_listening)
        self.stop_btn.clicked.connect(self.stop_listening)

        btns.addStretch()
        btns.addWidget(self.start_btn)
        btns.addWidget(self.stop_btn)
        btns.addStretch()

        layout.addLayout(btns)

    def connect_signals(self):
        self.signal_command.connect(self.command.set_value)
        self.signal_intent.connect(
            lambda i, c: (
                self.intent.set_value(i),
                self.confidence.set_value(f"{c * 100:.1f}%")
            )
        )
        self.signal_response.connect(self.response.set_value)
        self.signal_mic.connect(self.update_mic)

    def start_listening(self):
        """Start listening for voice commands"""
        self.is_listening = True
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

        # Update UI to listening state
        self.signal_mic.emit("LISTENING")
        self.signal_command.emit("Listening...")
        self.signal_response.emit("Ready to receive commands")

        print("Started listening...")

        # Create and start the listener thread
        self.listener_thread = VoiceListenerThread()
        self.listener_thread.command_received.connect(self.on_command_received)
        self.listener_thread.status_changed.connect(self.signal_mic.emit)
        self.listener_thread.start()

        # If you have a voice assistant instance, call its start method
        if self.voice_assistant and hasattr(self.voice_assistant, 'start_listening'):
            self.voice_assistant.start_listening()

    def stop_listening(self):
        """Stop listening for voice commands"""
        self.is_listening = False
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

        # Stop the listener thread
        if self.listener_thread:
            self.listener_thread.stop()
            self.listener_thread = None

        # Update UI to idle state
        self.signal_mic.emit("IDLE")
        self.signal_command.emit("-")
        self.signal_intent.emit("-", 0.0)
        self.signal_response.emit("Stopped listening")

        print("Stopped listening...")

        # If you have a voice assistant instance, call its stop method
        if self.voice_assistant and hasattr(self.voice_assistant, 'stop_listening'):
            self.voice_assistant.stop_listening()

    def on_command_received(self, command):
        """Handle received voice commands"""
        self.signal_command.emit(command)
        print(f"Command received: {command}")

        # TODO: Process the command with your intent recognition
        # Example:
        # intent, confidence = self.voice_assistant.get_intent(command)
        # self.signal_intent.emit(intent, confidence)
        # response = self.voice_assistant.execute_command(command, intent)
        # self.signal_response.emit(response)

    def update_mic(self, state):
        color_map = {
            "LISTENING": "#00FF00",
            "PROCESSING": "#FFAA00",
            "SPEAKING": "#00BFFF",
            "IDLE": "rgba(0, 200, 255, 220)"
        }

        color = color_map.get(state, "rgba(0, 200, 255, 220)")
        self.status.setText(f"● {state}")
        self.status.setStyleSheet(f"""
            color: {color};
            font-size: 14px;
            font-weight: bold;
            padding: 6px 18px;
            background: rgba(0, 20, 40, 150);
            border-radius: 15px;
            border: 1px solid rgba(0, 255, 255, 120);
        """)

        active = state == "LISTENING"
        self.orb.set_active(active)
        self.wave.set_active(active)

    def closeEvent(self, event):
        """Clean up when window is closed"""
        if self.listener_thread:
            self.listener_thread.stop()
        event.accept()


# For testing
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    # Create window without voice assistant for testing
    window = AuraAdvancedGUI()

    # Test the interface with simulated data
    QTimer.singleShot(5000, lambda: window.signal_mic.emit("PROCESSING"))
    QTimer.singleShot(5500, lambda: window.signal_command.emit("Turn on the lights"))
    QTimer.singleShot(6000, lambda: window.signal_intent.emit("Smart Home Control", 0.95))
    QTimer.singleShot(6500, lambda: window.signal_response.emit("Lights have been turned on successfully!"))
    QTimer.singleShot(7000, lambda: window.signal_mic.emit("IDLE"))

    window.show()
    sys.exit(app.exec_())