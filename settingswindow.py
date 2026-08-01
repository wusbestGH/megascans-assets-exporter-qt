from PySide6.QtWidgets import *
import json

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(300, 180)

        self.layout = QVBoxLayout(self)

        self.port_layout = QHBoxLayout()
        self.port_label = QLabel("PORT:")
        self.port_input = QLineEdit()
        self.port_layout.addWidget(self.port_label)
        self.port_layout.addWidget(self.port_input)

        self.app_layout = QHBoxLayout()
        self.app_label = QLabel("APP:")
        self.app_combo = QComboBox()
        self.app_combo.addItems(["Blender", "Cinema 4D", "Maya", "Houdini"])

        self.app_layout.addWidget(self.app_label)
        self.app_layout.addWidget(self.app_combo)

        self.path_layout = QHBoxLayout()
        self.path_label = QLabel("PATH:")
        self.path_input = QLineEdit()
        self.path_layout.addWidget(self.path_label)
        self.path_layout.addWidget(self.path_input)

        self.save_btn = QPushButton("Save Settings")
        self.save_btn.clicked.connect(self.accept)

        self.layout.addLayout(self.port_layout)
        self.app_layout.addWidget(self.app_combo)
        self.layout.addLayout(self.app_layout)
        self.layout.addLayout(self.path_layout)
        self.layout.addWidget(self.save_btn)

    def get_input_data(self):
        return {
            "path": self.path_input.text(),
            "app": self.app_combo.currentText(),
            "port": self.port_input.text()
        }
