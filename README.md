<div align="center">

# 🎙️ AURA
### The Voice Controlled AI Desktop Assistant

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![AI](https://img.shields.io/badge/AI-Powered-green?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Enabled-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-red?style=for-the-badge)

*Experience hands-free computing with intelligent voice commands*

[Features](#-features) • [Installation](#️-installation) • [Usage](#-usage) • [Demo](#-demo-video)

---

</div>

## 📋 Table of Contents

- [Overview](#-project-overview)
- [Objectives](#-objectives)
- [Features](#-features)
- [Technologies](#-technologies--tools)
- [Project Structure](#-project-structure)
- [Installation](#️-installation)
- [Usage](#-usage)
- [Voice Commands](#-example-voice-commands)
- [Use Cases](#-use-cases)
- [Future Enhancements](#-future-enhancements)
- [Demo Video](#-demo-video)
- [Author](#-author)
- [License](#-license)

---

## 📌 Project Overview

**Aura** is an advanced voice-controlled AI desktop assistant that revolutionizes the way users interact with their computers. By leveraging cutting-edge speech recognition, natural language processing (NLP), and intelligent system automation, Aura enables seamless hands-free computer operation.

Inspired by industry-leading assistants like **Siri**, **Alexa**, and **J.A.R.V.I.S**, this project demonstrates the practical application of Data Science, AI, NLP, and Human-Computer Interaction principles.

---

## 🎯 Objectives

| Objective | Description |
|-----------|-------------|
| 🎤 **Voice Control** | Enable complete hands-free computer operation using natural voice commands |
| 🧠 **Intent Understanding** | Utilize NLP techniques to accurately detect and interpret user intentions |
| ⚡ **Smart Automation** | Execute system-level actions and application controls intelligently |
| 🔊 **Interactive Feedback** | Provide both voice responses and visual feedback for enhanced user experience |
| 🎨 **Modern Interface** | Create an intuitive and visually appealing graphical user interface |

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎤 Core Capabilities
- ✅ Real-time voice command recognition
- ✅ Advanced intent detection using NLP
- ✅ Desktop application control
- ✅ Web search integration
- ✅ Natural text-to-speech responses

</td>
<td width="50%">

### 🖼️ GUI Features
- ✅ Live system status monitoring
- ✅ Command history display
- ✅ Intent recognition visualization
- ✅ Response logging system
- ✅ Modern, interactive interface

</td>
</tr>
</table>

---

## 🛠️ Technologies & Tools

### 💻 Core Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white) | Core programming language |
| **Speech Recognition** | SpeechRecognition | Voice input processing |
| **Text-to-Speech** | Pyttsx3, gTTS, edge-tts | Voice response generation |
| **NLP** | Custom NLP techniques | Intent recognition & processing |
| **GUI Framework** | PyQt | Graphical user interface |
| **System Control** | OS, Subprocess | System automation & control |
| **API Integration** | Requests | External API communication |

### 🧩 Key Concepts Implemented

```
┌─────────────────────────────────────────────┐
│  🤖 Artificial Intelligence                 │
│  📝 Natural Language Processing (NLP)       │
│  📊 Data Science Fundamentals               │
│  🖱️ Human-Computer Interaction              │
│  ⚡ Event-Driven Programming                │
└─────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
AURA-THE-VOICE-CONTROLLED-ASSISTANT/
│
├── 📁 .idea/                      # IDE configuration files
├── 📁 .venv/                      # Virtual environment
├── 📁 actions/                    # Action handlers and executors
├── 📁 assets/                     # Images, icons, and media files
├── 📁 data/                       # Data files and datasets
├── 📁 gui/                        # GUI components and designs
├── 📁 memory/                     # Context and memory management
├── 📁 utils/                      # Utility functions and helpers
├── 📁 venv/                       # Alternative virtual environment
│
├── 📄 .env                        # Environment variables
├── 📄 .gitignore                  # Git ignore rules
├── 📄 assistant.py                # Main assistant logic
├── 📄 knowledge.py                # Knowledge base management
├── 📄 listener.py                 # Voice input listener
├── 📄 main.py                     # 🚀 Main entry point
├── 📄 nlu.py                      # Natural Language Understanding
├── 📄 README.md                   # Project documentation
├── 📄 requirements.txt            # Python dependencies
├── 📄 router.py                   # Command routing system
├── 📄 screenshot_1769184882.png   # Demo screenshots
├── 📄 screenshot_1769185916.png   
├── 📄 smalltalk.py                # Conversational responses
├── 📄 speaker.py                  # Text-to-speech output
├── 📄 speech_state.py             # Speech state management
├── 📄 test_hf.py                  # Testing scripts
├── 📄 test_qt.py                  
├── 📄 test_video.py               
└── 📄 tts_test.py                 
```

---

## ⚙️ Installation

Follow these steps to set up and run Aura on your local machine:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/developerSakshi365/AURA---Voice-Controlled-Assistant.git
```

### 2️⃣ Navigate to Project Directory

```bash
cd AURA---Voice-Controlled-Assistant
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 4️⃣ Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run Aura 🚀

```bash
python main.py
```

---

## 🎮 Usage

1. **Launch the application** using `python main.py`
2. **Grant microphone permissions** when prompted
3. **Speak your command** clearly after the wake signal
4. **Observe the GUI** for:
   - Voice input recognition
   - Intent detection
   - System response
   - Command history
5. **Receive voice feedback** from Aura

---

## 🗣️ Example Voice Commands

| Command | Action |
|---------|--------|
| 🌐 "Open Chrome" | Launches Google Chrome browser |
| 🔍 "Search Python tutorials" | Searches the web for Python tutorials |
| 📁 "Open file explorer" | Opens Windows File Explorer |
| ⏰ "What is the time?" | Announces current time |
| 🔌 "Shutdown the system" | Initiates system shutdown |
| 📧 "Open Gmail" | Opens Gmail in browser |
| 🎵 "Play music" | Launches music player |
| 💻 "Open VS Code" | Launches Visual Studio Code |

---

## 🎓 Use Cases

<div align="center">

| 🎯 Use Case | 📝 Description |
|------------|---------------|
| **Accessibility** | Assists users with mobility limitations |
| **Productivity** | Hands-free multitasking while working |
| **Education** | Learning AI/NLP concepts practically |
| **Research** | Academic demonstration of HCI |
| **Automation** | Smart home and office automation |

</div>

---

## 🔮 Future Enhancements

- [ ] 🤖 Machine learning-based intent classification
- [ ] 📴 Offline voice processing capabilities
- [ ] 🌍 Cross-platform support (Windows, macOS, Linux)
- [ ] 🧠 Personalized learning from user behavior
- [ ] 🔗 Integration with smart home devices
- [ ] 📱 Mobile companion app
- [ ] 🌐 Multi-language support
- [ ] 🔐 Voice authentication security

---
<!-- 
## 🎥 Demo Video

> **Experience Aura in action!** Watch the complete demonstration below:

### 📺 [Watch Demo Video Here]()
*Click the link above to see Aura's capabilities and features in action*

> 🎬 *Demo video showcasing voice commands, GUI interaction, and system responses*

--- -->

## 👩‍💻 Author

<div align="center">

### **Sakshi Vishwakarma**

🎓 **TYBSc-IT | Data Science**  
💡 **AI & Automation Enthusiast**  
🚀 **Passionate about building intelligent systems**

### 🌐 Connect with Me
<p align="left">
  <a href="https://www.linkedin.com/in/sakshi-vishwakarma-21098b27b" target="_blank">
  <img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="linkedin" height="40" />
</a>
  <a href="mailto:developersakshi365@gmail.com" target="_blank">
    <img align="center" src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="email" height="40" />
  </a>
</p>
</div>

---

## 📜 License

```
This project is developed for educational and academic purposes only.
© 2026 Sakshi Vishwakarma. All Rights Reserved.
```

---

<div align="center">

### ⭐ If you find this project helpful, please consider giving it a star!

**Made with ❤️ and Python**

</div>