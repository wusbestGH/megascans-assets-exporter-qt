from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from settingswindow import SettingsWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Megascans Assets Importer")
        self.setMinimumSize(QSize(640, 480))

        self.init_toolbars()

    def init_toolbars(self):
        self.status_bar: str = ""

        self.top_toolbar = QToolBar("Top Toolbar")
        self.top_toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, self.top_toolbar)

        self.settings_action = QPushButton("Settings")
        self.settings_action.clicked.connect(self.open_settings)
        self.top_toolbar.addWidget(self.settings_action)

        self.bottom_toolbar = QToolBar("Bottom Toolbar")
        self.bottom_toolbar.setMovable(False)
        self.addToolBar(Qt.BottomToolBarArea, self.bottom_toolbar)

        self.status_label = QLabel(self.status_bar)
        self.status_label.setContentsMargins(5, 0, 5, 0)
        self.bottom_toolbar.addWidget(self.status_label)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottom_toolbar.addWidget(spacer)

        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["1K", "2K", "4K"])

        self.export_btn = QPushButton("EXPORT")
        self.bottom_toolbar.addWidget(self.quality_combo)
        self.bottom_toolbar.addWidget(self.export_btn)

    def open_settings(self):
        dialog = SettingsWindow(self)
        dialog.exec()

    def update_status(self, message):
        self.status_label.setText(f"STATUS: {message}")
        print(f"[STATUS] {message}")