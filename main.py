import sys
from PySide6.QtWidgets import *
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.update_status("Just go fuck off")
    window.show()
    sys.exit(app.exec())