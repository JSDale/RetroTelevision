from display import Display
from PyQt5.QtWidgets import QApplication
import sys
import signal

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    display = Display()
    display.showFullScreen()
    display.start()
    sys.exit(app.exec_())
