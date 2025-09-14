from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QShortcut
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QKeySequence
from FileLoader import FileLoader

class Display:

    def __init__(self):
        self._app = QApplication([])
        self._player = QMediaPlayer()
        self._video_widget = QVideoWidget()
        self._player.mediaStatusChanged.connect(self.on_media_status_changed)
        self._window = QWidget()
        self._file_paths = None
        self.file_loader = FileLoader()
        self._path_index = 0
        self._file_index = 0

    def on_media_status_changed(self, status):
        if status != QMediaPlayer.MediaStatus.EndOfMedia:
            return
        
        self._next_media()

    def configure(self):
        self._file_paths = self.file_loader.get_file_paths()
        self._window.setWindowTitle("Retro Television")

        self._bind_key_presses()

        layout = QVBoxLayout()
        layout.addWidget(self._video_widget)

        self._player.setVideoOutput(self._video_widget)
        self._player.setMedia(QMediaContent(QUrl.fromLocalFile(self._file_paths[self._path_index][self._file_index])))

        self._window.setLayout(layout)
        self._window.showFullScreen()

    def start(self):
        self._player.play()
        self._app.exec()

    def _bind_key_presses(self):
        self.shortcut = QShortcut(QKeySequence("N"), self._video_widget)
        self.shortcut.activated.connect(self._next_media)

    def _next_media(self):
        self._player.stop()
        media_path = self._get_next_media()
        if media_path == None:
            return
        
        self._player.setMedia(QMediaContent(QUrl.fromLocalFile(media_path)))
        self._player.play()

    def _get_next_media(self):
        path_count = len(self._file_paths)
        if path_count == 0:
            return None
        
        if path_count == 1:
            self._increment_file_index()
            return self._file_paths[0][self._file_index]
        
        self._path_index = self._path_index + 1
        if self._path_index > path_count:
            self._path_index = 0
        self._increment_file_index()
        return self._file_paths[self._path_index][self._file_index]

    def _increment_file_index(self):
        self._file_index = self._file_index + 1
        if self._file_index >= len(self._file_paths[0]):
            self._file_index = 0

