# speaker.py
import asyncio
import edge_tts
import tempfile
import os
import threading

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

VOICE_NAME = "en-US-GuyNeural"

_player = QMediaPlayer()
_lock = threading.Lock()
_current_file = None


async def _generate_audio(text: str, path: str):
    communicate = edge_tts.Communicate(text, VOICE_NAME)
    with open(path, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])


def _speak_worker(text: str):
    global _current_file

    with _lock:
        stop_speaking()

        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        _current_file = tmp.name
        tmp.close()

    asyncio.run(_generate_audio(text, _current_file))

    _player.setMedia(QMediaContent(QUrl.fromLocalFile(_current_file)))
    _player.play()


def speak(text: str):
    if not text:
        return

    threading.Thread(
        target=_speak_worker,
        args=(text,),
        daemon=True
    ).start()


def stop_speaking():
    global _current_file
    _player.stop()
    if _current_file and os.path.exists(_current_file):
        try:
            os.remove(_current_file)
        except:
            pass
        _current_file = None
