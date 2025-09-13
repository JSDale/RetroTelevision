from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

class Display:

    def __init__(self):
        self._app = QApplication([])
        self._player = QMediaPlayer()
        self._player.mediaStatusChanged.connect(self.on_media_status_changed)
        self._window = QWidget()

    def on_media_status_changed(status):
        if status != QMediaPlayer.MediaStatus.EndOfMedia:
            return
        print('next file')

    def configure(self):
        self._window.setWindowTitle("Retro Television")

        layout = QVBoxLayout()
        video_widget = QVideoWidget()
        layout.addWidget(video_widget)

        self._player.setVideoOutput(video_widget)
        self._player.setMedia(QMediaContent(QUrl.fromLocalFile("/Users/jacobdale/Desktop/20220716_133618.mp4")))

        self._window.setLayout(layout)
        self._window.showFullScreen()

    def start(self):
        self._player.play()
        self._app.exec()