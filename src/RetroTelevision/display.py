from PyQt5.QtWidgets import QWidget, QVBoxLayout, QShortcut
from PyQt5.QtGui import QKeySequence
from FileLoader import FileLoader
import vlc
import sys

class Display(QWidget):
    def __init__(self):
        super().__init__()
        self._file_loader = FileLoader()
        self._file_paths = self._file_loader.get_file_paths()
        self._path_index = 0
        self._file_index = 0

        self._configure_layout()
        self._configure_vlc()
        self._bind_key_presses()

    def start(self):
        """Attach VLC video to the widget and start playback"""
        if sys.platform.startswith("linux"):
            self.player.set_xwindow(self.winId())
        elif sys.platform == "win32":
            self.player.set_hwnd(self.winId())
        elif sys.platform == "darwin":
            # On macOS, winId() must be cast to int
            self.player.set_nsobject(int(self.winId()))

        self.player.play()

    def _configure_layout(self):
        """Sets up the UI layout"""
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def _configure_vlc(self):
        """Configure the VLC element"""
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self._load_media(self._file_paths[0][0])
        event_manager = self.player.event_manager()
        event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self._on_media_finished)

    def _bind_key_presses(self):
        """Bind keyboard shortcuts"""
        self.shortcut_next = QShortcut(QKeySequence("N"), self)
        self.shortcut_next.activated.connect(self._next_media)

    def _on_media_finished(self, event):
        self._next_media()

    def _next_media(self):
        """Stop current media and play the next one"""
        self.player.stop()
        next_media = self._get_next_media()
        if next_media:
            self._load_media(next_media)
            self.player.play()

    def _load_media(self, path):
        """Load a media file into VLC player"""
        if path:
            media = self.instance.media_new(path)
            self.player.set_media(media)

    def _get_next_media(self):
        """Get the next media file path"""
        path_count = len(self._file_paths)
        if path_count == 0:
            return None

        if path_count == 1:
            self._increment_file_index()
            return self._file_paths[0][self._file_index]

        self._path_index += 1
        if self._path_index >= path_count:
            self._path_index = 0
        self._increment_file_index()
        return self._file_paths[self._path_index][self._file_index]

    def _increment_file_index(self):
        """Cycle through files in the current path"""
        self._file_index += 1
        if self._file_index >= len(self._file_paths[0]):
            self._file_index = 0
