import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)

w = QWidget()
w.resize(800, 600)

video = QVideoWidget(w)
video.setGeometry(0, 0, 800, 600)

player = QMediaPlayer()
player.setVideoOutput(video)
player.setMedia(QMediaContent(QUrl.fromLocalFile("assets/boot.gif")))
player.setVolume(0)
player.play()

w.show()
sys.exit(app.exec_())
